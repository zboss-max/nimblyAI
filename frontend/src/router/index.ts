import {createRouter, createWebHistory} from 'vue-router'

import marketingRoutes from "@/modules/marketing/routes";
import authRoutes from "@/modules/auth/routes"


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    ...marketingRoutes,
    ...authRoutes,
  ],
})


/**
 * 全局前置守卫：每次页面跳转前执行。
 * to：准备访问的页面；return 路由对象表示改道；不返回则正常放行。
 */
router.beforeEach(
  async (to) => {
    // 动态引入，避免 router → user store → request → router 的循环依赖
    const { useUserStore } = await import('@/modules/auth/store')
    const userStore = useUserStore()

    // 情况一：目标页面要求登录，但本地没有 Token，改去登录页
    if (to.meta.requiresAuth && !userStore.isSignedIn) {
      return {
        name: 'auth-signin',
        query: {
          // 记录原本想去的地址，下一步登录成功后可以跳回来
          redirect: to.fullPath,
        },
      }
    }

    // 情况二：已经登录，不再停留在登录或注册页，去首页
    const isAuthPage = to.name === 'auth-signin' || to.name === 'auth-signup'
    if (userStore.isSignedIn && isAuthPage) {
      return { name: 'marketing-home' }
    }

    // 其他情况正常放行
  }
)

export default router
