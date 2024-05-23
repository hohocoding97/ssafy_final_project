import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useCounterStore } from './userCounter'
import { movieCounterStore } from './movieCounter'
import { useRouter } from 'vue-router'

export const articleCounterStore = defineStore('articleCounterStore', () => {
  const userStore = useCounterStore()
  const router = useRouter()
  const movieStore = movieCounterStore()
  const article = ref({})
  const articles = ref([])

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
    axios({
      method: 'GET',
      url:`${userStore.API_URL}/community/article/`,
    
    })
    .then(res => {
      console.log(res.data)
      articles.value = res.data
    })
    .catch(err => {
      console.log(err)
    })
  }

  const getArticleDetail = function(articleId) {
    axios.get(`${movieStore.API_URL}/community/article/${articleId}`)
    .then((res) => {
      console.log(res.data)
      article.value = res.data
    })
    .catch(err => console.log(err))
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
      console.log(res.data)
      console.log('게시글 수정되었음')
      router.push({name:'articleDetail', params:{articleId:articleId}})
    })
    .catch(err => console.log(err))
  }

  //게시글 삭제하기
  const deleteArticle = function(articleId){
    axios({
      method: 'DELETE',
      url : `${userStore.API_URL}/community/article/${articleId}/ud/`,
      headers: {Authorization: `Token ${userStore.token}`},
    })
      .then((res) => {
        console.log('게시글 삭제됨')
      })
      .catch(err => console.log(err))
  }

  const createComment = function(payload) {
    const { articleId, content } = payload
    axios({
      method: 'POST',
      url: `${userStore.API_URL}/community/comment/${articleId}/create/`,
      data : { content },
      headers: {Authorization: `Token ${userStore.token}`},
    })
      .then(res => {
        console.log('댓글 생성 성공', res.data)
        getArticleDetail()
      })
      .catch(err => console.log(err))
  }

  return { writeArticle, getArticle, editArticle, deleteArticle, createComment, getArticleDetail,
     article, articles }
}, {persist:true})
