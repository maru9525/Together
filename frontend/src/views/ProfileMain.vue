<template>
  <div>
    <div class="profile-main__info__top--array">
      <div class="text-2xl font-bold">내 정보</div>
      <div class="text-gray-400">
        <router-link :to="{ name: 'ProfileEdit' }">수정</router-link>
      </div>
    </div>
    <div class="profile-main__info--array">
      <p class="text-gray-500">닉네임</p>
      <p>누클리어 런치 디텍티드</p>
    </div>
    <div class="profile-main__info--array">
      <p class="text-gray-500">이름</p>
      <p>김정은</p>
    </div>
    <div class="profile-main__info--array">
      <p class="text-gray-500">휴대폰 번호</p>
      <p>010-1803-1806</p>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'ProfileMain',
  setup() {
    return {}
  },
})
</script>

<style lang="scss" scoped>
.profile-main__info__top--array {
  @apply flex justify-between items-center;
  margin: 24px 16px 0px 16px;
}

.profile-main__info--array {
  @apply flex justify-between items-center;
  margin: 16px 16px;
}

@media (min-width: 768px) {
  .profile-main__info__top--array {
    margin: 28px 352px 0px;
  }
  .profile-main__info--array {
    margin: 16px 352px 0px;
  }
}
</style>
