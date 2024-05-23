<template>
  <div v-if="movieStore.detailMovie.actors.length > 0" class="w-75 mx-auto">
    <h1 id="title">출연 배우</h1>
    <div id="mainslider" >
      <splide :options="options">
        <splide-slide v-for="actor in movieStore.detailMovie.actors" :key="actor.id">
          <img type="button" :src="`${imgURL}${actor.profile_path}`" :alt="actor.actor_name" style="width: 99%;">
          <p>{{ actor.actor_name }}</p>
        </splide-slide>
      </splide>
    </div>
  </div>
</template>

<script setup>
  import { movieCounterStore } from '@/stores/movieCounter'
  import { Splide, SplideSlide } from '@splidejs/vue-splide'
  import '@splidejs/splide/dist/css/themes/splide-default.min.css'
 
  const movieStore = movieCounterStore()
  const imgURL = movieStore.imgURL

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