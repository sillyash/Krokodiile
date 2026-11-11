import axios from 'axios'

import { API_URL } from '@/config'

const SAFE_METHODS = ['get', 'head', 'options']

let csrfToken = ''

/** Set from `/auth/me/`: the API cookie can't be read from the frontend origin. */
export function setCsrfToken(token: string) {
  csrfToken = token
}

export const api = axios.create({
  baseURL: API_URL,
  withCredentials: true,
})

api.interceptors.request.use((config) => {
  if (csrfToken && !SAFE_METHODS.includes(config.method ?? 'get')) {
    config.headers.set('X-CSRFToken', csrfToken)
  }
  return config
})
