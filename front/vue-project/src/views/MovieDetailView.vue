<template>
  <div v-if="movieStore.detailMovie">
    <DetailMovieHeader/>
    <Actors/>
  </div>

</template>

<script setup>
  import { onMounted, ref } from 'vue'
  import { useRoute } from 'vue-router'
  import { movieCounterStore } from '@/stores/movieCounter'
  import Actors from '@/components/Actors.vue'
  import DetailMovieHeader from '@/components/DetailMovieHeader.vue'

  const movieStore = movieCounterStore()
  const route = useRoute()
  const imgURL = movieStore.imgURL

  onMounted(()=>{
    console.log('무비 디테일 마운트함 ')
    console.log(route.params)
    movieStore.getDetailMovie(route.params.movieId)
  })
</script>

<style scoped>

</style>
