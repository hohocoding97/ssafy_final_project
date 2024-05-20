<template>
  <div>
    <h1>{{ route.params }}</h1>
    <div v-for="movie in movies">
      <p>{{ movie.title }}</p>
      <img :src="`${imgURL}${movie.poster_url}`" alt="">
    </div>
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue';
  import { useRoute } from 'vue-router';
  import { movieCounterStore } from '@/stores/movieCounter';
  import axios from 'axios';
  const route = useRoute()
  const store = movieCounterStore()
  const movies = ref(null)
  const imgURL = store.imgURL
  onMounted(() => {
    const url = `${store.API_URL}/movies/genre/${route.params.genre_code}/`
    console.log(url)
    axios.get(url)
    .then((res) => {
      console.log(res.data)
      movies.value = res.data
    })
    .catch((err) => console.log(err))
  })
</script>

<style  scoped>

</style>