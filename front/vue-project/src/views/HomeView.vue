<template>
  <div class="container_test" style="background-color: rgb(240, 234, 210);">
    <p v-if="userStore.is_login">{{ userStore.userInfo.username }}님 안녕하세요</p>
      <div class="background"/>
      <HomeHeader class="homeheader_inform"/>
      <div style="margin-top: 20px;"></div>
      <PopularCarousel/>
      <LatestCarousel/>
      <AllMovies/>
  </div>
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
.container_test{
  position: absolute;
  display: flex;
  flex-direction: column;
  width: 100%;
}
.background {
  position: absolute;
  background-image: url("/src/assets/background.png"); /* 이미지 URL을 지정합니다. */
  background-size: cover; /* 이미지를 컨테이너에 맞게 확장합니다. */
  background-position: center; /* 이미지를 가운데로 정렬합니다. */
  z-index: 0;
  /* width: 100px; */
  height: 850px; /* 화면 전체 높이로 설정합니다.*/
  width: 100vw; /* 전체 너비로 설정합니다. */
  margin-top: 0px;
}
.homeheader_inform{
  position: relative;
  z-index: 1000;
}
</style>