/**
 *  pinia共享
 */
import {defineStore} from 'pinia'
import {ref, computed} from 'vue'

import {
  getToken,
  setToken,
  clearToken,
  getUser,
  setUser,
  clearUser
} from "@/modules/auth/storage"
import {signIn as signInApi} from "@/modules/auth/api";

import type {
  UserInfo,
  SignInPayload
} from "@/modules/auth/types"


/** 创建用户共享,共享名user */
export const useUserStore = defineStore(
  'user'
  ,
  () => {

    // ---------- 状态：会变的数据 ----------
    const token = ref<string | null>(getToken())
    const user = ref<UserInfo | null>(getUser())

    // ---------- 派生状态：由状态算出来的，不单独存 ----------
    const isSignedIn = computed(
      () => Boolean(token.value)
    )
    const displayName = computed(
      () => user.value?.username ||
        user.value?.phone ||
        user.value?.email ||
        '用户'
    )

    // ---------- 动作：外部应通过这些方法修改用户状态 ----------
    async function signIn(payload: SignInPayload) {
      const result = await signInApi(payload)

      // 修改状态
      token.value = result.token
      user.value = result.user
      // 存储
      setToken(result.token)
      setUser(result.user)
    }

    function signOut() {
      token.value = null
      user.value = null
      clearToken()
      clearUser()
    }

    return {token, user, isSignedIn, displayName, signIn, signOut}
  }
)


