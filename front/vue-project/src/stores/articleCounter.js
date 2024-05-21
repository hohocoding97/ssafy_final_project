import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useCounterStore } from './userCounter'
import { useRouter } from 'vue-router'

export const articleCounterStore = defineStore('articleCounterStore', () => {
  const userStore = useCounterStore()
  const router = useRouter()
  // 게시글 작성 함수
  const writeArticle = function(payload) {
    const {title, content} = payload
    axios({
      method:'POST',
      url:   `${userStore.API_URL}/community/article/` ,
      data : {title, content},
      headers: {Authorization: `Token ${userStore.token}`}
    })
    .then((res) => {
      console.log('게시글 작성 완료')
      router.push({name:'community'})
    })
    .then(err => console.log(err))
  }

  const getArticle = function() {
    axios.get(`${userStore.API_URL}/community/article/`)
    .then(res => {
      console.log(res.data)
    })
    .catch(err => {
      console.log(err)
    })
  }

  return { writeArticle, getArticle,  }
}, {persist:true})
