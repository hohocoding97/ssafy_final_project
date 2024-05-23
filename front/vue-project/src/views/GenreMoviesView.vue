<template>
  <div>
    <h1 class="comment mx-auto my-4" id="search">{{ movieStore.genre[route.params.genre_code] }} 검색 결과입니다.</h1>
    
    <div v-if="movieStore.genreMovies" id="mainslider">
      <Splide :options="options">
        <SplideSlide v-for="movie in movieStore.genreMovies" :key="movie.id" @click="router.push({ name: 'movieDetail', params: { movieId: movie.code } })">
          <img :src="`${imgURL}${movie.poster_url}`" type="button" :alt="movie.title" style="width: 99%;">
        </SplideSlide>
      </Splide>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeMount } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { movieCounterStore } from '@/stores/movieCounter';
import { Splide, SplideSlide } from '@splidejs/vue-splide';
import '@splidejs/splide/dist/css/themes/splide-default.min.css';

const route = useRoute()
const router = useRouter()
const movieStore = movieCounterStore()
const imgURL = movieStore.imgURL

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

const moveDetail = function (movieId) {
  router.push({ name: 'movieDetail', params: { movieId: movieId } })
}

onBeforeMount(() => {
  movieStore.getGenreMovies(route.params.genre_code)
})

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

@font-face {
  font-family: 'MoveSans-Bold';
  src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/2405-2@1.0/MoveSans-Bold.woff2') format('woff2');
}

#search {
  font-family: 'MoveSans-Bold';
  font-size: xx-large;
  font-weight: 700;
}

</style>
