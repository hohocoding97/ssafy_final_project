<template>
  <div>
    <!-- <iframe v-for="trailer in movieStrore.detailMovie.trailers"  id="ytplayer" type="text/html"
    width="480px" height="360px"
    :src="videoSrc"
    frameborder="0" allowfullscreen>
</iframe> -->

  </div>
</template>

<script setup>
  import { movieCounterStore } from '@/stores/movieCounter'


  const movieStrore = movieCounterStore()
</script>

<style scoped>

</style>