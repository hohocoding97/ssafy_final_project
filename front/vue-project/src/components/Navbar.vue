<template>
  <header>

    <RouterLink :to="{name:'home'}" class="site-logomark">
      <div class="logo-container" style="text-align: center;">
        <img src="/src/assets/nav-logo.png" alt="Logo" width="90" height="80" style="display: inline-block; vertical-align: middle; margin-left: 10px; margin-top: -3px;">
        <p id="Logo-name" style="display: inline-block; vertical-align: middle; margin-top: -20px;">Takofix</p>
      </div>
    </RouterLink>
    <nav>
      <RouterLink>TakoTalk</RouterLink>
      <RouterLink :to="{name:'community'}">Community</RouterLink>
      <RouterLink >AI 추천</RouterLink>
      <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" style="width: 200px;">
      <a class="contact" href="#">Search</a>
      <a v-if="userStore.is_login === true" @click="userStore.logout()" class="contact">로그아웃</a>
      <RouterLink v-if="userStore.is_login === false" :to="{name:'SignUpView'}" class="contact" >Singup</RouterLink>
      <RouterLink v-if="userStore.is_login === false" :to="{name:'LoginView'}" class="contact">Login</RouterLink>
    </nav>
  </header>
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
  
  <style scoped>
  :root {
    font-family: "Open Sans", sans-serif;
    --bg: #eaf0e9;
    --color: #100f15;
    --color-rgb: 16, 15, 21;
    --primary: #b4ee9d;
    --primary-rgb: 40, 136, 166;
    --primary-hue: 204deg;
    --shadows: 0 0.4vmin 0.6vmin rgba(var(--color-rgb), 0.2),
      0 1.2vmin 1.7vmin rgba(var(--color-rgb), 0.08);
    color: var(--color);
    --work-color: var(--primary);
  }
  h1,
  h2,
  h3,
  h4,
  h5,
  h6 {
    font-family: "Roboto Slab", serif;
  }
  
  main {
    position: absolute;
    top: 0;
    left: 0;
    background: var(--bg);
    height: 100vh;
    width: 100vw;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
  
  header {
    /* z-index: 5; */
    box-sizing: border-box;
    position: fixed;
    width: 100vw;
    height: 8vh;
    min-height: 50px;
    top: 0;
    left: 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: var(--bg);
    padding: 1vh 3.5vw;
    border-bottom: solid rgba(var(--color-rgb), 0.3) 1px;
    box-shadow: 0 0.1vmin 0.4vmin rgba(var(--color-rgb), 0.08);
  }
  
  header a {
    text-decoration: none;
    color: inherit;
  }
  
  .site-logomark {
    font-weight: bold;
    font-size: 140%;
    background: linear-gradient(to right, rgb(225, 255, 201), var(--color));
    background-size: 0 250%;
    background-repeat: no-repeat;
    background-position: left center;
    transition: color 0.12s ease-in-out, background-size 0.18s ease-in-out;
    padding: 0.25em 0.5em;
    height: 90%;
  }
  
  .site-logomark svg {
    height: 100%;
  }
  
  .cls-1 {
    fill: var(--color);
    transition: fill 0.12s ease-in-out;
  }
  
  .site-logomark:hover,
  .site-logomark:focus {
    background-size: 250% 250%;
    outline: none;
  }
  
  .site-logomark:hover .cls-1,
  .site-logomark:focus .cls-1 {
    fill: var(--bg);
  }

  
  header nav {
    width: 70%; /* 네비게이션 바의 너비를 늘립니다. */
    max-width: 900px; /* 최대 너비를 지정하여 너무 커지지 않도록 합니다. */
    display: flex;
    flex-wrap: wrap; /* 요소들이 넘칠 경우 다음 줄로 넘어가도록 설정합니다. */
    justify-content: center; /* 요소들을 가운데 정렬합니다. */
  }
  
  header nav a {
    margin: 0 10px; /* 각 링크 사이의 간격을 조정합니다. */
  }
  
  header nav a:not(.contact)::after {
    content: "";
    position: absolute;
    top: 100%;
    left: -0.5vw;
    height: 2px;
    width: 0;
    background: linear-gradient(to right, rgb(206, 251, 201), var(--primary) 50%);
    transition: width 0.12s ease-in-out;
  }

  header nav input,
header nav button {
  margin: 5px;
}
  
  header nav a:not(.contact):focus {
    outline: none;
  }
  
  header nav a:hover::after,
  header nav a:focus::after {
    width: calc(100% + 1vw);
  }
  
  /* Contact Badge */
  .contact {
  color: white;
  background: linear-gradient(to bottom, transparent 60%, rgb(0, 128, 0)),
    linear-gradient(-60deg, var(--primary) 30%, rgb(179, 235, 133)); /* 여기서 연두색으로 변경 */
  background-size: 250% 250%;
  background-position: center;
  text-decoration: none;
  display: inline-block;
  padding: 0.5em 1em;
  border-radius: 1vmin;
  transform: translate(0, 0) scale(1);
  --shadow-1-height: 0;
  --shadow-1-blur: 0;
  --shadow-2-height: 0;
  --shadow-2-blur: 0;
  box-shadow: 0 var(--shadow-1-height) var(--shadow-1-blur)
      rgba(var(--primary-rgb), 0.2),
    0 var(--shadow-2-height) var(--shadow-2-blur) rgba(var(--color-rgb), 0.06);
  transition: all 0.12s ease-in-out;
  }

  
  .contact:hover,
  .contact:focus {
    outline: none;
    transform: translate(0, -0.5vh) scale(1.1);
    --shadow-1-height: 0.3vmin;
    --shadow-1-blur: 0.8vmin;
    --shadow-2-height: 0.9vmin;
    --shadow-2-blur: 1.2vmin;
  }
  
  @media (orientation: portrait) {
    header {
      top: unset;
      bottom: 0;
      justify-content: center;
      border-bottom: none;
      border-top: solid rgba(var(--color-rgb), 0.3) 1px;
      box-shadow: 0 -0.1vmin 0.4vmin rgba(var(--color-rgb), 0.08);
    }
  
    .site-logomark {
      position: fixed;
      top: 1.5vh;
      left: 50%;
      height: min-content;
      display: flex;
      align-items: center;
      padding: 0.5vh 1vw;
      transform: translate(-50%);
    }
  
    .site-logomark svg {
      display: inline-block;
      height: 5vh;
    }
  
    header nav {
      width: 100vw;
      font-size: calc(0.3em + 2vmin);
      justify-content: space-around;
      box-sizing: border-box;
      padding: 0 1.5vmin;
      max-width: unset;
      min-width: unset;
    }
  }

    #Logo-name {
      font-size: larger;
      font-weight: bolder;
      font-family: 'Franklin Gothic Medium', 'Arial Narrow';
      margin-top: -10px;
    }


  </style>
  
  