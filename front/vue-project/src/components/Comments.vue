<template>
  <div>

  </div>
</template>

<script setup>
  import { articleCounterStore } from '@/stores/articleCounter'
  const articleStore = articleCounterStore()

  const createComment = function(articleId) {
    const payload = { articleId, content:content.value}
    articleStore.createComment(payload)
    getArticle() //코멘트 생성 후 아티클 다시 업데이트하자
  }
</script>



<style scoped>
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