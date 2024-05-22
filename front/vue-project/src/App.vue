<template>
  <Navbar/>
  <div class="container_app">
    <!-- <div style="height: 80px;"></div> -->
    <div style="height: 200px;"><!-- 그냥 밑에 Footter에 가리지 말라고 해둠 --></div>
    <RouterView />
  </div>
  <Footer />
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
  display:flex;
  justify-content: center;
  height: 170vh;
  background-color: rgb(240, 234, 210);
}
</style>
