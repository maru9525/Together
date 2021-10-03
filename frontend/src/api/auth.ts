import http from '@/api/http'
import { keysToCamel } from '@/libs/func'
import { OutputUser, InputUser } from '@/libs/interface'
import axios, { AxiosResponse } from 'axios'

interface AuthResponseData {
  accessToken: string
  refreshToken: string
  user: OutputUser
}

export const login = async (
  email: string,
  password: string
): Promise<AuthResponseData> => {
  try {
    const res = await http.post('account/login/', {
      email,
      password,
    })
    return keysToCamel(res.data)
  } catch (error) {
    throw new Error('로그인 실패')
  }
}

export const register = async (
  name: string,
  email: string,
  password1: string,
  password2: string,
  phoneNumber: string,
  nickname: string
): Promise<AuthResponseData> => {
  return http.post('account/register/', {
    username: name,
    email: email,
    password1: password1,
    password2: password2,
    phone_number: phoneNumber,
    nickname: nickname,
  })
}

export function resetPassword(email: string): Promise<AxiosResponse> {
  return http.post('account/password/reset/', { email: email })
}

export function resetPasswordConfirm(
  uid: string,
  token: string,
  password1: string,
  password2: string
): Promise<AxiosResponse> {
  return http.post('account/password/reset/confirm/', {
    uid: uid,
    token: token,
    new_password1: password1,
    new_password2: password2,
  })
}

export const getUserData = async (userId: number): Promise<OutputUser> => {
  try {
    // const res: AxiosResponse<InputUser> = await http.get(`account/${userId}/`)
    const res: AxiosResponse<InputUser> = await axios.get(
      `http://localhost:3000/account/${userId}/`
    )
    const user: OutputUser = keysToCamel(res.data)
    console.log(user)
    return user
  } catch (error) {
    throw new Error('에러 발생')
  }
}
