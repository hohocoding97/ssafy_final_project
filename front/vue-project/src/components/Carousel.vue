<template>
<!-- 영화 carousel -->

  <div id="mainslider">
    <splide :options="options">
      <splide-slide v-for="movie in movieStore.movies" :key="movie.id">
        <img :src="`${imgURL}${movie.poster_url}`" :alt="movie.title">
      </splide-slide>
    </splide>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { movieCounterStore } from '@/stores/movieCounter';
import { Splide, SplideSlide } from '@splidejs/vue-splide';
import '@splidejs/splide/dist/css/themes/splide-default.min.css';

const movieStore = movieCounterStore();
const imgURL = movieStore.imgURL;

// SPLIDE의 옵션 설정
const options = {
  type: 'loop',
  rewind: true,
  perPage: 5,
  autoplay: true,
  perMove: 1,
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

#mainslider {
  margin-left: 50px;
  margin-right: 50px;
}
</style>
  