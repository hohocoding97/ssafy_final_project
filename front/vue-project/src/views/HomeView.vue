<template>
<!-- Home 상단 -->
<HomeHeader/>

<div id="Title">
  <h1>최신 개봉작</h1>
</div>
<Carousel/>

<div id="Title">
  <h1>oo님을 위한 추천영화</h1>
</div>
<Carousel/>
<!-- <AllMovies/> -->
</template>


<script setup>
  import AllMovies from '@/components/AllMovies.vue';
  import { movieCounterStore } from '@/stores/movieCounter';
  const movieStore = movieCounterStore()
  const imgURL = movieStore.imgURL
  import Carousel from '@/components/Carousel.vue';
  import HomeHeader from '@/components/HomeHeader.vue';
</script>

<style scoped>

#Title {
  font-size: large;
  font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  font-weight: 900;
  margin-left: 30px;
  margin-top: 20px;
  margin-bottom: 20px;
}
</style>