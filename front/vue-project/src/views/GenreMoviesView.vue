<template>
  <div>
    <!-- <h1>{{ route.params }}</h1>
    <h3>{{ route }}</h3> -->
    <h1 class="comment mx-auto my-4">oo장르 검색 결과입니다.</h1>
    <div id="mainslider">
      <Splide :options="options">
        <SplideSlide v-for="movie in movies" :key="movie.id" @click="router.push({name:'movieDetail', params:{movieId: movie.code}})">
          <img :src="`${imgURL}${movie.poster_url}`" :alt="movie.title" style="width: 99%;">
        </SplideSlide>
      </Splide>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { movieCounterStore } from '@/stores/movieCounter';
import axios from 'axios';
import { Splide, SplideSlide } from '@splidejs/vue-splide';
import '@splidejs/splide/dist/css/themes/splide-default.min.css';

const route = useRoute();
const router = useRouter();
const store = movieCounterStore();
const movies = ref([]);
const imgURL = store.imgURL;

// SPLIDE의 옵션 설정
const options = {
  type: 'loop',
  rewind: true,
  autoplay: true,
  perMove: 1,
  breakpoints: {
    5000: { perPage: 6 },
    1200: { perPage: 5 },
    992: { perPage: 4 },
    768: { perPage: 3 },
    576: { perPage: 2 },
    480: { perPage: 1 },
  },
};

const navigateToMovieDetail = (movieId) => {
  router.push({ name: 'movieDetail', params: { movieId } });
};

onMounted(() => {
  const url = `${store.API_URL}/movies/genre/${route.params.genre_code}/`;
  axios.get(url)
    .then((res) => {
      movies.value = res.data;
    })
    .catch((err) => console.log(err));
});
</script>


<script>
export default {
  name : "MainSlider",
  components : {
    Splide,
    SplideSlide
  }
}
</script>
<style scoped>
  #mainslider {
    margin-top: 20px;
    margin-left: 10px;
    margin-right: 10px;
  }
/* 여기에 스타일을 추가하세요 */
</style>
