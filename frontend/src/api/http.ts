import store from '@/store'
import axios from 'axios'

const http = axios.create({
  baseURL: 'http://j5d202.p.ssafy.io',
})

http.interceptors.request.use(function (config) {
  const accessToken = store.getters['auth/getToken']
  if (accessToken) {
    config.headers['Authorization'] = `Bearer ${accessToken}`
  }
  return config
})

export default http
