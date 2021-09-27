<template>
  <div class="container">
    <section class="noti-section">
      <div class="noti-box">
        <p>파티를 만들고,</p>
        <p>다른 사람들과 함께 하세요 🎉</p>
      </div>
    </section>
    <section class="service-section">
      <header class="section-header">
        <h1 class="section-title" :class="{ selected: provider }">
          서비스 선택
        </h1>
        <button
          class="reset-service-btn"
          @click="handleResetProvider"
          v-if="provider"
        >
          다시 선택
        </button>
      </header>
      <div class="service-list">
        <button
          class="service"
          :class="{ selected: provider === '넷플릭스' }"
          v-if="!provider || provider === '넷플릭스'"
          @click="handleSelectProvider('넷플릭스')"
        >
          <div class="logo-wrapper">
            <img src="@/assets/images/netflix.png" alt="넷플릭스" />
          </div>
          <p class="service-name">넷플릭스</p>
        </button>
        <button
          class="service"
          :class="{ selected: provider === '왓챠' }"
          v-if="!provider || provider === '왓챠'"
          @click="handleSelectProvider('왓챠')"
        >
          <div class="logo-wrapper">
            <img src="@/assets/images/watcha.png" alt="왓챠" />
          </div>
          <p class="service-name">왓챠</p>
        </button>
        <button
          class="service"
          :class="{ selected: provider === '웨이브' }"
          v-if="!provider || provider === '웨이브'"
          @click="handleSelectProvider('웨이브')"
        >
          <div class="logo-wrapper">
            <img src="@/assets/images/wavve.png" alt="웨이브" />
          </div>
          <p class="service-name">웨이브</p>
        </button>
      </div>
    </section>
    <section class="party-section">
      <header class="section-header">
        <h1 class="section-title">파티 정보</h1>
      </header>
      <template v-if="provider">
        <form class="grid gap-4">
          <TextInput
            v-for="(field, key) in formData"
            v-model="field.value"
            :key="key"
            :name="key"
            :field="field"
            :formData="formData"
            @update:validate="handleUpdateValidate($event)"
          />
        </form>
      </template>
    </section>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import TextInput from '@/components/Common/TextInput.vue'
import { requiredValidator } from '@/libs/validator'
import { PartyForm, Provider, ValidateData } from '@/libs/interface'

export default defineComponent({
  name: 'PartyCreate',
  components: { TextInput },
  setup() {
    const provider = ref<Provider>('')
    const formData = ref<PartyForm>({
      title: {
        label: '파티 이름',
        type: 'text',
        value: '',
        placeholder: '파티 이름을 입력하세요',
        errors: {},
        validators: [requiredValidator],
      },
      serviceId: {
        label: '계정',
        type: 'text',
        value: '',
        placeholder: '공유할 서비스 계정을 입력하세요',
        errors: {},
        validators: [requiredValidator],
      },
      servicePassword: {
        label: '비밀번호',
        type: 'text',
        value: '',
        placeholder: '공유할 서비스 비밀번호를 입력하세요',
        errors: {},
        validators: [],
      },
      memberCount: {
        label: '모집인원',
        type: 'number',
        value: '',
        placeholder: '모집인원',
        errors: {},
      },
      endDate: {
        label: '파티 종료일',
        type: 'date',
        value: Date(),
        placeholder: '파티 종료일',
        errors: {},
      },
      pricePerDay: {
        label: '하루 이용료',
        type: 'text',
        value: '',
        placeholder: '하루 이용료',
        errors: {},
      },
    })

    const handleUpdateValidate = (data: ValidateData) => {
      console.group(`handleUpdateValidate`)
      console.log(data)
      console.groupEnd()
      const { key, type, status, message } = data
      if (!status && message) {
        formData.value[key].errors[type] = message
      } else {
        delete formData.value[key].errors[type]
      }
    }

    const handleSelectProvider = (p: Provider) => {
      provider.value = p
    }

    const handleResetProvider = () => {
      provider.value = ''
    }

    return {
      provider,
      formData,
      handleSelectProvider,
      handleResetProvider,
      handleUpdateValidate,
    }
  },
})
</script>

<style lang="scss" scoped>
.noti-section {
  @apply py-6 px-4;

  .noti-box {
    @apply w-full py-4 text-center bg-indigo-50 rounded-lg;

    p {
      @apply text-lg font-bold text-indigo-500;
    }
  }
}

.service-section {
  @apply p-4;
  .section-header {
    @apply mb-4 flex items-center justify-between;
    .section-title {
      @apply text-2xl font-bold;

      &.selected {
        @apply text-gray-400;
      }
    }
    .reset-service-btn {
      @apply text-sm text-gray-400;
    }
  }

  .service-list {
    @apply grid;

    .service {
      @apply py-2 flex gap-4 items-center;

      &:hover:not(.selected) {
        @apply bg-gray-100 cursor-pointer;
      }

      &.selected .service-name {
        @apply text-gray-400;
      }

      .logo-wrapper {
        @apply w-8 h-8 overflow-hidden rounded;
      }
      .service-name {
        @apply text-lg text-gray-700 font-medium;
      }
    }
  }
}

.party-section {
  @apply p-4;

  .section-header {
    @apply mb-4;

    .section-title {
      @apply text-2xl font-bold;
    }
  }
}
</style>
