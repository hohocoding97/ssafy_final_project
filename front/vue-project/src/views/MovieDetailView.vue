<template>
  <DetailMovieHeader/>
  <Actors/>
</template>

<script setup>
  import { onMounted, ref } from 'vue'
  import { useRoute } from 'vue-router'
  import { movieCounterStore } from '@/stores/movieCounter'
  import axios from 'axios'
  import Actors from '@/components/Actors.vue'
  import DetailMovieHeader from '@/components/DetailMovieHeader.vue'

  const movieStore = movieCounterStore()
  const route = useRoute()
  const imgURL = movieStore.imgURL

  onMounted(()=>{
    movieStore.getDetailMovie(route.params.movieId)
  })

</script>

<style scoped>

</style>
