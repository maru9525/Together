<template>
  <p class="profile-changepassword__top--array text-2xl font-bold">
    비밀번호 변경
  </p>
  <div class="profile-changepassword__box__form">
    <input
      class="profile-changepassword__box__form__text--array"
      type="password"
      value=""
      placeholder="현재 비밀번호"
    />
  </div>
  <div class="profile-changepassword__box__form">
    <input
      class="profile-changepassword__box__form__text--array"
      type="password"
      value=""
      placeholder="새 비밀번호"
    />
  </div>
  <div class="profile-changepassword__box__form">
    <input
      class="profile-changepassword__box__form__text--array"
      type="password"
      value=""
      placeholder="새 비밀번호 확인"
    />
  </div>
  <div class="profile-changepassword__button__box--array">
    <p class="profile-changepassword__checkbox--form">확인</p>
    <router-link
      :to="{ name: 'ProfileEdit' }"
      class="profile-changepassword__back--array"
      >돌아가기</router-link
    >
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  setup() {
    return {}
  },
})
</script>

<style lang="scss" scoped>
.profile-changepassword__top--array {
  margin: 24px 16px 16px 16px;
}

.profile-changepassword__box__form {
  @apply flex flex-col justify-center items-start;
  margin: 0px 16px 8px 16px;
  height: 60px;
  border: 1px solid lightgray;
  border-radius: 6px;
}

.profile-changepassword__box__form__text--array {
  margin: 18px 0px 18px 16px;
}

.profile-changepassword__button__box--array {
  @apply flex flex-col justify-center items-center;
}

.profile-changepassword__checkbox--form {
  @apply flex justify-center items-center;
  margin: 40px auto 8px;
  width: 382px;
  height: 56px;
  border: 1px solid;
  border-radius: 12px;
  color: white;
  background-color: #312e81;
}

.profile-changepassword__back--array {
  margin: 0px auto;
}
</style>
