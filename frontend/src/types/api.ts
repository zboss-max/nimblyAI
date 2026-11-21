/**
 * 后端统一响应体
 * 泛型 T 代表 data 的真实类型，调用时由使用方指定
 */
export interface ApiResponse<T> {
  code: number;
  msg: string;
  data: T;
}
