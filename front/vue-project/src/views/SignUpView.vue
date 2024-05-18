<template>
  <!-- 이미지부터 환영 코멘트까지 -->
  <div class="upper" style="text-align: center;">
    <img src="/src/assets/taco.png" alt="" width = "180px" height = "150px" style="margin-top: 50px;">
    <div class = enter-ment>
      <p>타코야끼를 좋아하는 영화인! 환영해요~!</p>
      <p>즐겁게 영화보며 이야기 해보아요~!</p>
    </div>    
  </div>
  <!-- 회원가입 폼 -->
  <div style="margin-top: 100px;">
  <div style="display: flex; justify-content: center; align-items: center; height: 150px;">
    <div class="card" style="width: 400px; height:300px; min-width: 400px;" >
      <form @submit.prevent="signup">
        <div style="margin-bottom: 10px;">
          <h3 style="text-align: center; margin-top: 30px; margin-bottom: 30px">CREATE ACCOUNT</h3>
          <label for="username" style="margin-left: 20px;">ID : </label>
          <input type="text" v-model.trim="username" id="username" placeholder="ID를 입력하세요." style="margin-left: 120px; width: 200px;">
        </div>
        <div style="margin-bottom: 10px;"> 
          <label for="password1" style="margin-left: 20px;">PASSWORD : </label>
          <input type="password" v-model.trim="password1" id="password1" placeholder="PW를 입력하세요." style="margin-left: 51px; width: 200px;">
        </div>
        <div style="margin-bottom: 10px;">
          <label for="password2" style="margin-left: 20px;">PASSWORD 확인 : </label>
          <input type="password" v-model.trim="password2" id="password2" placeholder="PW를 다시 입력하세요." style="margin-left: 13px; width: 200px;">
        </div>
        <!-- <div>
          <label for="is_ckecked" style="margin-left: 20px;">비밀번호 보이기</label>
          <input type="checkbox" name="is_ckecked" id="is_ckecked" v-model="is_checked">
        </div> -->
        <div style="text-align: center; margin-top: 30px;">
          <input type="submit" value = '회원가입' class="btn btn-dark">
        </div>
      </form>
    </div>
  </div>
</div>
</template>

<script setup>
  import { ref } from 'vue';
  import { useCounterStore } from '@/stores/userCounter'

  const store = useCounterStore()
  const username = ref(null)
  const password1 = ref(null)
  const password2 = ref(null)
  const is_checked = ref(false)
  
  const signup = function() {
    const payload = {
      username: username.value,
      password1: password1.value,
      password2: password2.value
    }
    store.signup(payload)
  }
</script>

<style scoped>

</style>