<template>
  <div class="container">
    <!-- 이미지부터 커뮤니티 검색 화면까지 -->
    <div class="upper" style="text-align: center; margin-top: 20px;">
      <Drawing class="my-3"/>
      <div class="enter-ment">
      <h1 id="header">Takofix Community</h1>
      </div>
    </div>

  <!-- 게시글 확인 -->
  <div class="card-container">
    <div class="card" style="width: 800px; margin-top: 20px;">
      <div class="card-body">
        <h4 class="card-title" style="margin-left: 10px;">{{articleStore.article.title}}</h4>
        <div class="d-flex" style="justify-content: space-between;">
          <div class="owner">
            <h6 class="card-subtitle mb-2 text-body-secondary" style="margin-left: 10px; margin-top: 5px;">작성자 : {{articleStore.article.username}}</h6>
            <button type="button" class="btn btn-dark" style="width: 80px; height: 30px; display: flex; align-items: center; justify-content: center;">Follow</button>
          </div>
          <!-- 삭제와 수정버튼 있는 곳(작성자만 수정 삭제가능하게하기) -->
          <div v-if="userStore.userInfo.id === articleStore.article.user" class="d-felx" style="margin-right: 10px;">
            <button type="button" class="btn btn-secondary" @click="deleteArticle(articleStore.article.id)"   style="margin-right: 2px;">삭제</button>
            <button type="button" class="btn btn-secondary" @click="router.push({name:'editArticle', params:{articleId:articleStore.article.id}})">수정</button>
          </div>
        </div>
        <div class="card mb-3" style="width: 100%; margin-top: 10px;">
          <div class="card-body">
            <p class="card-text">{{articleStore.article.content}}</p>
          </div>
        </div>
        <!-- 댓글 기능 구현 -->
        <div class="card reply-card" style="width: 100%;">
          <div class="card-header bg-light">
            <i class="fa fa-comment fa"></i> 댓글
          </div>
          <div class="card-body">
            <ul class="list-group list-group-flush">
              <li v-for="comment in articleStore.article.comment_set" style="margin-left: 20px;">
              <div style="display: flex;  justify-content: space-between;">
                <div>{{ comment.username }} - {{ comment.content }}</div>
                <div>작성일 : {{ comment.created_at.split('T')[0] }}</div>
              </div>
              </li>
              <li class="list-group-item" style="inline-block">
                <textarea class="form-control" v-model="content" rows="3"></textarea>
                <button type="button"  class="btn btn-dark mt-3" @click="createComment(articleStore.article.id)">댓글 작성</button>
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
  import { ref, onMounted, computed, onBeforeMount, watch } from 'vue'
  import { useRoute, useRouter } from 'vue-router'
  import { articleCounterStore } from '@/stores/articleCounter'
  import { movieCounterStore } from '@/stores/movieCounter'
  import { useCounterStore } from '@/stores/userCounter'
  import Drawing from '@/components/Drawing.vue'

  const userStore = useCounterStore()
  const movieStore = movieCounterStore()
  const articleStore = articleCounterStore()  
  const route = useRoute()
  const router = useRouter()
  const content = ref('')


  onBeforeMount(() => {
    articleStore.getArticleDetail(route.params.articleId)
  })
  

  const deleteArticle = function(articleId) {
    articleStore.deleteArticle(articleId)
    router.push({name:'community'})
  }
  const createComment = function(articleId) {
    if (userStore.userInfo.id){
      const payload = { articleId: articleStore.article.id, content:content.value}
      articleStore.createComment(payload)
      // articleStore.getArticleDetail(route.params.articleId)
      content.value = ''
    } else {
      window.alert('로그인이 필요합니다')
    }
  }
</script>

<style scoped>

@font-face {
    font-family: 'MoveSans-Bold';
    src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/2405-2@1.0/MoveSans-Bold.woff2') format('woff2');
}

#header {

}
.owner {
  display: flex;
  align-items: center; /* 수직 중앙 정렬 */
  gap: 10px; /* 요소 간 간격 */
}

.card-container {
  min-width: 450px;
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
