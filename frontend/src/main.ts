import {createApp} from 'vue'
import {createPinia} from 'pinia'
import ElementPlus from 'element-plus'

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia()) // 全局状态
app.use(router) // 路由
app.use(ElementPlus) // UI 组件库

app.mount('#app')
