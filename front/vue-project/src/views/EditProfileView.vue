<template>
    <!-- 프로필 변경 상단 -->
    <div class="Profile d-flex flex-column align-items-center">
        <h3 style="margin-top: 10px; font-weight: bold;">프로필 변경</h3>
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
                    <input type="checkbox" id="layerPopup">
                    <label for="layerPopup" style="margin-left: 300px;" class="btn btn-dark">
                        회원탈퇴
                    </label>
                    <div id="layer_bg">
                        <div id="popup">
                            <h2>
                               회원탈퇴 
                                <label for="layerPopup">X</label>
                            </h2>
                            <p>회원 탈퇴를 신청하기 전, 다음 내용을 꼭 확인해 주세요</p>
                            <p> - 고객 정보 및 서비스 이용 기록은 개인 정보 보호 처리 방침에 따라 삭제됩니다.</p>
                            <p> - 회원 탈퇴 시 더 이상 Takofix(이하, 탁호픽스) 서비스 이용이 불가능하며, 탈퇴 처리 됩니다.</p>
                            <div class="container mt-5">
                                <div class="form-check form-check-inline">
                                    <input class="form-check-input" type="checkbox" id="exampleCheckbox">
                                    <label class="form-check-label" for="exampleCheckbox">
                                        안내사항을 모두 확인하였으며, 이에 동의합니다.
                                    </label>
                                </div>
                            </div>
                            <div style="text-align: center; margin-top: 20px;">
                                <input type="submit" href = "#" value = '회원탈퇴' class="btn btn-dark">                           
                            </div>
                        </div>
                    </div>
                    </div>
                </form>
            </div>
        </div>
    </div>

    <!-- 회원 탈퇴 팝업 구현 -->
    

</template>

<script setup>

</script>

<style scoped>
#layerPopup {
    display: none;
}

#layerPopup + label {
    display:inline-block;
    padding: 7px 14px;
    background:#333;
    color:#fff;
}

#layer_bg {
    display:none;
    position:absolute;
    top:0;
    left:0;
    width:100%;
    height:100%;
    background:rgba(0,0,0,0.5);
}

#layer_bg > #popup {
    position:absolute;
    padding:15px;
    box-sizing:border-box;
    border-radius:15px; 
    top:50%;
    left:50%;
    transform:translate(-50%, -50%);
    width:500px;
    height:400px;
    background:#fff;
    box-shadow: 7px 7px 5px rgba(0,0,0,0.2); 
}

#layer_bg > #popup > h2 {
    margin-bottom:25px;
}

#layer_bg > #popup > h2 > label {
    float: right;
}

#layerPopup:checked + label + #layer_bg {
    display:block;
}
</style>