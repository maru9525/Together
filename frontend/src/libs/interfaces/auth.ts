export interface Token {
  accessToken: string
  refreshToken: string
}

export type InputUser = {
  pk: number
  username?: string
  nickname?: string
  phone_number?: string
  email?: string
  favorite_genres?: {
    id: number
    name: string
    k_name: string
  }[]
}

export type OutputUser = {
  pk: number
  username?: string
  nickname?: string
  phoneNumber?: string
  email?: string
  favoriteGenres?: {
    id: number
    name: string
    kName: string
  }[]
}
