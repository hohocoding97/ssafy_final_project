import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useCounterStore } from './userCounter'
import axios from 'axios'

export const movieCounterStore = defineStore('movieCounterStore', () => {
  const API_URL='http://127.0.0.1:8000'
  const imgURL = 'https://image.tmdb.org/t/p/w200'

  const allMovies = ref(null)     // 홈에서 사용될 영화 데이터
  const popularMovies = ref(null) // 인기 영화 데이터
  const latestMovies = ref(null)  // 최신 영화 데이터
  const randomMovies = ref(null)  // 랜덤 영화 데이터
  const detailMovie = ref(null)         // 디테일 페이지 영화 데이터

  const fetch_movies = function(){
    axios.get(`${API_URL}/movies/`)
    .then(res => allMovies.value = res.data)
    .catch(err => console.log('모든 영화 가져올때 에러 발생함',err))
    axios.get(`${API_URL}/movies/popular/`)
    .then(res => popularMovies.value = res.data)
    .catch(err => console.log('인기 영화 가져올때 에러 발생함', err))
    axios.get(`${API_URL}/movies/latest/`)
    .then(res => latestMovies.value = res.data)
    .catch(err => console.log(err))
  }

  const getRandomMovies = function() {
    axios.get(`${API_URL}/movies/random/`)
    .then(res => { 
      console.log(res.data)
      randomMovies.value = res.data
    })
    .catch(err => console.log('랜덤영화가져오는데 문제가 발생함'))
  }

  const getDetailMovie = function(movieId) {
    axios.get(`${API_URL}/movies/${movieId}/`)
    .then((res)=>detailMovie.value = res.data)
    .catch((err) => console.log('영화디테일 가져오다가 문제 발생했음'))
  }
  
  // 영화 좋아요
  const likeMovie = function(movieId){
    axios({
      method:'POST',
      url: `${API_URL}/movies/${movieId}/like/`,
      headers: { Authorization: `Token ${useCounterStore().token}`}
    })
      .then(res => {
        console.log(res.data)
        useCounterStore().getUserInfo() // 유저정보 업데이트하기
      })
      .catch(err => console.log(err))
  }
  return { API_URL,imgURL,allMovies, popularMovies, latestMovies, randomMovies, detailMovie,
    fetch_movies, getRandomMovies, getDetailMovie, likeMovie,
   }
}, {persist:true})
