/**
 * 请求体
 */

import axios from 'axios'
import {ElMessage} from 'element-plus'
import router from "@/router";

import {getToken} from "@/modules/auth/storage";

import {
  type AxiosInstance,
  type AxiosError,
  type AxiosRequestConfig
} from 'axios'
import type {ApiResponse} from "@/types/api";


/** 请求地址 */
const http: AxiosInstance = axios.create(
  {
    baseURL: '/api',
    timeout: 10000,
  }
)

/**
 * 唯一出口：解包 {code,msg,data}，直接返回 data
 * 泛型 <T> 让调用方写 post<SignInResult>() 就能拿到带类型的返回值
 */
export async function request<T>(config: AxiosRequestConfig): Promise<T> {
  const response = await http.request<ApiResponse<T>>(config)
  const body = response.data
  if (body.code !== 0) {
    // 兜底：万一后端用 200 返回了业务错误
    ElMessage.error(body.msg || '请求失败')
    throw new Error(body.msg || '请求失败')
  }
  return body.data
}


/**
 * 拦截器
 */
// 请求拦截器：每个请求出去前自动挂上 Authorization
http.interceptors.request.use(
  (config) => {
    const token = getToken()
    if (token) {
      config.headers.Authorization = 'Bearer ' + token
    }
    return config
  }
)
// 响应拦截器：只处理“失败的 HTTP 状态”
http.interceptors.response.use(
  // 响应成功走第1个
  (response) => response
  ,
  // 响应失败走第2个
  async (error: AxiosError<ApiResponse<unknown>>) => {
    const status = error.response?.status
    const msg = error.response?.data?.msg
      ?? '网络异常'

    // 登录过期走401，账密错误也走401
    const isSignIn = error.config?.url?.includes('/auth/signin')
      ?? false
    // 不在登陆页面的话，清除登录信息，并跳转到登录页
    if (status === 401 && !isSignIn) {
      await reSignIn()
    } else {
      ElMessage.error(msg)
    }
    return Promise.reject(error) // 继续抛给页面，让页面能 catch
  }
)

/** 重新登录 */
async function reSignIn() {
  // 动态引入，避免 request.ts 和 user Store 相互静态引用
  const {useUserStore} = await import('@/modules/auth')
  const userStore = useUserStore()

  // 一次清理 Pinia 和 LocalStorage 中的登录状态
  userStore.signOut()

  ElMessage.error('登录已过期，请重新登录')
  router.replace({name: 'auth-signin'})
}


