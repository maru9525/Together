<template>
  <div class="grid gap-1">
    <div class="input-container">
      <input
        autocomplete="off"
        id="inputText"
        :type="field.type"
        :value="modelValue"
        :class="{ active: isFocused }"
        @blur="handleBlur"
        @focus="handleFocus"
        @input="handleInput"
        @keydown.enter="$emit('submit')"
      />
      <label
        id="inputLabel"
        class="input-container__placeholder"
        :class="{ active: isFocused }"
      >
        <p v-if="isFocused">{{ field.label }}</p>
        <p v-else>{{ field.placeholder }}</p>
      </label>
    </div>
  </div>
</template>

<script lang="ts">
import { computed, defineComponent, onMounted, ref, watch } from 'vue'

export default defineComponent({
  name: 'TextInput',
  props: {
    field: {
      type: Object,
    },
    formData: {
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
  setup(props, { emit }) {
    const modelValue = computed(() => props.modelValue)
    const isFocused = ref<boolean>(Boolean(props.modelValue))

    // const validate = () => {
    //   return
    // }

    const handleBlur = () => {
      isFocused.value = props.modelValue ? true : false
      console.log(Boolean(props.modelValue))
    }

    const handleFocus = () => {
      console.log(Boolean(props.modelValue))
      isFocused.value = true
    }

    // any의 사용에 대한 확신이 없음. 수정 필요
    const handleInput = (event: any) => {
      // emit('update:modelValue', event.target.value)
      return
    }

    watch(modelValue, (value) => {
      console.log(value, '워치중')
      // isFocused.value = Boolean(value)
    })

    onMounted(() => {
      console.log(props.modelValue, '모델')
    })

    return {
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
    @apply relative text-sm outline-none px-4 py-3 rounded-md bg-transparent border border-gray-300 w-full py-2;

    &.active {
      @apply border-indigo-900;
    }
  }
  &__placeholder {
    @apply absolute top-3 left-3 text-sm text-gray-300 transition-all;
    transform: translate(0);

    &.active {
      transform: translate(0, -170%);
    }
  }
}
</style>
