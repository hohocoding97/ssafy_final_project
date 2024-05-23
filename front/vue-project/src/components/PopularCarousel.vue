<template>
<!-- 영화 carousel -->
  <div class="w-100">
    <div id="Title">
      <h1 id="header">인기 영화</h1>
    </div>
    <div id="mainslider" >
      <splide :options="options">
        <splide-slide v-for="movie in movieStore.popularMovies" :key="movie.id" @click="router.push({name:'movieDetail', params:{movieId: movie.code}})">
          <img type="button" :src="`${imgURL}${movie.poster_url}`" :alt="movie.title" style="width: 99%;">
        </splide-slide>
      </splide>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { movieCounterStore } from '@/stores/movieCounter'
import { Splide, SplideSlide } from '@splidejs/vue-splide'
import '@splidejs/splide/dist/css/themes/splide-default.min.css'

const movieStore = movieCounterStore()
const imgURL = movieStore.imgURL
const router = useRouter()

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

<style>
  
@font-face {
  font-family: 'MoveSans-Bold';
  src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/2405-2@1.0/MoveSans-Bold.woff2') format('woff2');
}

@font-face {
    font-family: 'Freesentation-9Black';
    src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/2404@1.0/Freesentation-9Black.woff2') format('woff2');
    font-style: normal;
}


#mainslider {
  margin-left: 1px;
  margin-right: 1px;
}

#header {
  font-size: xx-large;
  font-family:'MoveSans-Bold';
  font-weight: 700;
  margin-left: 30px;
  margin-top: 20px;
  margin-bottom: 20px;
}
</style>
    