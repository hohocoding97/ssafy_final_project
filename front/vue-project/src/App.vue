<template>
  <Navbar/>
  <div class="container_app">
    <RouterView />
    <div style="height: 200px;"></div>
    <Footer/>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { RouterView } from 'vue-router'
import { movieCounterStore } from './stores/movieCounter';
import Navbar from '@/components/Navbar.vue';
import Footer from '@/components/Footer.vue';

const movieStore = movieCounterStore()

onMounted(() => movieStore.fetch_movies()) //App 컴포넌트 마운트될때 데이터 다 가져오기

</script>

<style scoped>
.container_app{

  /* display:flex; */
  /* justify-content: center; */
  height: 150%;

  background-color: rgb(240, 234, 210);
}
</style>
