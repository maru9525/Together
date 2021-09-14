<template>
  <section v-if="loading">로딩 중</section>
  <template v-else>
    <section class="banner-section">배너</section>
    <section class="info-section">
      <header class="section-header">
        <span class="title">{{ content.title }}</span>
        <div class="sim-rate">{{ content.simRate }}%</div>
      </header>
      <ul class="provider-list">
        <li
          class="provider-item"
          v-for="provider in content.providers"
          :key="provider"
        >
          {{ provider }}
        </li>
      </ul>
      <div class="details">
        <div>{{ content.firstAirYear }}</div>
        <div>{{ content.rated }}</div>
        <div>시즌 {{ content.seasons }}개</div>
      </div>
      <div class="overview">
        {{ content.overview }}
      </div>
      <div class="rating-wrapper">
        <button class="rating-btn" v-for="i in 5" :key="i">
          <span class="material-icons star">star</span>
        </button>
      </div>
    </section>
    <section class="review-section">
      <header class="section-header">{{ content.title }} 리뷰</header>
      <ul class="review-list">
        <li
          class="review-item"
          v-for="review in displayedReviews"
          :key="review.id.videoId"
        >
          <a
            :href="`https://youtube.com/watch?v=${review.id.videoId}`"
            target="_blank"
            rel="noopener noreferrer"
          >
            <div class="review">
              <div class="thumbnail-wrapper">
                <img
                  :src="review.snippet.thumbnails.high.url"
                  :alt="`${review.snippet.title} 썸네일`"
                />
              </div>
              <span class="title" v-html="review.snippet.title" />
            </div>
          </a>
        </li>
      </ul>
    </section>
    <section class="party-section">
      <header class="section-header">파티에 참여하세요!</header>
      <ul class="party-list">
        <li class="party-item" v-for="party in parties" :key="party.id">
          <div class="party">
            <div class="infos">
              <div class="text">
                <h3>{{ party.provider }} 프리미엄</h3>
                <p>{{ party.title }}</p>
              </div>
              <div class="logo-wrapper">로고</div>
            </div>
            <div class="members">
              <span class="material-icons" v-for="i in 5" :key="i">star</span>
            </div>
            <div class="details">
              <div>
                <p class="date">
                  {{ party.endDate }}까지 ({{ party.restDays }}일)
                </p>
              </div>
              <div class="price-wrapper">
                <p class="original-price">
                  {{ toCurrency(party.originalPricePerDay * party.restDays) }}
                </p>
                <p class="price">
                  {{ toCurrency(party.pricePerDay * party.restDays) }}
                </p>
              </div>
            </div>
          </div>
        </li>
      </ul>
      <div class="flex">
        <router-link class="more-link" :to="{ name: 'ContentList' }">
          <span class="label">더보기</span>
          <span class="material-icons">chevron_right</span>
        </router-link>
      </div>
    </section>
    <section class="community-section">
      <header class="section-header">
        <h1>커뮤니티</h1>
        <p>댓글 12</p>
      </header>
      <ul class="comment-list">
        <li class="comment-item" v-for="comment in comments" :key="comment.id">
          <div class="left">
            <img class="profile-img" :src="comment.user.profileImg" />
            <div class="rating">{{ comment.rating }}</div>
          </div>
          <div class="right">
            <div class="upper">
              <span>{{ comment.user.nickName }}</span>
              <span>2시간 전</span>
            </div>
            <div class="comment">종이로 집을 지으면 전부 타버릴거야!</div>
            <button class="btn-like">
              <span class="material-icons text-gray-400">favorite</span>
              <span class="like-count">{{ comment.like }}</span>
            </button>
          </div>
        </li>
      </ul>
    </section>
  </template>
  <div class="py-40"></div>
</template>

<script lang="ts">
import axios from 'axios'
import { computed, defineComponent, onMounted, ref } from 'vue'

interface ContentDetail {
  id: number
  title: string
  posterPath: string
  simRate: number
  providers: string[]
  firstAirYear: number
  rated: string
  seasons: number
  overview: string
}

interface Youtube {
  id: {
    kind: string
    videoId: string
  }
  snippet: {
    title: string
    thumbnails: {
      medium?: {
        url: string
      }
      high?: {
        url: string
      }
    }
  }
}

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

interface Comment {
  id: number
  user: {
    nickName: string
    profileImg: string
  }
  comment: string
  like: number
  rating: number
}

const YOUTUBE_BASEURL = 'https://www.googleapis.com/youtube/v3/search'
const YOUTUBE_KEY = 'AIzaSyA3BjU4BpGVhBFlvHsJHsTNRuLePCbaU1Q'

export default defineComponent({
  props: {
    contentId: {
      type: [String, Number],
    },
  },
  setup(props) {
    const loading = ref<boolean>(true)
    const content = ref<ContentDetail>()
    const youtubeReviews = ref<Youtube[]>()
    const parties = ref<Party[]>()
    const comments = ref<Comment[]>()

    const displayedReviews = computed(() => {
      // 화면 사이즈에 따라 end index가 달라진다.
      return youtubeReviews.value?.slice(0, 3)
    })

    const toCurrency = (price: number): string => {
      return `${String(price).replace(/\B(?=(\d{3})+(?!\d))/g, ',')}원`
    }

    onMounted(async () => {
      console.log('asdf')
      try {
        const res = await axios.get(
          `http://localhost:3000/contents/${props.contentId}`
        )
        console.log(res)
        content.value = res.data
      } catch (error) {
        console.log(error)
        // 에러가 발생하는 경우 목록 페이지로 이동
      }

      try {
        const res = await axios.get(`http://localhost:3000/parties`)
        parties.value = res.data
      } catch (error) {
        console.log(error)
      }

      try {
        const res = await axios.get(`http://localhost:3000/comments`)
        comments.value = res.data
      } catch (error) {
        console.log(error)
      }

      try {
        const res = await axios.get(YOUTUBE_BASEURL, {
          params: {
            key: YOUTUBE_KEY,
            part: 'snippet',
            q: `${content.value?.title} 리뷰`,
            maxResults: 20,
            type: 'video',
            regionCode: 'KR',
          },
        })
        youtubeReviews.value = res.data.items
      } catch (error) {
        console.log(error)
      }
      loading.value = false
    })
    return {
      loading,
      content,
      displayedReviews,
      parties,
      comments,
      toCurrency,
    }
  },
})
</script>

<style lang="scss" scoped>
.banner-section {
  @apply h-44 bg-purple-100;
}

.info-section {
  @apply p-4 grid gap-4;

  .section-header {
    @apply flex justify-between items-center;

    .title {
      @apply text-2xl font-bold;
    }

    .sim-rate {
      @apply text-xs text-yellow-400 bg-gray-900 rounded-md py-0.5 px-2;
    }
  }

  .provider-list {
    @apply flex gap-2;
  }

  .details {
    @apply flex gap-2 text-sm;
  }

  .overview {
    word-break: keep-all;
    @apply text-sm;
  }

  .rating-wrapper {
    @apply p-2 border border-gray-200 rounded mr-auto flex gap-1;

    .rating-btn {
      @apply flex;

      .star {
        @apply text-gray-200;
      }
    }
  }
}

.review-section {
  @apply py-6 px-4;

  .section-header {
    @apply text-2xl font-bold mb-4;
  }

  .review-list {
    @apply grid gap-2;

    .review-item {
      .review {
        @apply grid grid-cols-2 gap-2;
        .thumbnail-wrapper {
          padding-top: 55.5%;
          @apply relative overflow-hidden;

          img {
            transform: translateY(-50%);
            @apply absolute top-1/2 left-0 w-full object-center;
          }
        }
        .title {
          -webkit-line-clamp: 2;
          -webkit-box-orient: vertical;
          display: -webkit-box;
          @apply text-sm max-h-10 overflow-hidden overflow-ellipsis text-left;
        }
      }
    }
  }
}

.party-section {
  @apply py-6 px-4;

  .section-header {
    @apply text-2xl font-bold mb-4;
  }

  .party-list {
    @apply grid gap-2 mb-1;

    .party {
      @apply grid gap-4 p-4 border rounded-md border-gray-100;

      .infos {
        @apply flex justify-between;

        .text {
          h3 {
            @apply font-bold mb-1;
          }
          p {
            @apply text-xs;
          }
        }
      }

      .members {
        @apply flex gap-2;

        .material-icons {
          font-size: 2rem;
        }
      }

      .details {
        @apply flex justify-between;

        .date {
          @apply text-xs;
        }

        .price-wrapper {
          @apply text-right;

          .original-price {
            @apply text-red-600 text-sm font-bold line-through;
          }

          .price {
            @apply font-bold text-gray-700;
          }
        }
      }
    }
  }

  .more-link {
    @apply flex items-center mx-auto;

    .label {
      @apply text-sm font-medium text-gray-500;
    }

    .material-icons {
      font-size: 1rem;
    }
  }
}

.community-section {
  @apply py-6 px-4;

  .section-header {
    @apply flex items-center justify-between mb-4;

    h1 {
      @apply text-2xl font-bold;
    }

    p {
      @apply text-sm font-medium text-gray-400;
    }
  }

  .comment-list {
    @apply grid gap-2;

    .comment-item {
      @apply flex gap-2 p-2;

      .left {
        @apply flex flex-col gap-1;

        .profile-img {
          @apply w-8 h-8 rounded-md;
        }

        .rating {
          @apply text-center bg-gray-900 rounded-md text-xs text-yellow-400;
        }
      }

      .right {
        .upper {
          @apply mb-1 flex gap-2 text-xs text-gray-400;
        }

        .comment {
          @apply text-sm mb-2;
        }
        .btn-like {
          @apply flex items-center gap-2;

          .material-icons {
            font-size: 1rem;
            @apply text-gray-400;
          }

          .like-count {
            @apply text-xs text-gray-400;
          }
        }
      }
    }
  }
}
</style>
