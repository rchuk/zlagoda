import {BaseCriteria} from "../../../../../generated";

interface BaseEntity {
  id: number
}

export function createIdsCriteria<EntityT extends BaseEntity>(list: EntityT[] | null): BaseCriteria {
  return {
    ids: list?.map(item => item.id) ?? []
  };
}

export function findEntity<EntityT extends BaseEntity>(list: EntityT[] | null, id: number): EntityT | null {
  return list?.find(entity => entity.id == id) ?? null;
}

/*
export function entityListToMap<EntityT extends {id: number}>(list: EntityT[]): Map<number, EntityT> {
  return new Map(list.map(entity => {
    return [entity.id, entity];
  }));
}

export function entityListToMapSplit<EntityT extends {id: number}>(list: EntityT[]): Map<number, Omit<EntityT, "id">> {
  return new Map(list.map(entity => {
    const {id, ...other} = entity;

    return [id, other];
  }));
}
*/
