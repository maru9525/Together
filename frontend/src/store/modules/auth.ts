import * as authApi from '@/api/auth'
import { Module } from 'vuex'
import { RootState } from '@/store/index'

interface authModule {
  token: string
}

export const auth: Module<authModule, RootState> = {
  namespaced: true,
  state: {
    token: '',
  },
  mutations: {
    setToken(state: authModule, token: string): void {
      state.token = token
      console.log('login mutation success')
    },
  },
  actions: {
    async login(context, params) {
      try {
        const response = await authApi.login(params.userEmail, params.password)
        if (response.status === 200) {
          context.commit('setToken', response.data.access_token)
          return response
        }
      } catch (err) {
        alert('아이디 혹은 비밀번호를 확인해주세요.')
      }
    },
    async register(context, params) {
      try {
        const res = await authApi.register(
          params.name,
          params.userEmail,
          params.password,
          params.passwordConfirm,
          params.phoneNumber,
          params.nickName
        )
        return res
      } catch (err) {
        // TODO: 에러 리턴을 조금 더 UX 좋게 바꿔야 함.
        // 현재 에러 리턴하면 보기 좋지 않게 옴. 모듈화를 풀고 then, catch를 사용하는 방법 고려
        alert('이메일 혹은 이름이 중복되었습니다.')
        return err
      }
    },
  },
  getters: {},
}
