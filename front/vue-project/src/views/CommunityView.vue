<template>
  <div v-if="articleStore.articles">

    <div class="container">
      <!-- 이미지부터 커뮤니티 검색 화면까지 -->
      <div class="upper" style="text-align: center;">
        <Cat class="mx-auto my-5"/>
        <div class = enter-ment>
          <h1 id="header">Takofix Community</h1>
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" style="width: 400px;">
          <button type="button" class="btn btn-dark" >Search</button>
        </div>    
      </div>
    </div>
  </div>

    
    <!-- 게시판 생성 -->
  <div class="board">
  <div style="height: 50px;"></div>
  <table class="table">
    <tr class="header" style="margin-top: 30px;">
        <td class="num">번호</td>
        <td class="title">제목</td>
        <td>작성자</td>
        <td>작성일</td>
    </tr>
  <!-- </table> -->
  <!-- <br> -->
  <!-- <table style="text-align: center;"> -->
    <tr v-for="article in articleStore.articles" style="text-align: center;">
        <td class="num">{{ article.id }}</td>
        <td class="title" @click="goDetail(article.id)" type="button">
          {{ article.title }}
        </td>
        <td @click="router.push({name:'profile' ,params:{userId : article.id}})">{{ article.username }}</td>
        <td >{{ article.created_at.split('T')[0] }}</td>
        <hr>
      </tr>
    </table>
    <td><RouterLink :to="{name:'write'}" type="button" class="btn btn-dark" style="width: 80px; margin-left: 730px; margin-top: 20px;">글쓰기</RouterLink></td>
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
  //게시글 데이터 가져오자
  articleStore.getArticle()
  
})

const goDetail =function(articleId){
  router.push({name:'articleDetail' ,params:{articleId:articleId}})
}



// import type { Header, Item } from "vue3-easy-data-table";

// const headers: Header[] = [
//   { text: "글번호", value: "player" },
//   { text: "제목", value: "title"},
//   { text: "작성일", value: "created_at"},
//   { text: "댓글수", value: "position"},
//   { text: "작성자", value: "user"},
// ];

// const items: Item[] = [
//   { player: "Stephen Curry", team: "GSW", number: 30, position: 'G', indicator: {"height": '6-2', "weight": 185}, lastAttended: "Davidson", country: "USA"},
//   { player: "Lebron James", team: "LAL", number: 6, position: 'F', indicator: {"height": '6-9', "weight": 250}, lastAttended: "St. Vincent-St. Mary HS (OH)", country: "USA"},
//   { player: "Kevin Durant", team: "BKN", number: 7, position: 'F', indicator: {"height": '6-10', "weight": 240}, lastAttended: "Texas-Austin", country: "USA"},
//   { player: "Giannis Antetokounmpo", team: "MIL", number: 34, position: 'F', indicator: {"height": '6-11', "weight": 242}, lastAttended: "Filathlitikos", country: "Greece"},
// ];
</script>

<style scoped>

@font-face {
    font-family: 'MoveSans-Bold';
    src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/2405-2@1.0/MoveSans-Bold.woff2') format('woff2');
}



table {
  margin: auto;
  width: 700px;
  border-radius: 5px;
  border-collapse: collapse;
  border-top: none;
}
.header {
  background-color: rgb(255, 240, 218);
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
.body {
  text-align: center;
}
.body .title {
  text-align: left;
}
button {
  width: 100px;
  height: 40px;
  font-size: 15px;
  border: 0;
  border-radius: 5px;
  padding-left: 10px;
}
button:active {
  width: 100px;
  height: 40px;
  font-size: 15px;
  border: 0;
  border-radius: 5px;
  padding-left: 10px;
}
.enter-ment {
  text-align: center;
  margin-top: 20px;
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

  /* table {
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
} */

/* .button {
  text-align: right;
  margin-top: 20px;
} */
</style>