import { Content, Genre } from '@/libs/interface'
import axios, { AxiosError, AxiosResponse } from 'axios'
import { Module } from 'vuex'
import { RootState } from '@/store/index'

interface ProfileState {
  data: string
}

const apiAxios = axios.create({
  baseURL: 'http://localhost:3000',
})

export const content: Module<ProfileState, RootState> = {
  namespaced: true,
  state: {
    data: '',
  },
  mutations: {},
  actions: {
    getContent: async (
      context,
      contentId: number | string
    ): Promise<Content | undefined> => {
      try {
        const res = await apiAxios.get(`/contents/${contentId}`)
        return res.data
      } catch (error) {
        if (axios.isAxiosError(error)) {
          // Access to config, request, and response
          throw new Error(`${error.code}: ${error.message}`)
        } else {
          // Just a stock error
          throw new Error('알 수 없는 에러 발생')
        }
      }
    },
    getRecommendContent: async (): Promise<Content[] | undefined> => {
      try {
        const res = await apiAxios.get('/contents')
        return res.data
      } catch (error) {
        if (axios.isAxiosError(error)) {
          // Access to config, request, and response
          throw new Error(`${error.code}: ${error.message}`)
        } else {
          // Just a stock error
          throw new Error('알 수 없는 에러 발생')
        }
      }
    },
    getGenreList: async (): Promise<Genre[]> => {
      try {
        const res: AxiosResponse<Genre[]> = await apiAxios.get('/genres')
        return res.data
      } catch (error: any) {
        throw new Error(error.response)
      }
    },
  },
  getters: {},
}
