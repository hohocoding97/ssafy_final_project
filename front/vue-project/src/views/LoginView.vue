<template>
    <!-- 이미지부터 환영 코멘트까지 -->
  <div class="upper" style="text-align: center;">
    <img src="/src/assets/taco.png" alt="" width = "180px" height = "150px" style="margin-top: 50px;">
    <div class = enter-ment>
      <p>타코야끼를 좋아하는 영화인! 환영해요~!</p>
      <p>즐겁게 영화보며 이야기 해보아요~!</p>
    </div>    
  </div>
    <!-- 로그인 폼 -->
  <div style="margin-top: 80px;">
  <div style="display: flex; justify-content: center; align-items: center; height: 200px;">
    <div class="card" style="width: 400px; height:300px; " >
      <form @submit.prevent="signup">
        <div style="margin-bottom: 10px;">
          <h3 style="text-align: center; margin-top: 30px; margin-bottom: 30px">LOGIN</h3>
          <label for="username" style="margin-left: 20px;">ID : </label>
          <input type="text" v-model.trim="username" id="username" placeholder="ID를 입력하세요." style="margin-left: 120px; width: 200px;">
        </div>
        <div style="margin-bottom: 10px;"> 
          <label for="password1" style="margin-left: 20px;">PASSWORD : </label>
          <input type="text" v-model.trim="password1" id="password1" placeholder="PW를 입력하세요." style="margin-left: 50px; width: 200px;">
        </div>
        <div style="text-align: center; margin-top: 30px;">
          <input type="submit" href = "#" value = 'Login' class="btn btn-dark" style="margin-right: 50px;">
          <input type="submit" href = "#" value = 'Sign Up' class="btn btn-dark">
        </div>
      </form>
    </div>
  </div>
  </div>
  </template>
  
  <script setup>
  
  </script>
  
  <style scoped>
  
  </style>