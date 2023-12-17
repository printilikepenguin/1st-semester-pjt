<template>
  <div class="container1">
    <div class="dropdown menubar">
      <button
        class="btn btn-secondary dropdown-toggle"
        type="button"
        data-bs-toggle="dropdown"
        aria-expanded="false"
      >
        메뉴
      </button>
      <ul class="dropdown-menu">
        <li>
          <button class="dropdown-item" type="button">
            <RouterLink :to="{ name: 'editinfo' }" class="link"
              >기본정보수정</RouterLink
            >
          </button>
        </li>
        <li>
          <button class="dropdown-item" type="button">
            <RouterLink :to="{ name: 'editprofile' }" class="link"
              >포트폴리오수정</RouterLink
            >
          </button>
        </li>
        <li>
          <button class="dropdown-item" type="button">
            <RouterLink :to="{ name: 'recommend' }" class="link"
              >추천받기</RouterLink
            >
          </button>
        </li>
      </ul>
    </div>

    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<style scoped>
.container1 {
  width: 100vw;
  height: 87vh;
  margin-top: 30px;
  background-color: whitesmoke;
  background-size: cover;
  background-repeat: no-repeat;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

a {
  text-decoration: none;
  color: rgb(28, 54, 89);
  font-weight: 700;
  margin: 13px auto;
}

.menubar {
  position: absolute;
  top: 13%;
  left: 9%;
  width: 20%;
}
</style>
