<template>
  <main class="container1">
    <div class="titlepart">
      <h1 class="title">예적금 금리 비교</h1>
    </div>
    <div class="selecttype">
        <RouterLink :to="{ name: 'deposit' }">정기예금</RouterLink>
        <RouterLink :to="{ name: 'saving' }">적금</RouterLink>
    </div>
    <div class="contentbox">
      <RouterView />
    </div>
  </main>
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<style scoped>
.container1 {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  /* margin-bottom: 10px; */
}

.titlepart {
  width: 100%;
  height: 200px;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 30px;
  border-bottom: 2px solid lightgray;
}

.title {
  margin-top: 40px;
  font-size: 3rem;
  font-weight: 500;
  font-family: 'Noto Sans KR', sans-serif;
  color: rgb(0, 53, 133);
}

.selecttype {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 50px;
  width: 100%;
  display: flex;
  justify-content: center;
  margin-bottom: 30px;
}

.selecttype a {
  display: inline-block;
  width: 100px;
  height: 100%;
  text-align: center;
  line-height: 50px;
  background-color: rgb(233, 201, 142);
  color: #fff;
  text-decoration: none;
  transition: background-color 0.1s ease;
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 300;
}

.selecttype a.router-link-exact-active {
  background-color: rgb(219, 180, 107);
  color: #fff;
  font-weight: 600;
}

.contentbox {
  width: 80%;
  display: flex;
  justify-content: center;
  background-color: white;;
  box-shadow: 5px 5px 10px 5px lightgray;
  border-radius: 20px;
  margin-bottom: 50px;
  padding-bottom: 50px;
}

</style>
