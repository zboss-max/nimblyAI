import type {RouteRecordRaw} from 'vue-router'


/** auth 模块路由 */
const authRoutes: RouteRecordRaw[] = [
  {
    path: '/signin',
    name: 'auth-signin',

    component: () => import('@/modules/auth/views/SignInView.vue'),

    meta: {
      title: '登录',
      requiresAuth: false
    },
  },

  {
    path: '/signup',
    name: 'auth-signup',

    component: () => import('@/modules/auth/views/SignUpView.vue'),

    meta: {
      title: '注册',
      requiresAuth: false
    },
  },
]

export default authRoutes
