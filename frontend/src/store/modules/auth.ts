import * as authApi from '@/api/auth'
import { Module } from 'vuex'
import { RootState } from '@/store/index'

interface authModule {
  accessToken: string
  refreshToken: string
  resetPassword: boolean
}

interface loginResponseData {
  access_token: string
  refresh_token: string
  user: {
    pk: number
    email: string
    nickname: string
    username: string
    phone_number: string
  }
}

export const auth: Module<authModule, RootState> = {
  namespaced: true,
  state: {
    accessToken: '',
    refreshToken: '',
    resetPassword: false,
  },
  mutations: {
    setLoginData(state: authModule, loginData: loginResponseData): void {
      state.accessToken = loginData.access_token
      state.refreshToken = loginData.refresh_token
      console.log('auth modules: login mutation success')
    },
    setResetPassword(state: authModule): void {
      state.resetPassword = true
      console.log(
        'auth modules: resetPassword state becomes true: 임시 비밀번호 발급 완료'
      )
    },
    setChangePassword(state: authModule): void {
      state.resetPassword = false
      console.log(
        'auth modules: resetPassword state becomes false: 비밀번호 변경 완료'
      )
    },
  },
  actions: {
    async login({ commit }, params) {
      try {
        const response = await authApi.login(params.email, params.password)
        if (response.status === 200) {
          commit('setLoginData', response.data)
          alert('auth modules: login success')
        }
        return response
      } catch (err: any) {
        const errorKeys = Object.keys(err.response.data)
        // 에러가 여러 개일 경우, 맨 앞의 에러 하나만 띄우도록 한다.
        alert(err.response.data[errorKeys[0]])
      }
    },
    async register(context, params) {
      try {
        const response = await authApi.register(
          params.name,
          params.email,
          params.password,
          params.passwordConfirm,
          params.phoneNumber,
          params.nickName
        )
        alert('auth modules: register success')
        return response
      } catch (error: any) {
        const errorKeys = Object.keys(error.response.data)
        // 에러가 여러 개일 경우, 맨 앞의 에러 하나만 띄우도록 한다.
        alert(error.response.data[errorKeys[0]])
      }
    },
    async resetPassword({ commit }, params) {
      try {
        const response = await authApi.resetPassword(params.email)
        if (response.status === 200) {
          commit('setResetPassword')
        }
      } catch (error: any) {
        alert(error.response.data)
      }
    },
    async changePassword({ commit }, params) {
      try {
        const response = await authApi.changePassword(
          params.password,
          params.passwordConfirm
        )
        if (response.status === 200) {
          commit('setChangePassword')
        }
      } catch (error: any) {
        alert(error.response.data)
      }
    },
  },
  getters: {},
}
