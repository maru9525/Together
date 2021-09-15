<template>
  <div>
    <p class="profile-party__text--array text-2xl font-bold">내 파티</p>
    <div class="profile-party__box" id="profile_party__box--size">
      <div class="profile-party__box__text--array">
        <p class="font-semibold">넷플릭스 프리미엄</p>
        <img
          src="@/assets/images/Netflix.png"
          class="profile-party__box__image--size"
          alt="넷플릭스"
        />
      </div>
      <div class="profile-party__box__text--array2">
        <p>21.12.25까지 (109일)</p>
        <p class="font-bold">10,900원</p>
      </div>
      <details @click="contentShown">
        <summary></summary>
        <hr />
        <p class="profile-party__box__text--array3 font-semibold">계정 정보</p>
        <div class="profile-party__box__text--array4">
          <p>아이디</p>
          <p>northKing@NK.com</p>
        </div>
        <div class="profile-party__box__text--array4">
          <p>비밀번호</p>
          <input type="password" value="12335" style="text-align: right" />
        </div>
        <p class="profile-party__box__text--array3 font-semibold">
          파티장 정보
        </p>
        <div class="profile-party__box__text--array4">
          <p>이름</p>
          <p>김일성</p>
        </div>
        <div class="profile-party__box__text--array4">
          <p>휴대폰 번호</p>
          <p>011-247-1001</p>
        </div>
      </details>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'

export default defineComponent({
  name: 'ProfileParty',
  setup() {
    const isContentShown = ref<boolean>(false)
    const open = () => (isContentShown.value = true)

    // const contentShown = () => {
    //   // if (isContentShown === 'false')
    //   const sizeChange = document.getElementById('profile_party__box--size')
    //   sizeChange.style.height = '376px'
    // }

    return {
      isContentShown,
      open,
      // contentShown,
    }
  },
})
</script>

<style lang="scss" scoped>
.profile-party__text--array {
  margin: 24px 0px 16px 16px;
}

.profile-party__box {
  margin: 0px 16px 8px 16px;
  padding: 16px 16px;
  border: 1px red solid;
  border-radius: 6px;
}

details summary {
  cursor: pointer;
}

.profile-party__box__image--size {
  width: 50px;
  height: 50px;
}

.profile-party__box__text--array {
  @apply flex justify-between;
  margin-bottom: 32px;
}

.profile-party__box__text--array2 {
  @apply flex justify-between;
  margin-bottom: 16px;
}

.profile-party__box__text--array3 {
  margin-top: 16px;
}

.profile-party__box__text--array4 {
  @apply flex justify-between;
  margin: 8px 0px;
}
</style>
