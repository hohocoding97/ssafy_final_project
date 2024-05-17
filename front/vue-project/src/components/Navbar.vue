<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <img src="/src/assets/minitaco.png" alt="" width="30px" height="30px">
    <a class="navbar-brand" href="#">Takofix</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo02" aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse " id="navbarTogglerDemo02">

      <ul class="navbar-nav mx-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">TakoTalk</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Community</a>
        </li>
        <form class="d-flex" role="search">
          <input class="form-control me-2" type="search" placeholder="검색어를 입력하세요" aria-label="Search">
          <button class="btn btn-dark" type="submit">search</button>
        </form>
      </ul>
      <ul class="navbar-nav me-3 mb-2 mb-lg-0 me-0 ">
        <li class="nav-item">
          <a class="btn btn-dark" href="#" role="button">Sign up</a>
        </li>
      </ul>
      <ul class="navbar-nav me-3 mb-2 mb-lg-0 me-0 ">
        <li class="nav-item">
          <a class="btn btn-dark" href="#" role="button">Login</a>
        </li>
      </ul>
      
    </div>
  </div>
</nav>
</template>

<script setup>

</script>

<style scoped>

</style>