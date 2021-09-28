<template>
  <div class="container">
    <div class="body">
      <div class="input-container">
        <div class="input-container__info">
          비밀번호를 찾기 위해
          <br />
          본인인증이 필요합니다
        </div>
        <div class="input-container__input-list">
          <TextInput
            v-for="(field, key) in formData"
            v-model="field.value"
            :key="key"
            :name="key"
            :field="field"
            :formData="formData"
            @submit="submit"
            @update:validate="handleUpdateValidate($event)"
          />
        </div>
        <button
          class="input-container__submit-btn"
          :class="{ disabled: !isValidFormData }"
          :disabled="!isValidFormData"
          @click="submit"
        >
          이메일 본인인증
        </button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed } from 'vue'
import TextInput from '@/components/TextInput.vue'
import { emailValidator } from '@/libs/validator'
import { FormDataList, ValidateData } from '@/libs/interface'

export default defineComponent({
  name: 'PasswordReset',
  components: {
    TextInput,
  },
  setup() {
    const isValidFormData = computed(() => {
      const keys = Object.keys(formData.value)
      return keys.every((key) => {
        const errors = Object.keys(formData.value[key].errors)
        return formData.value[key].value !== '' && !errors.length
      })
    })

    const formData = ref<FormDataList>({
      email: {
        label: '이메일',
        type: 'email',
        value: '',
        placeholder: '복구할 이메일을 입력하세요.',
        validator: emailValidator,
        errors: {},
      },
    })

    const handleUpdateValidate = (data: ValidateData) => {
      const { key, type, status, message } = data
      // message와 같이 undefined로 올 수도 있는 경우, 체크를 잘 해주어야 함
      if (!status && message) {
        formData.value[key].errors[type] = message
      } else {
        delete formData.value[key].errors[type]
      }
    }

    const submit = async () => {
      if (isValidFormData.value) {
        console.log('true')
      }
    }

    return {
      formData,
      isValidFormData,
      handleUpdateValidate,
      submit,
    }
  },
})
</script>

<style lang="scss" scoped>
.body {
  @apply flex flex-col justify-center items-center w-full h-screen -mt-20 -mb-20;

  .input-container {
    @apply grid gap-2 px-8 w-full sm:w-96;

    &__input-list {
      @apply w-full;
    }
    &__info {
      @apply w-full text-indigo-900 bg-indigo-50 px-4 py-4 mb-8 font-bold text-base text-center;
    }
    &__submit-btn {
      @apply w-full rounded-lg py-3 text-xs text-white font-bold bg-indigo-900 text-center;

      &.disabled {
        @apply opacity-50;
      }
    }
  }
}
</style>
