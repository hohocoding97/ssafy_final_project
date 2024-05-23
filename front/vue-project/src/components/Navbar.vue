<template>

<nav class="navbar navbar-expand-lg bg-body-tertiary p-0">
  <div class="container-fluid" style="background-color: rgb(195, 70, 64);">
    <RouterLink :to="{name:'home'}" class="site-logomark" style="text-decoration: none;">
    <div class="logo">
    <img src="/src/assets/fin-logo.png" alt="" style=" height: 65px; margin-top: 10px; margin-bottom: 10px;">
    <a class="navbar-brand" id="Logo-name">Takofix</a>
    </div>
    </RouterLink>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse justify-content-end" id="navbarNavAltMarkup">
      <div class="navbar-nav p-3">
        <RouterLink style="margin-right: 10px; margin-top: 5px; text-decoration: none; color: black;">TakoTalk</RouterLink>
        <RouterLink :to="{name:'community'}" style="margin-right: 10px; margin-top: 5px; text-decoration: none; color: black;">Community</RouterLink>
        <RouterLink style="margin-right: 10px; margin-top: 5px; text-decoration: none; color: black;">AI 추천</RouterLink>
        <form class="d-flex" role="search" @submit.prevent="search">
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" v-model="query">
          <button class="btn btn-dark" type="submit" style="margin-right: 10px;">Search</button>
        </form>
        <p></p>
        <a v-if="userStore.userInfo.id" @click="userStore.logout()" class="btn btn-dark" type="button" style="margin-right: 10px;">logout</a>
        <RouterLink v-if="userStore.userInfo.id" :to="{name:'profile' ,params : { userId : userStore.userInfo.id}}"
        class="btn btn-dark" type="button" style="margin-right: 10px;">My</RouterLink>
        <RouterLink v-if="!userStore.userInfo.id" :to="{name:'SignUpView'}" class="btn btn-dark" type="button" style="margin-right: 10px;">signup</RouterLink>
        <RouterLink v-if="!userStore.userInfo.id" :to="{name:'LoginView'}" class="btn btn-dark" type="button" style="margin-right: 10px;">login</RouterLink>
      </div>
    </div>
  </div>
</nav>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter, RouterLink } from 'vue-router'
import { movieCounterStore } from '@/stores/movieCounter'
import { useCounterStore } from '@/stores/userCounter'
import { searchCounterStore } from '@/stores/searchCounter' 

const movieStore = movieCounterStore()
const userStore = useCounterStore()
const searchStore = searchCounterStore()
const router = useRouter()
const imgURL = movieStore.imgURL
const query = ref('')


const search = function(){
  searchStore.search(query.value)
  router.push({name:'search', params: { query: query.value }})
}

</script>

<style>

#Logo-name {
  font-size: x-large;
  font-weight: 700;
  font-family: 'MoveSans-Bold';
}

.navbar {
  position: absolute;
}

.navbar-nav {
  color: rgb(240, 234, 210);
}

@font-face {
    font-family: 'MoveSans-Bold';
    src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/2405-2@1.0/MoveSans-Bold.woff2') format('woff2');
}

@font-face {
    font-family: 'Freesentation-9Black';
    src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/2404@1.0/Freesentation-9Black.woff2') format('woff2');
    font-style: normal;
}

#navbarNavAltMarkup {
  font-family: 'Freesentation-9Black';
}
</style>
