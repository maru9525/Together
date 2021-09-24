import http from '@/api/http'
import { AxiosResponse } from 'axios'

export function login(
  userEmail: string,
  password: string
): Promise<AxiosResponse> {
  return http.post('/login', {
    userEmail,
    password,
  })
}

export function register(
  userEmail: string,
  password: string,
  nickName: string,
  name: string,
  phoneNumber: string
): Promise<AxiosResponse> {
  return http.post('/register', {
    userEmail,
    password,
    nickName,
    name,
    phoneNumber,
  })
}
