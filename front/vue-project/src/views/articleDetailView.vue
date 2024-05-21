<template>
  <!-- 이미지부터 커뮤니티 검색 화면까지 -->
  <div class="upper" style="text-align: center; margin-top: 20px;">
    <img src="/src/assets/taco.png" alt="" width="180px" height="150px" style="margin-top: 50px;">
    <div class="enter-ment">
      <h1>Takofix Community</h1>
    </div>
  </div>

  <!-- 게시글 확인 -->
  <div class="card-container">
    <div class="card" style="width: 800px; margin-top: 20px;">
      <div class="card-body">
        <h4 class="card-title" style="margin-left: 10px;">(제목 작성하는 곳)</h4>
        <div class="owner">
          <h6 class="card-subtitle mb-2 text-body-secondary" style="margin-left: 10px; margin-top: 5px;">작성자 : (작성자 정보 받아오는 곳)</h6>
          <button type="button" class="btn btn-dark" style="width: 80px; height: 30px; display: flex; align-items: center; justify-content: center;">Follow</button>
        </div>
        <div class="card mb-3" style="width: 750px; margin-top: 10px;">
          <div class="card-body">
            <p class="card-text">(게시글 내용 받아오는 곳)</p>
          </div>
        </div>
        <!-- 댓글 기능 구현 -->
        <div class="card reply-card" style="width: 750px;">
          <div class="card-header bg-light">
            <i class="fa fa-comment fa"></i> 댓글
          </div>
          <div class="card-body">
            <ul class="list-group list-group-flush">
              <li class="list-group-item">
                <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
                <button type="button" class="btn btn-dark mt-3" onClick="javascript:addReply();">post reply</button>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
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
</style>
