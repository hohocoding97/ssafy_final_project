<template>
  <main>
    <div v-for="movie in movieStore.movies" class="card" style="width: 9rem">
      <img :src="`${imgURL}${movie.poster_url}`" 
        :alt="movie.title" 
        class="card-img-top"
        @click="moveDetail(movie.code)"
        type="button"
        >
    </div>
  </main>
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
    // if (!movieStore.movies.values) { // 처음 데이터 받을 때만 가져오도록
    //   console.log('first')
    //   movieStore.fetch_movies() 
    // } else console.log('not first')
    movieStore.fetch_movies()
  })
</script>

<style scoped>

</style>