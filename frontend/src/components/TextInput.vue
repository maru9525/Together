<template>
  <div class="grid gap-1">
    <div class="input-container">
      <input
        autocomplete="off"
        :type="field.type"
        :value="modelValue"
        :class="{ active: labelActive }"
        @blur="handleBlur"
        @focus="handleFocus"
        @input="handleInput"
        @keydown.enter="$emit('submit')"
      />
      <label
        class="input-container__placeholder"
        :class="{ active: labelActive }"
      >
        <p v-if="labelActive">{{ field.label }}</p>
        <p v-else>{{ field.placeholder }}</p>
      </label>
    </div>
  </div>
</template>

<script lang="ts">
import { computed, defineComponent, ref, watch } from 'vue'

export default defineComponent({
  name: 'TextInput',
  props: {
    field: {
      type: Object,
    },
    modelValue: {
      type: String,
    },
    validator: {
      type: String,
    },
    name: {
      type: String,
    },
  },
  emits: ['update:modelValue'],
  setup(props, { emit }) {
    const modelValue = computed(() => props.modelValue)
    const labelActive = ref<boolean>(Boolean(props.modelValue))

    // const validate = () => {
    //   return
    // }

    const handleBlur = () => {
      labelActive.value = props.modelValue ? true : false
    }

    const handleFocus = () => {
      labelActive.value = true
    }

    // any의 사용에 대한 확신이 없음. 수정 필요
    const handleInput = (event: any) => {
      emit('update:modelValue', event.target.value)
    }

    watch(modelValue, (value) => {
      labelActive.value = Boolean(value)
    })

    return {
      labelActive,
      handleBlur,
      handleFocus,
      handleInput,
    }
  },
})
</script>

<style lang="scss" scoped>
.input-container {
  @apply relative w-full;

  input {
    @apply relative text-sm outline-none px-4 py-3 z-10 rounded-md bg-transparent border border-gray-300 w-full py-2;

    &.active {
      @apply border-indigo-900;
    }
  }
  &__placeholder {
    @apply absolute top-3 left-3 text-sm text-gray-300 transition-all;
    transform: translate(0);

    &.active {
      @apply bg-white rounded-md text-xs text-indigo-900 p-1 z-10;
      transform: translate(0, -100%);
    }
  }
}
</style>
