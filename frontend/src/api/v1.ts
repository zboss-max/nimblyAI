import {request} from '@/utils/request'

const API_VERSION = '/v1'


export function get<T>(path: string, params?: Record<string, unknown>): Promise<T> {
  return request<T>(
    {
      url: API_VERSION + path,
      method: 'get',
      params
    }
  )
}

export function post<T>(path: string, data?: unknown): Promise<T> {
  return request<T>(
    {
      url: API_VERSION + path,
      method: 'post',
      data
    }
  )
}
