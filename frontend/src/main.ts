import {createApp} from 'vue'
import {createPinia} from 'pinia'
import ElementPlus from 'element-plus'

import App from './App.vue'
import router from './router'

// Element 基础样式
import 'element-plus/dist/index.css'
//
import '@/styles/tokens.css'
//
import '@/styles/base.css'
//
import '@/styles/element-plus.css'


const app = createApp(App)

app.use(createPinia()) // 全局状态
app.use(router) // 路由
app.use(ElementPlus) // UI 组件库

app.mount('#app')
