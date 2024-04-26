from psycopg import AsyncConnection
from psycopg.rows import class_row

from employee.models import Employee
from employee.schemas import EmployeeCriteria
from database import db_conn
from exceptions import ValidationError
from utils import like_format, generate_random_str_id


def dto_field_to_entity_field(dto_field: str | None) -> str:
    if dto_field is None:
        return "id"

    fields = {
        "id": "id",
        "lastName": "last_name",
        "firstName": "first_name",
        "patronymic": "patronymic",
        "role": "role",
        "salary": "salary",
        "birthDate": "birth_date",
        "workStartDate": "work_start_date",
        "phoneNumber": "phone_number",
        "city": "city",
        "street": "street",
        "zipCode": "zip_code"
    }

    entity_field = fields.get(dto_field)
    if entity_field is None:
        raise ValidationError("Вказане поле для сортування не вірне")

    return entity_field

@db_conn
async def create(model: Employee, conn: AsyncConnection) -> str:
    model.id = generate_random_str_id(10)
    query = """
        INSERT INTO employee(id, last_name, first_name, patronymic, role, salary, birth_date, work_start_date, phone_number, city, street, zip_code)
        VALUES (%(id)s, %(last_name)s, %(first_name)s, %(patronymic)s, %(role)s, %(salary)s, %(birth_date)s, %(work_start_date)s, %(phone_number)s, %(city)s, %(street)s, %(zip_code)s)
        RETURNING id;
        """
    params = model.dict()
    async with conn.cursor() as cur:
        res = (await (await cur.execute(query, params)).fetchone())[0]
    return res


@db_conn
async def read(criteria: EmployeeCriteria, conn: AsyncConnection) -> list[Employee]:
    sort_field = dto_field_to_entity_field(criteria.sort_field)
    query = f"""
        SELECT *
        FROM employee 
        WHERE 
        {"id = ANY(%(ids)s)" if criteria.ids is not None else "TRUE"} AND 
        {"role = %(role)s" if criteria.role is not None else "TRUE"} AND 
        {("(last_name LIKE %(query)s OR "
          "first_name LIKE %(query)s OR "
          "patronymic LIKE %(query)s OR "
          "phone_number LIKE %(query)s OR "
          "city LIKE %(query)s OR "
          "street LIKE %(query)s OR "
          "zip_code LIKE %(query)s) ") if criteria.query is not None else "TRUE "}
        ORDER BY {sort_field} {'ASC ' if criteria.sort_ascending is None or criteria.sort_ascending else 'DESC '}
        {'LIMIT %(limit)s OFFSET %(offset)s ' if criteria.limit is not None and criteria.offset is not None else ''};
        """
    params = criteria.dict()
    if "query" in params:
        params["query"] = await like_format(params["query"])
    async with conn.cursor(row_factory=class_row(Employee)) as cur:
        res = await (await cur.execute(query, params)).fetchall()
    return res


@db_conn
async def read_one(id: str, conn: AsyncConnection) -> Employee:
    query = f"""
        SELECT *
        FROM employee 
        WHERE id = %s;
        """
    params = (id,)
    async with conn.cursor(row_factory=class_row(Employee)) as cur:
        res = await (await cur.execute(query, params)).fetchone()
    return res


@db_conn
async def update(model: Employee, conn: AsyncConnection) -> bool:
    query = """
    UPDATE employee
    SET 
    last_name = %(last_name)s,
    first_name = %(first_name)s,
    patronymic = %(patronymic)s,
    role = %(role)s,
    salary = %(salary)s,
    birth_date = %(birth_date)s,
    work_start_date = %(work_start_date)s,
    phone_number = %(phone_number)s,
    city = %(city)s,
    street = %(street)s,
    zip_code = %(zip_code)s
    WHERE id = %(id)s;
    """
    params = model.dict()
    async with conn.cursor() as cur:
        await cur.execute(query, params)
    return True


@db_conn
async def delete(id: str, conn: AsyncConnection) -> bool:
    query = """
    DELETE FROM employee
    WHERE id = %s;
    """
    params = (id,)
    async with conn.cursor() as cur:
        await cur.execute(query, params)
    return True


@db_conn
async def count(criteria: EmployeeCriteria, conn: AsyncConnection) -> int:
    query = f"""
        SELECT COUNT(*)
        FROM employee 
        WHERE 
        {"id = ANY(%(ids)s)" if criteria.ids is not None else "TRUE"} AND 
        {"role = %(role)s" if criteria.role is not None else "TRUE"} AND
        {("(last_name LIKE %(query)s OR "
          "first_name LIKE %(query)s OR "
          "patronymic LIKE %(query)s OR "
          "phone_number LIKE %(query)s OR "
          "city LIKE %(query)s OR "
          "street LIKE %(query)s OR "
          "zip_code LIKE %(query)s)") if criteria.query is not None else "TRUE"};
        """
    params = criteria.dict()
    if "query" in params:
        params["query"] = await like_format(params["query"])
    async with conn.cursor() as cur:
        res = (await (await cur.execute(query, params)).fetchone())[0]
    return res
