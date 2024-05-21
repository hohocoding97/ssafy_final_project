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
  const articles = ref([])

  const getArticle = function() {
    axios.get(`${userStore.API_URL}/community/article/`)
    .then(res => {
      console.log(res.data)
      articles.value = res.data
    })
    .catch(err => {
      console.log(err)
    })
  }

  //게시글 수정하기
  const editArticle = function(payload) {
    const { title, content, articleId } = payload
    axios({
      method: 'PUT',
      url : `${userStore.API_URL}/community/article/${articleId}/ud/`,
      data : {title, content},
      headers: {Authorization: `Token ${userStore.token}`}
    })
    .then(res => {
      console.log('게시글 수정되었음')
      router.push({name:'articleDetail', params:{articleId:articleId}})
    })
    .catch(err => console.log(err))
  }

  //게시글 삭제하기
  const deleteArticle = function(){
    axios({
      method: 'DELETE',
      url : `${userStore.API_URL}/community/article/${articleId}/ud/`,
      headers: {Authorization: `Token ${userStore.token}`}
    })
    then(res => {
      console.log('게시글 삭제됨')
      router.push({name:'community'})
    })
    .catch(err => console.log(err))
  }

  return { writeArticle, getArticle, editArticle, deleteArticle, articles }
}, {persist:true})
