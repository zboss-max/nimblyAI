<script setup lang="ts">
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import { useUserStore } from '@/modules/auth'

const router = useRouter()
const userStore = useUserStore()

function handleSignOut() {
  userStore.signOut()          // 已经清了 Pinia + localStorage
  ElMessage.success('已退出登录')
  router.replace({ name: 'marketing-home' })  // 留在首页
}
</script>

<template>
  <h1>Hello</h1>
  <el-button
    v-if="userStore.isSignedIn"
    type="danger"
    @click="handleSignOut"
  >
    登出
  </el-button>
</template>
