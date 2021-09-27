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
            <img src="@/assets/images/Netflix.png" alt="넷플릭스" />
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
            <img src="@/assets/images/Watcha.png" alt="왓챠" />
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
            <img src="@/assets/images/Wavve.jpg" alt="웨이브" />
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
            v-for="(field, key) in partyForm"
            v-model="field.value"
            :key="key"
            :name="key"
            :field="field"
          />
        </form>
      </template>
    </section>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import TextInput from '@/components/TextInput.vue'
import { FormDataList, Provider, ValidateData } from '@/libs/interface'

export default defineComponent({
  name: 'PartyCreate',
  components: { TextInput },
  setup() {
    const provider = ref<Provider>('')
    const partyForm = ref<FormDataList>({
      title: {
        label: '제목',
        type: 'text',
        value: '',
        placeholder: '제목을 입력하세요',
        errors: {},
      },
      serviceId: {
        label: '계정',
        type: 'text',
        value: '',
        placeholder: '넷플릭스 계정',
        errors: {},
      },
      servicePassword: {
        label: '비밀번호',
        type: 'text',
        value: '',
        placeholder: '넷플릭스 비밀번호',
        errors: {},
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
        type: 'text',
        value: '',
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
      const { key, type, status, message } = data
      if (!status && message) {
        partyForm.value[key].errors[type] = message
      } else {
        delete partyForm.value[key].errors[type]
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
      partyForm,
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
