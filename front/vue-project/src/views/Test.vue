<template>
  <div class="container">
    <!-- 이미지부터 커뮤니티 검색 화면까지 -->
    <div class="upper" style="text-align: center; margin-top: 20px;">
      <Cat class="mx-auto my-5"/>
      <div class="enter-ment">
        <h1>Takofix Community</h1>
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" style="width: 400px;">
        <button type="button" class="btn btn-dark">Search</button>
      </div>
    </div>

    <!-- 게시판 생성 -->
    <div style="height: 50px;"></div>
    <table class="table">
      <tr class="header" style="margin-top: 30px;">
        <td class="num">번호</td>
        <td class="title">제목</td>
        <td>작성자</td>
        <td>작성일</td>
      </tr>
      <tr v-for="article in articleStore.articles" :key="article.id">
        <td class="num">{{ article.id }}</td>
        <td class="title">
          <RouterLink :to="{name:'articleDetail', params:{articleId:article.id}}" class="link">{{ article.title }}</RouterLink>
        </td>
        <td>{{ article.username }}</td>
        <td>{{ article.created_at.split('T')[0] }}</td>
      </tr>
    </table>
    <hr>
    <div class="button">
      <RouterLink :to="{name:'write'}" type="button" class="btn btn-dark" style="width: 80px;">글쓰기</RouterLink>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { useRouter, RouterLink } from 'vue-router';
import { onMounted } from 'vue'
import { articleCounterStore } from '@/stores/articleCounter'
import Cat from '@/components/Cat.vue'

const articleStore = articleCounterStore()
const router = useRouter()

onMounted(() => {
  articleStore.getArticle()
})
</script>

<style scoped>
.container {
  width: 1000px;
  margin: 0 auto;
}
.upper {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.upper input,
.upper button {
  display: inline-block;
}
.upper input {
  margin-top: 10px;
}
.enter-ment {
  text-align: center;
  margin-top: 20px;
}
table {
  margin: auto;
  width: 700px;
  border-radius: 5px;
  border-collapse: collapse;
  border-top: none;
}
.header {
  background-color: rgb(218, 231, 255);
  text-align: center;
}
.table td,
.table th {
  border-bottom: 1px lightgray solid;
  height: 30px;
  font-size: 14px;
}
.num {
  width: 50px;
}
.title {
  width: 500px;
}
.button {
  text-align: right;
  margin-top: 20px;
}

/* Add this CSS to remove the white box around the title */
.link {
  text-decoration: none;
  color: inherit;
}
.link:focus,
.link:hover {
  outline: none;
}
</style>
