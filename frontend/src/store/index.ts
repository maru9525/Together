import { createStore } from 'vuex'
import { content } from '@/store/modules/content'

export interface RootState {
  data: string
}

export default createStore<RootState>({
  modules: { content },
})
