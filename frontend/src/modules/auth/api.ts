/**
 * 模块专用api
 */
import {post} from '@/api/v1'

import type {
  SignInPayload,
  SignInResult,
  SignUpPayload
} from '@/modules/auth/types'


// auth 模块的接口路径前缀
const AUTH_PREFIX = '/auth'


/** 登录 */
export function signIn(payload: SignInPayload): Promise<SignInResult> {
  return post<SignInResult>(
    AUTH_PREFIX + '/signin',
    payload
  )
}

/** 注册 */
export function signUp(payload: SignUpPayload) {
  return post(
    AUTH_PREFIX + '/signup',
    payload
  )
}
