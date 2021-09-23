<template>
  <section class="banner-section"></section>
  <div class="container">
    <section class="party-section">
      <header class="section-header">파티에 참여하세요!</header>
      <ul class="party-list">
        <PartyListItem
          v-for="party in parties"
          :key="party.id"
          :party="party"
        />
      </ul>
    </section>
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from 'vue'
import PartyListItem from '@/components/PartyListItem.vue'
import axios from 'axios'

interface Party {
  id: number
  provider: string
  title: string
  logoUrl: string
  member: {
    totalCount: number
    joinCount: number
  }
  endDate: string
  restDays: number
  pricePerDay: number
}

export default defineComponent({
  name: 'PartyList',
  components: { PartyListItem },
  setup() {
    const loading = ref(true)
    const parties = ref<Party[]>([])

    onMounted(async () => {
      try {
        const res = await axios.get('http://localhost:3000/parties')
        parties.value = res.data
      } catch (error) {
        console.log(error)
      }
    })
    return { loading, parties }
  },
})
</script>

<style lang="scss" scoped>
.banner-section {
  @apply h-44 bg-blue-500;
}

.party-section {
  @apply py-6 px-4;

  .section-header {
    @apply text-2xl font-bold mb-4;
  }

  .party-list {
    @apply grid gap-4 md:grid-cols-2 xl:grid-cols-3;
  }
}
</style>
