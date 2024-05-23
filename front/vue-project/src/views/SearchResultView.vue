<template>
  <div v-if="searchStore.movieSearchResults || searchStore.actorSearchResults || searchStore.directorSearchResults">
    
    <!-- 영화 검색 결과 -->
    <h3>"{{ route.params.query }}" <strong>영화</strong> 검색결과입니다.</h3>
    <div v-if="searchStore.movieSearchResults.length > 0" class="container" >
        <div 
          v-for="movie in searchStore.movieSearchResults" style="width: 200px;">
          <img :src="`${imgURL}${movie.poster_url}`" 
          :alt="movie.title" 
          style="width: 80px;"
          class="w-100"
          @click="moveDetail(movie.code)"
          type="button"
          >
        </div>
    </div>
    <div v-else>

    </div>
      <hr>
    <!-- 배우 검색 결과 -->
    <h3>"{{ route.params.query }}" <strong>배우</strong> 검색결과입니다.</h3>
    <div v-if="searchStore.actorSearchResults.length > 0" class="container">
      <div v-for="actor in searchStore.actorSearchResults" style="width: 200px;">
        <img :src="`${imgURL}${actor.profile_path}`" 
        style="width: 80px;"
        class="w-100"
        type="button"
        >
        <p>{{ actor.actor_name }}</p>
      </div>
    </div>
    <div v-else>

    </div>
    <hr>

    <!-- 감독 검색 결과는 사진 저장 안한 이슈로 뒤로 미루자 -->
    <!-- <h3>"{{ route.params.query }}" <strong>감독</strong> 검색결과입니다.</h3>
    <div v-if="searchStore.directorSearchResults.length > 0"  class="container">
      <div v-for="director in searchStore.directorSearchResults">
        <img :src="`${imgURL}${director.profile_path}`" 
        style="width: 80px;"
        class="w-100"
        type="button"
        >
        <p>{{ director.director_name }}</p>
      </div>
    </div>
    <div v-else>

    </div> -->
  </div>
  <div v-else>
    
  </div>
</template>

<script setup>
  import { onBeforeMount } from 'vue'
  import { useRoute, useRouter } from 'vue-router';
  import { searchCounterStore } from '@/stores/searchCounter'
  import { movieCounterStore } from '@/stores/movieCounter'

  const searchStore = searchCounterStore()
  const movieStore = movieCounterStore()
  const route = useRoute()
  const router = useRouter()
  const imgURL = 'https://image.tmdb.org/t/p/w200'
  onBeforeMount(() => {
    searchStore.search(route.params.query)
  })
  const moveDetail = function(movieId) {
    router.push({name:'movieDetail', params:{movieId:movieId}})
  }


</script>

<style scoped>
.container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  grid-auto-rows: minmax(100px, auto);
  gap: 10px;
}
h3 {
  text-align: center;
}
</style>