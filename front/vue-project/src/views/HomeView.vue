<template>
<!-- Home 상단 -->
<HomeHeader/>

<PopularCarousel/>

<LatestCarousel/>

<AllMovies/>
</template>


<script setup>
  import AllMovies from '@/components/AllMovies.vue';
  import { movieCounterStore } from '@/stores/movieCounter';
  const movieStore = movieCounterStore()
  const imgURL = movieStore.imgURL
  import PopularCarousel from '@/components/PopularCarousel.vue';
  import LatestCarousel from '@/components/LatestCarousel.vue';
  import HomeHeader from '@/components/HomeHeader.vue';
</script>

<style scoped>

</style>