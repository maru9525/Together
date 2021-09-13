import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import AuthLayout from '@/layouts/ContentsLayout.vue'
import ContentsLayout from '@/layouts/ContentsLayout.vue'
import PartyLayout from '@/layouts/ContentsLayout.vue'
import ProfileLayout from '@/layouts/ContentsLayout.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'ContentsLayout',
    component: ContentsLayout,
    // children: [
    //   {
    //     path: '/',
    //     name: 'ContentsList',
    //     component: ContentsList
    //   }
    // ]
  },
  {
    path: '/party',
    name: 'PartyLayout',
    component: PartyLayout,
  },
  {
    path: '/auth',
    name: 'AuthLayout',
    component: AuthLayout,
  },
  {
    path: '/profile',
    name: 'ProfileLayout',
    component: ProfileLayout,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
