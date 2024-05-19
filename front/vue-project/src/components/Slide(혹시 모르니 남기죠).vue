<template>
    <div class="slider">
      <div class="slide-track">
        <!-- 각각의 영화 포스터를 슬라이드로 표시 -->
        <div v-for="movie in movieStore.movies" class="slide">
          <div class="card" style="width: 9rem">
            <img :src="`${imgURL}${movie.poster_url}`" 
                 :alt="movie.title" 
                 class="card-img-top"
                 @click="movieDetail(movie.code)"
                 type="button"
            >
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
    import { movieCounterStore } from '@/stores/movieCounter';
    const movieStore = movieCounterStore();
    const imgURL = movieStore.imgURL;
  
    const movieDetail = (code) => {
      // 영화 상세 정보 표시 로직
    };
  </script>
  
  <style scoped>
    .slider {
      background: white;
      box-shadow: 0 10px 20px -5px rgba(0, 0, 0, .125);
      height: 250px;
      margin: auto;
      overflow: hidden;
      position: relative;
      width: 960px;
    }
  
    @mixin white-gradient {
      background: linear-gradient(to right, rgba(255,255,255,1) 0%, rgba(255,255,255,0) 100%);
    }
  
    .slider::before,
    .slider::after {
      content: "";
      height: 100px;
      position: absolute;
      width: 200px;
      z-index: 2;
    }
  
    .slider::after {
      right: 0;
      top: 0;
      transform: rotateZ(180deg);
    }
  
    .slider::before {
      left: 0;
      top: 0;
    }
  
    .slide-track {
      animation: scroll 40s linear infinite;
      display: flex;
    }
  
    .slide {
      height: 100px;
      width: 250px;
      margin-right: 10px; /* 슬라이드 사이의 간격 */
    }
  
    @keyframes scroll {
      0% { transform: translateX(0); }
      100% { transform: translateX(calc(-250px * 14)) } /* 슬라이드 폭 * 총 슬라이드 수 */
    }
  </style>
  