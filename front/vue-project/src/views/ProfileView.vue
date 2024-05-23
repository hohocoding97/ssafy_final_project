<template>

  <h2 style="text-align: center;">{{ userStore.profileInfo.username }}님의 페이지</h2>
  <div v-if="userStore.userInfo.id !== userStore.profileInfo.id">
    <button @click="follow">follow</button>
    <button @click="follow">unfollow</button>
  </div>

  <div class="w-100" >
      <div id="Title">
        <h4>{{ userStore.profileInfo.username }}님이 "좋아요❤️"한 영화</h4>
      </div>
      <hr class=" mx-auto" style="width: 95%;">
      <div id="mainslider" v-if="userStore.like_movies.like_movies.length > 0">
        <splide :options="options">
          <splide-slide v-for="movie in userStore.like_movies.like_movies" :key="movie.id" @click="router.push({name:'movieDetail', params:{movieId: movie.code}})">
            <img type="button" :src="`${imgURL}${movie.poster_url}`" :alt="movie.title" style="width: 99%;">
          </splide-slide>
        </splide>
      </div>
      <div v-else>
        <p class="ms-5">아직 "좋아요❤️"한 영화가 없습니다...</p>
      </div>
    </div>

</template>

<script setup>
  import { onMounted, computed, onBeforeMount } from 'vue';
  import { useRoute, useRouter } from 'vue-router'
  import { useCounterStore } from '@/stores/userCounter'
  import { movieCounterStore } from '@/stores/movieCounter'
  import { Splide, SplideSlide } from '@splidejs/vue-splide'
  import '@splidejs/splide/dist/css/themes/splide-default.min.css'
  
  const route = useRoute()
  const router = useRouter()
  const userStore = useCounterStore()
  const movieStore = movieCounterStore()
  const imgURL = movieStore.imgURL
  
  onBeforeMount(() => {
    userStore.getProfileInfo(route.params.userId)
    userStore.getLikeMovies(route.params.userId)
  })
  const profileImgURL = computed(() => `${userStore.API_URL}${userStore.profileInfo.image_url}`)
  
  const follow = function(){ userStore.follow() }

  // SPLIDE의 옵션 설정
  const options = {
    type: 'loop',
    rewind: true,
    autoplay: true,
    perMove: 1,
    breakpoints: {
      5000: {
        perPage: 6,
      },
      1200: {
        perPage: 5,
      },
      992: {
        perPage: 4,
      },
      768: {
        perPage: 3,
      },
      576: {
        perPage: 2,
      },
      480: {
        perPage: 1,
      },
    },
  };
</script>

<script>
export default {
    name: "MainSlider",
    components: {
      Splide,
      SplideSlide,
    },
  };
</script>
  

  

  
<style scoped>

  #mainslider {
    margin-left: 1px;
    margin-right: 1px;
  }
  
  #Title {
    font-size: large;
    font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
    font-weight: 900;
    margin-left: 30px;
    margin-top: 20px;
    margin-bottom: 20px;
  }
</style>