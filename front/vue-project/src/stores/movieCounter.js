import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const movieCounterStore = defineStore('movieCounterStore', () => {
  const API_URL='http://127.0.0.1:8000'

  const imgURL = 'https://image.tmdb.org/t/p/w200'
  const movies = ref([]) // 홈에서 사용될 영화 데이터
  const fetch_movies = function(){
    axios.get(`${API_URL}/movies/`)
    .then(res => {
      console.log(res.data)
      movies.value = res.data
    })
    .catch(err => console.log(err))
  }
  return { API_URL,imgURL,movies,fetch_movies }
}, {persist:true})
