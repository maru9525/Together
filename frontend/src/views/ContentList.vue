<template>
  <main class="container">
    <section class="banner-section">배너</section>
    <section class="filter-section">
      <ul class="filter-list">
        <li class="filter-item">넷</li>
        <li class="filter-item">웨</li>
        <li class="filter-item">왓</li>
        <li class="filter-item">네</li>
      </ul>
    </section>
    <section class="contents-section">
      <header class="section-header">추천 컨텐츠</header>
      <ul class="contents-list">
        <li class="contents-item" v-for="content in contents" :key="content.id">
          <router-link
            :to="{ name: 'ContentDetail', params: { contentId: content.id } }"
          >
            <div class="poster-wrapper">
              <img
                :src="content.posterPath"
                :alt="`${content.title}의 포스터`"
              />
            </div>
          </router-link>
        </li>
      </ul>
    </section>
    <div class="py-40"></div>
  </main>
</template>
<script lang="ts">
import { defineComponent, onMounted, ref } from 'vue'
import axios from 'axios'

interface Content {
  id: number
  title: string
  posterPath: string
}

export default defineComponent({
  name: 'ContentList',
  setup() {
    const contents = ref<Content[]>()
    onMounted(async () => {
      const res = await axios.get('http://localhost:3000/contents')
      contents.value = res.data
    })
    return {
      contents,
    }
  },
})
</script>
<style lang="scss" scoped>
.banner-section {
  @apply h-44 bg-gray-200;
}
.filter-section {
  @apply py-6 px-4;

  .filter-list {
    @apply flex gap-6;

    .filter-item {
      @apply w-8 h-8 bg-pink-300;
    }
  }
}

.contents-section {
  @apply p-4;

  .section-header {
    @apply text-2xl font-bold mb-4;
  }

  .contents-list {
    @apply grid grid-cols-3 gap-2 sm:grid-cols-4;

    .poster-wrapper {
      padding-top: 142.1686747%;
      @apply relative flex overflow-hidden rounded-md;

      img {
        @apply absolute inset-0 w-full;
      }
    }
  }
}
</style>
