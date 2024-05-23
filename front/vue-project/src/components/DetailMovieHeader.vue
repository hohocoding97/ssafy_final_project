<template>
  <div class="container">

    <div class="poster ">
        <img  v-bind:src="`${imgURL}${movieStore?.detailMovie?.poster_url}`" alt="movie_poster">
    </div>
    <div class="detail ">
      <h2>{{ movieStore?.detailMovie?.title }}</h2>
      <br>
      <p> 개봉일 : {{ movieStore?.detailMovie?.release_date }}</p>
      <p>{{ movieStore?.detailMovie?.overview }}</p>
      <!-- TMDB 평점 -->
      <div class="flex-wrapper">
        <div class="single-chart" style="margin-top: 10px;">
          <svg viewBox="0 0 36 36" class="circular-chart orange">
            <path class="circle-bg"
              d="M18 2.0845
                a 15.9155 15.9155 0 0 1 0 31.831
                a 15.9155 15.9155 0 0 1 0 -31.831"
            />
            <path class="circle"
              :stroke-dasharray="`${movieStore?.detailMovie?.score * 10}, 100`"
              d="M18 2.0845
                a 15.9155 15.9155 0 0 1 0 31.831
                a 15.9155 15.9155 0 0 1 0 -31.831"
            />
            <text x="18" y="20.35" class="percentage">{{ (movieStore?.detailMovie?.score * 10).toFixed(0) }}%</text>
          </svg>
        </div>
        <!-- 댓글 작성자들이 준 평점 (수정 필요) -->
        <div class="single-chart" style="margin-top: 10px;">
          <svg viewBox="0 0 36 36" class="circular-chart green">
            <path class="circle-bg"
              d="M18 2.0845
                a 15.9155 15.9155 0 0 1 0 31.831
                a 15.9155 15.9155 0 0 1 0 -31.831"
            />
            <path class="circle"
              :stroke-dasharray="`${movieStore?.detailMovie?.average_rating}, 100`"
              d="M18 2.0845
                a 15.9155 15.9155 0 0 1 0 31.831
                a 15.9155 15.9155 0 0 1 0 -31.831"
            />
            <text x="18" y="20.35" class="percentage">{{movieStore?.detailMovie?.average_rating}}%</text>
            
          </svg>
          
        </div>
        <!-- 좋아요 표시 -->
        <p v-if="is_like" 
        @click="likeMovie" type="button" style="font-size: 40px;">❤️</p>
        <p v-else 
        @click="likeMovie" type="button" style="font-size: 40px;">🤍</p>
        
      </div>
    </div>
  </div>

  <hr class="mx-auto" width="96%">
</template>

<script setup>
  import { movieCounterStore } from '@/stores/movieCounter'
  import { useCounterStore } from '@/stores/userCounter'
  import { computed } from 'vue'

  const movieStore = movieCounterStore()
  const userStore = useCounterStore()
  const imgURL = movieStore.imgURL

  const likeMovie = function(){
    if (userStore.is_login) {
      movieStore.likeMovie(movieStore?.detailMovie?.code)
    } else {
      window.alert('로그인이 필요합니다!')
    }
  }
  const is_like = computed(() => userStore.userInfo.like_movies.includes(movieStore?.detailMovie?.code)) //좋아요한 무비면 true


</script>

<style scoped>

.container {
  display: flex;
  justify-content: center;
  
}

.poster {
  margin-top: 30px;
  margin-right: 20px; 
  width: 200px;
  height: 300px;
}

.detail {
  margin-top: 30px;
  margin-left: 50px; 
  min-width: 300px;
}

.flex-wrapper {
  display: flex;
  flex-flow: row nowrap;
}

.single-chart {
  width: 33%;
  justify-content: space-around ;
}

.circular-chart {
  display: block;
  /* margin: 10px auto; */
  max-width: 80%;
  max-height: 50px;
}

.circle-bg {
  fill: none;
  stroke: #eee;
  stroke-width: 3.8;
}

.circle {
  fill: none;
  stroke-width: 2.8;
  stroke-linecap: round;
  animation: progress 1s ease-out forwards;
}

@keyframes progress {
  0% {
    stroke-dasharray: 0 100;
  }
}

.circular-chart.orange .circle {
  stroke: #ff9f00;
}

.circular-chart.green .circle {
  stroke: #4CC790;
}

.circular-chart.blue .circle {
  stroke: #3c9ee5;
}

.percentage {
  fill: #666;
  font-family: sans-serif;
  font-size: 0.5em;
  text-anchor: middle;
}
</style>