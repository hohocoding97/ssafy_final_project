<template>
  <Navbar/>

  <!-- <RouterLink :to="{name:'SignUpView'}">회원가입</RouterLink> -->
  <RouterView />

  <div style="height: 200px;"><!-- 그냥 밑에 Footter에 가리지 말라고 해둠 --></div>
  
  <Footer />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Navbar from '@/components/Navbar.vue';
import Footer from '@/components/Footer.vue';

</script>

<style scoped>

</style>
