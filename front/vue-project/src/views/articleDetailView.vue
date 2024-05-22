<template>
  <div class="container">
    <!-- 이미지부터 커뮤니티 검색 화면까지 -->
    <div class="upper" style="text-align: center; margin-top: 20px;">
      <img src="/src/assets/그림1.png" alt="" width="180px" height="150px" style="margin-top: 50px;">
      <div class="enter-ment">
        <h1>Takofix Community</h1>
      </div>
    </div>

  <!-- 게시글 확인 -->
  <div class="card-container">
    <div class="card" style="width: 800px; margin-top: 20px;">
      <div class="card-body">
        <h4 class="card-title" style="margin-left: 10px;">{{article.title}}</h4>
        <div class="d-flex" style="justify-content: space-between;">
          <div class="owner">
            <h6 class="card-subtitle mb-2 text-body-secondary" style="margin-left: 10px; margin-top: 5px;">작성자 : {{article.username}}</h6>
            <button type="button" class="btn btn-dark" style="width: 80px; height: 30px; display: flex; align-items: center; justify-content: center;">Follow</button>
          </div>
          <!-- 삭제와 수정버튼 있는 곳(작성자만 수정 삭제가능하게하기) -->
          <div v-if="userStore.userInfo.id === article.user" class="d-felx" style="margin-right: 10px;">
            <button type="button" class="btn btn-secondary"  style="margin-right: 2px;">삭제</button>
            <button type="button" class="btn btn-secondary" @click="router.push({name:'editArticle', params:{articleId:article.id}})">수정</button>
          </div>
        </div>
        <div class="card mb-3" style="width: 100%; margin-top: 10px;">
          <div class="card-body">
            <p class="card-text">{{article.content}}</p>
          </div>
        </div>
        <!-- 댓글 기능 구현 -->
        <div class="card reply-card" style="width: 100%;">
          <div class="card-header bg-light">
            <i class="fa fa-comment fa"></i> 댓글
          </div>
          <div class="card-body">
            <ul class="list-group list-group-flush">
              <li class="list-group-item" style="inline-block">
                <textarea class="form-control"  rows="3"></textarea>
                <button type="button" class="btn btn-dark mt-3" @click="">댓글 작성</button>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
  </div>
</template>

<script setup>
  import axios from 'axios'
  import { ref, onMounted } from 'vue'
  import { useRoute, useRouter } from 'vue-router'
  import { articleCounterStore } from '@/stores/articleCounter'
  import { movieCounterStore } from '@/stores/movieCounter'
  import { useCounterStore } from '@/stores/userCounter'
  
  const userStore = useCounterStore()
  const movieStore = movieCounterStore()
  const articleStore = articleCounterStore()  
  const route = useRoute()
  const router = useRouter()
  const article = ref({})
  onMounted(() => {
    axios.get(`${movieStore.API_URL}/community/article/${route.params.articleId}`)
    .then((res) => {
      console.log(res.data)
      article.value = res.data
    })
    .catch(err => console.log(err))
  })

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
  min-height: 200px; /* 최소 높이 설정 (필요에 따라 조정 가능) */
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
  height: 60px;
  padding: 4px 6px;
  border: 1px solid #999;
  border-radius: 4px;
  resize: vertical;
  font-size: 18px;
}
</style>
