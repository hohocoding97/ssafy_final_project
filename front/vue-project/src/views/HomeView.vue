<template>
<p v-if="userStore.is_login">{{ userStore.userInfo.username }}님 안녕하세요</p>
<HomeHeader/>
<PopularCarousel/>

<LatestCarousel/>

<AllMovies/>
</template>


<script setup>
  import AllMovies from '@/components/AllMovies.vue';
  import { movieCounterStore } from '@/stores/movieCounter';
  import { useCounterStore } from '@/stores/userCounter';
  const movieStore = movieCounterStore()
  const userStore = useCounterStore()
  const imgURL = movieStore.imgURL
  import PopularCarousel from '@/components/PopularCarousel.vue';
  import LatestCarousel from '@/components/LatestCarousel.vue';
  import HomeHeader from '@/components/HomeHeader.vue';
</script>

<style scoped>

</style>