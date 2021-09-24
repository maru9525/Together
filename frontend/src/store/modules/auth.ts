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
    },
  },
  actions: {
    login(context: any, { userEmail, password }) {
      try {
        const response = authApi.login(userEmail, password)
        if (response.status === 200) {
          context.commit('setToken', response.data.token)
        }
      } catch (err) {
        console.log(err)
      }
    },
  },
  getters: {},
}
