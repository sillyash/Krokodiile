import { defineStore } from 'pinia'
import { computed, ref } from 'vue'

import { api, setCsrfToken } from '@/api/client'
import { API_URL, AUTH_ENDPOINTS } from '@/config'

export interface User {
  id: number
  username: string
  name: string
}

interface MeResponse {
  user: User | null
  csrfToken: string
}

export const useAuthStore = defineStore('auth', () => {
  const user = ref<User | null>(null)
  const loaded = ref(false)
  const isLoggedIn = computed(() => user.value !== null)

  async function fetchMe() {
    try {
      const { data } = await api.get<MeResponse>(AUTH_ENDPOINTS.me)
      user.value = data.user
      setCsrfToken(data.csrfToken)
    } catch {
      user.value = null
    } finally {
      loaded.value = true
    }
  }

  /** Arise Connect login, coming back to `next` (a frontend route) afterwards. */
  function loginUrl(next = '/') {
    return `${API_URL}${AUTH_ENDPOINTS.login}?next=${encodeURIComponent(next)}`
  }

  async function logout() {
    await api.post(AUTH_ENDPOINTS.logout)
    // The session (and its CSRF token) changed.
    await fetchMe()
  }

  return { user, loaded, isLoggedIn, fetchMe, loginUrl, logout }
})
