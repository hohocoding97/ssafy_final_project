<template>
  <!-- 프로필 이미지부터 00님 페이지 -->
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="wrapper">
          <img src="/src/assets/face.png" alt="face" class="profile-image">
        </div>
      </div>
      <div class="col-md-6">
        <div class="wrapper">
          <h2 class="profile-title">{{ userStore.profileInfo.username }}님의 페이지</h2>
          <div class="d-flex justify-content-center align-items-center">
            <p id="follow" style="margin-right: 20px;">fOLLOWER : {팔로워 수}</p>
            <p id="follow" style="margin-right: 20px;">following : {팔로워 수}</p>
            <button type="button" class="btn btn-dark" id="btn">Follow</button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-if="userStore.userInfo.id !== userStore.profileInfo.id">
    <button @click="follow">follow</button>
    <button @click="follow">unfollow</button>
  </div>
<!-- 좋아요한 영화 모음 -->
  <div class="w-100" >
      <div id="Title">
        <h4 id="fav_mov">{{ userStore.profileInfo.username }}님이 "좋아요❤️"한 영화 모음</h4>
      </div>
      <hr class=" mx-auto" style="width: 95%;">
      <div id="mainslider" v-if="userStore.like_movies.like_movies.length > 0">
        <splide :options="options">
          <splide-slide v-for="movie in userStore.like_movies.like_movies" :key="movie.id" @click="router.push({name:'movieDetail', params:{movieId: movie.code}})">
            <img type="button" :src="`${imgURL}${movie.poster_url}`" :alt="movie.title" style="width: 99%;">
          </splide-slide>
        </splide>
      </div>
      <div v-else id="else">
        <p class="ms-5">아직 "좋아요❤️"한 영화가 없습니다...</p>
      </div>
    </div>

<div>
  <div id="Title">
    <h4 id="written">{{ userStore.profileInfo.username }}님이 작성한 게시글 모음</h4>
  </div>

</div>
</template>

<script setup>
  import { onMounted, computed, onBeforeMount } from 'vue';
  import { useRoute, useRouter } from 'vue-router'
  import { useCounterStore } from '@/stores/userCounter'
  import { movieCounterStore } from '@/stores/movieCounter'
  import { Splide, SplideSlide } from '@splidejs/vue-splide'
  import '@splidejs/splide/dist/css/themes/splide-default.min.css'
  
  const route = useRoute()
  const router = useRouter()
  const userStore = useCounterStore()
  const movieStore = movieCounterStore()
  const imgURL = movieStore.imgURL
  
  onBeforeMount(() => {
    userStore.getProfileInfo(route.params.userId)
    userStore.getLikeMovies(route.params.userId)
  })
  const profileImgURL = computed(() => `${userStore.API_URL}${userStore.profileInfo.image_url}`)
  
  const follow = function(){ userStore.follow() }

  // SPLIDE의 옵션 설정
  const options = {
    type: 'loop',
    rewind: true,
    autoplay: true,
    perMove: 1,
    breakpoints: {
      5000: {
        perPage: 6,
      },
      1200: {
        perPage: 5,
      },
      992: {
        perPage: 4,
      },
      768: {
        perPage: 3,
      },
      576: {
        perPage: 2,
      },
      480: {
        perPage: 1,
      },
    },
  };
</script>

<script>
export default {
    name: "MainSlider",
    components: {
      Splide,
      SplideSlide,
    },
  };
</script>
  

  

  
<style scoped>

@font-face {
    font-family: 'Freesentation-9Black';
    src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/2404@1.0/Freesentation-9Black.woff2') format('woff2');
    font-style: normal;
}

@font-face {
    font-family: 'MoveSans-Bold';
    src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/2405-2@1.0/MoveSans-Bold.woff2') format('woff2');
}
.container {
  /* margin-top: 50px; 페이지 상단 여백 조정 */
}

.wrapper {
  text-align: center; /* 내용 가운데 정렬 */
}

.profile-image {
  border-radius: 50%; /* 원형 모양으로 이미지 변형 */
  width: 200px; /* 이미지 너비 조정 */
  margin-top: 20px;
}

.profile-title {
  margin-top: 50px;
  font-family: 'MoveSans-Bold';
  font-weight: 700;
}

#mainslider {
  margin-left: 1px;
  margin-right: 1px;
}

#Title {
  font-family: 'MoveSans-Bold';
  font-size: larger;
  font-weight: 700;
  margin-left: 30px;
  margin-top: 20px;
  margin-bottom: 20px;
}

#follow {
  font-family: 'MoveSans-Bold';
  font-size: larger;
}

#btn {
  font-family: 'Freesentation-9Black';
}

#fav_mov {
  font-family: 'MoveSans-Bold';
  font-size: larger;
  font-weight: 700;
}

#else {
  font-family: 'MoveSans-Bold';
  font-size: larger;
}

#written {
  font-family: 'MoveSans-Bold';
  font-size: larger;
  font-weight: 700;
}

</style>