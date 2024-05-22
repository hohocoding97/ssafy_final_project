<template>
  <h1>프로필 페이지임</h1>
  <p>{{ userStore.profileInfo.username }}님의 페이지</p>
  <p>{{ userStore.profileInfo}}</p>
  <img :src="`${userStore.API_URL}${userStore.profileInfo.image_url}`" alt="">
</template>

<script setup>
  import { onMounted } from 'vue';
  import { useRoute } from 'vue-router'
  import { useCounterStore } from '@/stores/userCounter'
  
  const route = useRoute()
  const userStore = useCounterStore()

  onMounted(() => {
    userStore.getProfileInfo(route.params.userId)
  })
</script>

<style scoped>

</style>