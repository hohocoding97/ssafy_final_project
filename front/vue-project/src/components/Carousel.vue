<template>
<!-- 영화 carousel -->
<div id="Title">
  <h1>최신 개봉작</h1>
</div>

<main>
    <!-- Carousel 컨테이너 -->
    <div class="carousel">
      <div v-for="movie in movieStore.movies" class="card" style="width: 9rem">
        <img :src="`${imgURL}${movie.poster_url}`" 
          :alt="movie.title" 
          class="card-img-top"
          @click="movieDetail(movie.code)"
          type="button"
          >
      </div>
    </div>
    <!-- 좌우 화살표 -->
 </main>

<!-- <AllMovies/> -->
</template>
    
<script setup>
    import AllMovies from '@/components/AllMovies.vue';
    import { movieCounterStore } from '@/stores/movieCounter';
    const movieStore = movieCounterStore()
    const imgURL = movieStore.imgURL
</script>

<style scoped>
.carousel {
  display: flex;
  overflow-x: auto; /* 가로 스크롤 가능하도록 설정 */
  scroll-snap-type: x mandatory; /* carousel 기능을 위해 필요한 속성 */
}

.card {
  scroll-snap-align: start; /* carousel 기능을 위해 필요한 속성 */
  flex: 0 0 auto; /* carousel에서 요소가 자동으로 크기 조절되지 않도록 설정 */
  width: 9rem;
}
</style>