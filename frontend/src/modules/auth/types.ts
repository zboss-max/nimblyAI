/**
 * auth 模块的类型定义
 * 原则：字段名照抄后端 JSON，不做任何改名，改名就等于给自己挖坑
 */

/** 用户信息 */
export interface UserInfo {
  username: string | null
  phone: string | null
  email: string | null
  create_time: string | null
}

/** 登录入参 */
export interface SignInPayload {
  identifier: string // 用户名 / 手机号 / 邮箱，三选一
  password: string
}

/** 登录返回 */
export interface SignInResult {
  token: string
  user: UserInfo
}

/** 注册入参 */
export interface SignUpPayload {
  username?: string // ? = 可以不传（前端没填就不发这个字段）
  phone?: string
  email?: string
  password: string
}
