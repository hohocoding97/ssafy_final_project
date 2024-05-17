<template>
    <!-- 프로필 변경 상단 -->
    <div class="Profile d-flex flex-column align-items-center">
        <h3 style="margin-top: 10px;">프로필 변경</h3>
        <div style="width: 200px; height: 200px; border-radius: 50%; overflow: hidden; margin-bottom : 10px; ">
            <img src="/src/assets/face.png" alt="User Image" style="width: 100%; height: 100%; object-fit: cover;">
        </div>
        <div class="input-group mb-3" style="width: 400px; height: 20px;">
            <input type="file" class="form-control" id="inputGroupFile02">
            <label class="input-group-text" for="inputGroupFile02">Upload</label>
        </div>
    </div>
    <!-- 프로필 수정 폼 -->
    <div style="margin-top: 150px;">
        <div style="display: flex; justify-content: center; align-items: center; height: 150px;">
            <div class="card" style="width: 400px; height:420px; " >
                <form @submit.prevent="signup">
                    <div style="margin-bottom: 10px;">
                    <h3 style="text-align: center; margin-top: 30px; margin-bottom: 30px">MODIFY PROFILE</h3>
                        <label for="username" style="margin-left: 20px;">ID : </label>
                        <input type="text" v-model.trim="username" id="username" placeholder="ID를 입력하세요." style="margin-left: 120px; width: 200px;">
                    </div>
                    <div style="margin-bottom: 10px;"> 
                        <label for="password1" style="margin-left: 20px;">PASSWORD : </label>
                        <input type="text" v-model.trim="password1" id="password1" placeholder="PW를 입력하세요." style="margin-left: 50px; width: 200px;">
                    </div>
                    <div style="margin-bottom: 10px;">
                        <label for="password2" style="margin-left: 20px;">PASSWORD : </label>
                        <input type="text" v-model.trim="password2" id="password2" placeholder="PW를 다시 입력하세요." style="margin-left: 50px; width: 200px;">
                    </div>
                    <div style="margin-bottom: 10px;">
                        <label for="password2" style="margin-left: 20px;">NAME : </label>
                        <input type="text" v-model.trim="password2" id="password2" placeholder="이름을 입력하세요." style="margin-left: 90px; width: 200px;">
                    </div>
                    <div style="margin-bottom: 10px;">
                        <label for="password2" style="margin-left: 20px;">FAVORITE GENRE : </label>
                        <input type="text" v-model.trim="password2" id="password2" placeholder="영화취향을 입력하세요." style="margin-left: 10px; width: 200px;">
                    </div>
                    <div style="text-align: center; margin-top: 30px;">
                        <input type="submit" href = "#" value = 'MODIFY' class="btn btn-dark">
                    </div>
                    <div>
                        <input type="submit" href = "#" value = '회원탈퇴' class="btn btn-secondary" style="margin-left: 300px; margin-top: 10px;">
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