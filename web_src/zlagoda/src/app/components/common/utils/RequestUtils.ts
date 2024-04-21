import {FetchError, ResponseError} from "../../../../../generated";


export async function getRequestError(reason: unknown): Promise<string> {
  if (reason instanceof ResponseError) {
    const text = await reason.response.text();
    if (text.length != 0)
      return text;
  } else if (reason instanceof FetchError) {
    return "Не вдалося отримати дані";
  }

  if (reason instanceof Object)
    return reason.toString();

  return "Невідома помилка";
}
