import dayjs from "dayjs";

interface NameEntity {
  firstName: string,
  lastName: string,
  patronymic?: string
}

export function getEntityPersonFullName(entity: NameEntity | null): string {
  return entity ? joinName(entity.firstName, entity.lastName) : "";
}

export function getEntityPersonFullNameWithPatronymic(entity: NameEntity | null): string {
  return entity ? joinName(entity.firstName, entity.lastName, entity.patronymic) : "";
}

export function joinName(firstName: string, lastName: string, patronymic?: string): string {
  let fullName = `${lastName} ${firstName}`;
  if (patronymic != null)
    return`${fullName} ${patronymic}`;

  return fullName;
}

export function formatDate(date: Date | null): string {
  return date ? dayjs(date).format("DD.MM.YYYY") : "";
}

export function formatDateTime(dateTime: Date | null): string {
  return dateTime ? dayjs(dateTime).format("DD.MM.YYYY HH:mm:ss") : "";
}
