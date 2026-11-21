/**
 * localStorage 里的读写，集中在一处，方便以后换成 cookie
 */
import type {UserInfo} from "@/modules/auth/types"


/** token */
const TOKEN_KEY = 'nimbly_token'

/** 获取token */
export function getToken(): string | null {
  const token = localStorage.getItem(TOKEN_KEY)
  if (!token) return null
  return token
}

/** 写入token */
export function setToken(token: string) {
  localStorage.setItem(TOKEN_KEY, token)
}

/** 清除token */
export function clearToken() {
  localStorage.removeItem(TOKEN_KEY)
}


/** user */
const USER_KEY = 'nimbly_user'

/** 读取用户 */
export function getUser(): UserInfo | null {
  const user = localStorage.getItem(USER_KEY)

  if (!user) return null
  try {
    // JSON.parse 返回 any，这里断言成我们存储时的形状
    return JSON.parse(user) as UserInfo
  } catch {
    // 存储被手动改坏时自愈，不留垃圾
    localStorage.removeItem(USER_KEY)

    return null
  }
}

export function setUser(user: UserInfo) {
  localStorage.setItem(USER_KEY, JSON.stringify(user))
}

export function clearUser() {
  localStorage.removeItem(USER_KEY)
}

