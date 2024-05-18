<template>
  <Navbar/>

  <!-- <RouterLink :to="{name:'SignUpView'}">회원가입</RouterLink> -->
  <RouterView />
  
  <Footer />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Navbar from '@/components/Navbar.vue';
import Footer from '@/components/Footer.vue';

</script>

<style scoped>

</style>
