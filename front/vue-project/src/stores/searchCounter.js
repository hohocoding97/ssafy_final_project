import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const searchCounterStore = defineStore('searchCounterStore', () => {
  const API_URL='http://127.0.0.1:8000'

  const movieSearchResults = ref([])
  const actorSearchResults = ref([])
  const directorSearchResults = ref([])

  const search = function(query) {
    axios.get(`${API_URL}/movies/search/${query}/movie/`)
    .then((res) => movieSearchResults.value = res.data)
    .catch((err) => console.log('영화 검색결과 가져오는 중 오류 발생함'))
    
    axios.get(`${API_URL}/movies/search/${query}/actor/`)
    .then((res) => actorSearchResults.value = res.data)
    .catch((err) => console.log('배우 검색결과 가져오는 중 오류 발생함'))

    axios.get(`${API_URL}/movies/search/${query}/director/`)
    .then((res) => directorSearchResults.value = res.data)
    .catch((err) => console.log('감독 검색결과 가져오는 중 오류 발생함'))

  }
  return { movieSearchResults, actorSearchResults, directorSearchResults,
    search,
  }
}, {persist: true})
