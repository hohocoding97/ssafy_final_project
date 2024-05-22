<template>
  <div class="container">
  <!-- 이미지부터 커뮤니티 검색 화면까지 -->
  <div class="upper" style="text-align: center; margin-top: 20px;">
    <Yum class="my-3"/>
    <div class="enter-ment">
    <h1>Takofix Community</h1>
    </div>
  </div>

  <!-- 게시글 확인 -->
  <div class="card-container">
    <div class="card" style="width: 800px; margin-top: 20px;">
      <div class="card-body">
        <input type="text" v-model="title" style="margin: 0 10px ;">
        <div class="d-flex" style="justify-content: space-between;">
          <div class="owner">
            <h6 class="card-subtitle mb-2 text-body-secondary" style="margin-left: 10px; margin-top: 5px;">작성자 : {{username}}</h6>
          </div>
        </div>

        <textarea  v-model="content"></textarea>
        
          <input @click="editArticle" type="button" value="등록" class="btn btn-dark">
 
      </div>
    </div>
  </div>
  </div>
</template>

<script setup>
  import axios from 'axios'
  import { ref, onMounted } from 'vue'
  import { useRoute } from 'vue-router'
  import { articleCounterStore } from '@/stores/articleCounter'
  import { movieCounterStore } from '@/stores/movieCounter'
  import { useCounterStore } from '@/stores/userCounter'
  import Yum from '@/components/Yum.vue'


  const userStore = useCounterStore()
  const movieStore = movieCounterStore()
  const articleStore = articleCounterStore()  
  const title = ref('')
  const content = ref('')
  const route = useRoute()
  const username = ref('')
  const articleId = ref('')
  onMounted(() => {
    axios.get(`${movieStore.API_URL}/community/article/${route.params.articleId}`)
    .then((res) => {
      console.log(res.data)
      title.value = res.data.title
      content.value = res.data.content
      username.value = res.data.username
      articleId.value = res.data.id
    })
    .catch(err => console.log(err))
  })

  const editArticle = function(){
    const payload = {title: title.value, content: content.value, articleId: articleId.value}
    articleStore.editArticle(payload)
  }

</script>

<style scoped>
.owner {
  display: flex;
  align-items: center; /* 수직 중앙 정렬 */
  gap: 10px; /* 요소 간 간격 */
}

.card-container {
  display: flex;
  justify-content: center; /* 수평 중앙 정렬 */
}

.card {
  margin: 0 auto; /* 카드의 수평 중앙 정렬 */
  min-height: 300px; /* 최소 높이 설정 (필요에 따라 조정 가능) */
}

.card-body {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.reply-card {
  margin-top: 20px !important; /* 항상 30px의 여백을 위에 추가 */
}

textarea {
  width: 100%;
  height: 400px;
  border-radius: 5px;
  padding-left: 10px;
  padding-top: 10px;
  margin: auto;
  resize: vertical;

}


</style>
