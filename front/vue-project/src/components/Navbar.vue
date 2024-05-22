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
        <div class="navbar-nav">
          <RouterLink style="margin-right: 10px; margin-top: 5px; text-decoration: none; color: black;">TakoTalk</RouterLink>
          <RouterLink :to="{name:'community'}" style="margin-right: 10px; margin-top: 5px; text-decoration: none; color: black;">Community</RouterLink>
          <RouterLink style="margin-right: 10px; margin-top: 5px; text-decoration: none; color: black;">AI Movie Recommend</RouterLink>
          <form class="d-flex" role="search">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-dark" type="submit" style="margin-right: 10px;">Search</button>
          </form>
          <p></p>
          <a v-if="userStore.is_login === true" @click="userStore.logout()" class="btn btn-dark" type="button" style="margin-right: 10px;">로그아웃</a>
          <RouterLink v-if="userStore.is_login === false" :to="{name:'SignUpView'}" class="btn btn-dark" type="button" style="margin-right: 10px;">Signup</RouterLink>
          <RouterLink v-if="userStore.is_login === false" :to="{name:'LoginView'}" class="btn btn-dark" type="button" style="margin-right: 10px;">Login</RouterLink>
        </div>
      </div>
    </div>
  </nav>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { movieCounterStore } from '@/stores/movieCounter';
  import { useCounterStore } from '@/stores/userCounter'
  import { RouterLink } from 'vue-router';
  
  const movieStore = movieCounterStore();
  const userStore = useCounterStore()
  const imgURL = movieStore.imgURL;
  
  </script>
  
  <style>
  
  #Logo-name {
    font-size:x-large;
    font-weight: bolder;
    font-family: 'Franklin Gothic Medium', 'Arial Narrow';
  }
  
  .navbar {
    position: absolute;
  }

  .navbar-nav {
    color: rgb(240, 234, 210);
  }
  </style>
  
  