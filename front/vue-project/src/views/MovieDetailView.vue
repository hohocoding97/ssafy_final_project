<template>
  <div>
    <h1>디테일</h1>
    <p>{{ movie }}</p>
  </div>
</template>

<script setup>
  import { onMounted, ref } from 'vue';
  import { useRoute } from 'vue-router';
  import { movieCounterStore } from '@/stores/movieCounter';
  import axios from 'axios';
  
  const movie = ref(null)
  const movieStore = movieCounterStore()
  const route = useRoute()
  onMounted(()=>{
    axios.get(`${movieStore.API_URL}/movies/${route.params.movieId}/`)
    .then((res)=>{
      movie.value = res.data
    })
    .catch((err) => console.log(err))
  })

</script>

<style scoped>

</style>