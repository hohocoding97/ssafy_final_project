<template>
    <div>
      <h1>다른 영화들</h1>
    </div>
    <div class="container" style="padding: 0px; margin: auto;">
        <div v-for="movie in movieStore.allMovies">
          <img :src="`${imgURL}${movie.poster_url}`" 
          :alt="movie.title" 
          style="width: 80px;"
          class="w-100"
          @click="moveDetail(movie.code)"
          type="button"
          >
        </div>
    </div>
    
    
</template>

<script setup>
  import { onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  import { movieCounterStore } from '@/stores/movieCounter';
  const movieStore = movieCounterStore()
  const router = useRouter()
  const imgURL = movieStore.imgURL

  const moveDetail = function(movieId) {
    router.push({name:'movieDetail', params:{movieId:movieId}})
  }
  
  onMounted(() => {
    movieStore.fetch_movies()
  })
  
</script>

<style scoped>
.container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  grid-auto-rows: minmax(100px, auto);
  gap: 10px;
}

</style>