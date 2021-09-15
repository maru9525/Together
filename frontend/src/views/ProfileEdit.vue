<template>
  <p class="profile-edit__info__top--array text-2xl font-bold">내 정보</p>
  <div class="profile-edit__box__form">
    <p class="profile-edit__box__form__text--array1 text-xs text-gray-400">
      닉네임
    </p>
    <input
      class="profile-edit__box__form__text--array2 text-sm"
      value="누클리어 런치 디텍티드"
    />
  </div>
  <div class="profile-edit__box__form">
    <p class="profile-edit__box__form__text--array1 text-xs text-gray-400">
      이름
    </p>
    <input
      class="profile-edit__box__form__text--array2 text-sm"
      value="김정은"
    />
  </div>
  <div class="profile-edit__box__form">
    <p class="profile-edit__box__form__text--array1 text-xs text-gray-400">
      휴대폰 번호
    </p>
    <input
      class="profile-edit__box__form__text--array2 text-sm"
      value="010-1717-1602"
    />
  </div>
  <p class="profile-edit__cert__text--array text-sm text-gray-700">
    휴대폰 번호를 변경하려면 새로운 번호 인증을 해야 합니다.
  </p>
  <button class="profile-edit__cert__box__form text-sm">
    <p>휴대폰 본인인증</p>
  </button>
  <div class="profile-edit__button__box--array">
    <router-link
      :to="{ name: 'ProfileMain' }"
      class="profile-edit__checkbox--form"
      >확인</router-link
    >
    <router-link
      :to="{ name: 'ProfileChangePassword' }"
      class="profile-edit__changepw--array"
      >비밀번호 변경</router-link
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
.profile-edit__info__top--array {
  margin: 24px 16px 16px 16px;
}

.profile-edit__box__form {
  @apply flex flex-col justify-center items-start;
  margin: 0px 16px 8px 16px;
  height: 60px;
  border: 1px solid lightgray;
  border-radius: 6px;
}

.profile-edit__box__form__text--array1 {
  margin: 8px 0px 0px 16px;
}

.profile-edit__box__form__text--array2 {
  margin: 0px 0px 8px 16px;
}

.profile-edit__cert__text--array {
  margin: 0px 16px 8px 16px;
}

.profile-edit__cert__box__form {
  @apply flex justify-center items-center;
  margin-left: 16px;
  width: 126px;
  height: 36px;
  border: 1px solid;
  border-radius: 999px;
  color: white;
  background-color: #312e81;
}

.profile-edit__button__box--array {
  @apply flex flex-col justify-center items-center;
}

.profile-edit__checkbox--form {
  @apply flex justify-center items-center;
  margin: 40px auto 8px;
  width: 382px;
  height: 56px;
  border: 1px solid;
  border-radius: 12px;
  color: white;
  background-color: #312e81;
}

.profile-edit__changepw--array {
  margin: 0px auto;
}
</style>
