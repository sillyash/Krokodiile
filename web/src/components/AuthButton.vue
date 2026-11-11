<script setup lang="ts">
import { useRoute } from 'vue-router'

import { useAuthStore } from '@/stores/auth'

const auth = useAuthStore()
const route = useRoute()
</script>

<template>
  <div v-if="auth.loaded" class="auth">
    <template v-if="auth.user">
      <span class="auth-name">{{ auth.user.name }}</span>
      <button type="button" class="auth-action" @click="auth.logout()">Déconnexion</button>
    </template>
    <a v-else class="auth-action" :href="auth.loginUrl(route.fullPath)">Connexion</a>
  </div>
</template>

<style scoped>
.auth {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.auth-name {
  font-weight: bold;
}

.auth-action {
  padding: 0.4rem 0.9rem;
  border: 2px solid var(--color-border);
  border-radius: 999px;
  background: var(--color-surface);
  color: var(--color-text);
  font: inherit;
  font-weight: bold;
  text-decoration: none;
  cursor: pointer;
}

.auth-action:hover {
  color: var(--color-accent);
}
</style>
