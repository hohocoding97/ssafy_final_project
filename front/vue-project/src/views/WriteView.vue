<template>
  <!-- 이미지부터 커뮤니티 검색 화면까지 -->
  <div class="upper" style="text-align: center; margin-top: 20px;">
    <img src="/src/assets/taco.png" alt="" width="180px" height="150px" style="margin-top: 50px;">
    <div class="enter-ment">
      <h1>Takofix Community</h1>
    </div>
  </div>

  <!-- 게시글 작성 -->
  <body>
    <form>
      <table>
        <tr><td class="header">Title</td></tr>
        <tr><td><input type="text" placeholder="제목을 입력하세요" name="title"></td></tr>
        <tr><td class="header">Content</td></tr>
        <tr><td><textarea placeholder="내용을 입력하세요" name="detail"></textarea></td></tr>
        <div id="bottom" style="margin-top: 10px;">
          <div class="input-group">
            <input type="file" class="form-control" id="inputGroupFile04" aria-describedby="inputGroupFileAddon04" aria-label="Upload">
            <button class="btn btn-outline-secondary" type="button" id="inputGroupFileAddon04">Button</button>
          </div>
          <!-- 등록, 수정 삭제 -->
            <input type="submit" value="등록" class="btn btn-dark" onclick="alert('작성 완료!')">
            <input type="submit" value="수정" class="btn btn-dark" onclick="alert('수정 완료!')">
            <input type="submit" value="삭제" class="btn btn-dark" onclick="alert('삭제 완료!')">
          </div>
      </table>
    </form>
  </body>
</template>

<script setup>
</script>

<style scoped>
#bottom {
  display: flex;
  align-items: center;
}

#bottom > * {
  margin-right: 10px; /* 요소 사이의 간격을 조정합니다. */
}

#bottom > :last-child {
  margin-right: 0; /* 마지막 요소의 오른쪽 여백을 제거합니다. */
}

table {
  margin: auto;
}

textarea {
  width: 600px;
  height: 400px;
  border-radius: 5px;
  padding-left: 10px;
  padding-top: 10px;
  resize: none;
}

.header {
  height: 30px;
}

.upper input {
  margin-top: 10px;
}

</style>
