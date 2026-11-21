<script setup lang="ts">
type AuthMode = 'signin' | 'signup'

const props = defineProps<{
  mode: AuthMode
}>()

const content = {
  signin: {
    title: '欢迎回来',
    subtitle: '登录账号，继续你的智能工作流。',
  },
  signup: {
    title: '创建账号',
    subtitle: '加入 Nimbly AI，开启高效创造之旅。',
  },
} as const
</script>

<template>
  <div class="sign-layout">
    <aside class="sign-brand">

      <router-link class="brand-logo" :to="{ name: 'marketing-home' }">
        <img
          class="brand-logo__mark"
          src="/favicon.ico"
          alt=""
          aria-hidden="true"
        />
        <span>NIMBLY <strong>AI</strong></span>
      </router-link>

      <div class="brand-copy">
        <p class="brand-copy__eyebrow">INTELLIGENT WORKFLOW</p>
        <h1>
          让想法，<br/>
          <span>即刻成为现实。</span>
        </h1>
        <p class="brand-copy__description">
          连接灵感与效率，用智能技术简化每一次创造。
        </p>
      </div>

      <p class="brand-footer">© 2026 Nimbly AI · Build what matters.</p>
    </aside>

    <main class="sign-content">
      <section class="sign-card">

        <router-link class="sign-card__logo" :to="{ name: 'marketing-home' }">
          <img
            class="brand-logo__mark"
            src="/favicon.ico"
            alt=""
            aria-hidden="true"
          />
          <span>NIMBLY <strong>AI</strong></span>
        </router-link>

        <header class="sign-card__header">
          <h2>{{ content[props.mode].title }}</h2>
          <p>{{ content[props.mode].subtitle }}</p>
        </header>

        <!-- 登录或注册表单由使用方传入 -->
        <slot/>
      </section>
    </main>
  </div>
</template>

<style scoped>
.sign-layout {
  display: grid;
  grid-template-columns: minmax(0, 1.05fr) minmax(400px, 0.95fr);
  min-height: 100vh;
}

.sign-brand {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: clamp(32px, 5vw, 72px);
}

.brand-logo,
.sign-card__logo {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  font-size: 15px;
  font-weight: 600;
  letter-spacing: 0.14em;
}

.brand-logo {
  align-self: flex-start;
}

.brand-logo__mark {
  display: grid;
  flex: 0 0 auto;
  width: 38px;
  height: 38px;
  padding: 6px;
  object-fit: contain;
  place-items: center;
  border: 1px solid var(--color-border-active);
  border-radius: 11px;
  background: rgba(56, 189, 248, 0.08);
  box-shadow: var(--shadow-glow);
}


.brand-logo strong,
.sign-card__logo strong {
  color: var(--color-primary);
}

.brand-copy {
  max-width: 620px;
}

.brand-copy__eyebrow {
  margin-bottom: 24px;
  color: var(--color-primary);
  font-size: 12px;
  letter-spacing: 0.22em;
}

.brand-copy h1 {
  font-size: clamp(42px, 5vw, 72px);
  line-height: 1.12;
  letter-spacing: -0.04em;
}

.brand-copy h1 span {
  background: var(--gradient-primary);
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.brand-copy__description {
  max-width: 420px;
  margin-top: 28px;
  color: var(--color-text-secondary);
  line-height: 1.8;
}

.brand-footer {
  color: var(--color-muted);
  font-size: 12px;
}

.sign-content {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 200px 40px 24px; /* 上、右、下、左 */

}

.sign-card {
  width: min(100%, 440px);
  padding: 34px;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  background: var(--color-surface);
  box-shadow: var(--shadow-card);
  backdrop-filter: blur(20px);
}

.sign-card__logo {
  margin-bottom: 28px;
}

.sign-card__header {
  margin-bottom: 28px;
}

.sign-card__header h2 {
  font-size: 28px;
  letter-spacing: -0.02em;
}

.sign-card__header p {
  margin-top: 8px;
  color: var(--color-text-secondary);
  font-size: 14px;
}

@media (max-width: 900px) {
  .sign-layout {
    grid-template-columns: 1fr;
  }

  .sign-brand {
    display: none;
  }

  .sign-content {
    min-height: 100vh;
    padding: 24px 16px;
  }

  .sign-card {
    padding: 28px 22px;
  }
}
</style>
