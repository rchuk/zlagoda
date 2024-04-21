import {BaseIntIdCriteria, BaseStringIdCriteria} from "../../../../../generated";

export type EntityId = number | string;

export interface BaseEntity<IdT extends EntityId> {
  id: IdT
}

export function createIdsCriteria<EntityT extends BaseEntity<number>>(list: EntityT[] | null): BaseIntIdCriteria {
  return extractIds(list);
}

export function createStringIdsCriteria<EntityT extends BaseEntity<string>>(list: EntityT[] | null): BaseStringIdCriteria {
  return extractIds(list);
}

function extractIds<EntityT extends BaseEntity<IdT>, IdT extends EntityId>(list: EntityT[] | null): { ids: IdT[] } {
  return {
    ids: list?.map(item => item.id) ?? []
  };
}

export function findEntity<EntityT extends BaseEntity<IdT>, IdT extends EntityId>
  (list: EntityT[] | null, id: IdT): EntityT | null {
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
