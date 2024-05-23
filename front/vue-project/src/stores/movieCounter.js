import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useCounterStore } from './userCounter'
import axios from 'axios'
import { articleCounterStore } from './articleCounter'

export const movieCounterStore = defineStore('movieCounterStore', () => {
  const API_URL='http://127.0.0.1:8000'
  const imgURL = 'https://image.tmdb.org/t/p/w200'

  const allMovies = ref(null)     // 홈에서 사용될 영화 데이터
  const popularMovies = ref(null) // 인기 영화 데이터
  const latestMovies = ref(null)  // 최신 영화 데이터
  const randomMovies = ref(null)  // 랜덤 영화 데이터
  const genreMovies = ref(null)   // 장르별 영화 데이터
  const detailMovie = ref(null)   // 디테일 페이지 영화 데이터
  const genre = {28:'액션', 18:'드라마', 99:'다큐멘터리', 10749:'멜로/로멘스', 16:'애니메이션', 53:'스릴러', 14:'판타지', 27:'공포', 10402:'음악'}

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
    
    articleCounterStore().getArticle()
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


  const getGenreMovies = function(genreCode) {
    const url = `${API_URL}/movies/genre/${genreCode}/`
    axios.get(url)
      .then((res) => {
        console.log('장르별 영화 가져왔음')
        genreMovies.value = res.data;
      })
      .catch((err) => console.log(err))
  }

  return { API_URL,imgURL,allMovies, popularMovies, latestMovies, randomMovies, detailMovie, genreMovies, genre,
    fetch_movies, getRandomMovies, getDetailMovie, likeMovie,getGenreMovies
   }
}, {persist:true})
