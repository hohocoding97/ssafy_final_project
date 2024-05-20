<template>
    <!-- 이미지부터 커뮤니티 검색 화면까지 -->
    <div class="upper" style="text-align: center; margin-top: 20px;">
      <img src="/src/assets/taco.png" alt="" width = "180px" height = "150px" style="margin-top: 50px;">
        <div class = enter-ment>
          <h1>Takofix Community</h1>
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" style="width: 400px;">
          <button type="button" class="btn btn-dark" >Search</button>
      </div>    
    </div>

    
    <!-- 게시판 생성 -->
    <table class="table">
    <!-- <tr><td colspan="2"><h2>게시판</h2></td></tr> -->

    <tr class="header" style="margin-top: 30px;">
        <td class="num">번호</td>
        <td class="title">제목</td>
        <td>작성자</td>
        <td>작성날짜</td>
    </tr>
  </table>
<br>
    <table>
    <tr>
        <td><button type="button" class="btn btn-dark">글쓰기</button></td>
    </tr>
  </table>
</template>

<script>
var i, day = 20;
for (i = 10; i > 0; i--) {
    document.write("<tr class='body'>");
    document.write("<td>" + i +"</td>");
    document.write("<td class='title'>제목입니다.</td>"); 
    document.write("<td>작성자</td>"); 
  document.write("<td>24-01-" + day-- + "</td>");
    document.write("</tr>");
}
</script>

<style scoped>
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
</style>