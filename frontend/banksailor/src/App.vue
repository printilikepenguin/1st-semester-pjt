<script setup>
import Swal from "sweetalert2";
import { RouterLink, RouterView } from "vue-router";
import { useCounterStore } from "@/stores/counter";
import { useRouter } from "vue-router";
import { navbarLinks } from "/src/constants/navbarLinks";

const store = useCounterStore();

const customlogout = async function () {
  // Toast.fire({
  //   icon: "error",
  //   title: "",
  // });
  Swal.fire({
    title: "정말 로그아웃하실건가요?",
    text: "다시 되돌릴 수 없습니다",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "YES",
    cancelButtonText: "NO",
    customClass: {
      container: "swal-container",
    },
  }).then((result) => {
    if (result.isConfirmed) {
      Swal.fire("로그아웃!", "성공적으로 로그아웃되었습니다", "success");
      store.logOut();
    }
  });
};

const router = useRouter();

const goHome = () => {
  router.push({ name: "home" });
};

</script>

<template>
  <header>
    <nav>
      <a class="navbar-brand" href="#" @click.prevent="goHome">
        <img src="@/assets/title_logo.png" alt="Logo" height="40" />
      </a>
      <div class="navbar-items">
        <template v-for="(item, idx) in navbarLinks" key="item">
          <div
            class="navbar-item"
            :class="{ active: $route.fullPath.includes(item.links) || (item.links === 'deposit' && $route.fullPath.includes('saving'))}">
            <RouterLink
              :to="{ name: item.links }"
              style="font-family: 'Noto Sans KR', sans-serif"
              >{{ item.label }}</RouterLink
            >
          </div>
        </template>
      </div>

      <div class="auth">
        <template v-if="store.isLogin">
          <form @submit.prevent="customlogout">
            <input type="submit" value="Logout" class="logout" />
          </form>

          <RouterLink :to="{ name: 'editinfo' }" class="profile"
            >프로필</RouterLink
          >
        </template>
        <template v-else>
          <RouterLink :to="{ name: 'LogInView' }" class="login"
            >로그인</RouterLink
          >
          <RouterLink :to="{ name: 'SignUpView' }" class="signup"
            >회원가입</RouterLink
          >
        </template>
      </div>
    </nav>
    <div :class="{ 'gradation': !$route.fullPath.includes('home') }"></div>
    <div :class="{ 'gradation-home': $route.fullPath.includes('home') }"></div>
  </header>
  <RouterView />
  <footer>
    <div class="copyright">
      Copyright 2023. BankSailor. All rights reserved.
    </div>
    <div class="link-bar">
      <a href="#">이용약관</a>  |
      <a href="#">개인정보처리방침</a>  |
      <a href="#">사이트맵</a>  |
      <a href="#">서비스 문의</a>
    </div>
  </footer>
</template>

<style scoped>
nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  height: 9vh;
  margin: 0 auto;
  flex-wrap: nowrap;
  background-color: white;
}

.navbar-brand {
  margin-left: 40px;
}

.navbar-items {
  margin-right: 200px;
  width: 500px;
  height: 100%;
  display: flex;
  justify-content: center;
}

.navbar-item {
  width: 25%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.auth {
  width: 170px;
  height: 100%;
  margin-right: 40px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.login {
  border: 1px solid #000f50;
  color: rgb(0, 52, 119);
  padding: 5px 10px;
  border-radius: 30px;
  font-weight: 600;
}

.signup,
.logout {
  border: 1px solid #000f50;
  background-color: rgb(0, 52, 119);
  color: white;
  padding: 5px 12px;
  border-radius: 30px;
}
.active {
  color: #00082e;
  font-weight: 800;
  border-bottom: 3px solid #00082e;
}

.profile {
  border: 1px solid #000f50;
  color: #000f50;
  padding: 5px 10px;
  border-radius: 30px;
  font-weight: 600;
}

a {
  text-decoration: none;
  color: #000f50;
}

.gradation {
  width: 100%;
  height: 10px;
  background: linear-gradient(to bottom, lightgrey, transparent);
}

.gradation-home {
  width: 100%;
  height: 10px;
  background: linear-gradient(to bottom, lightgrey, white);
}

footer {
  width: 100%;
  height: 80px;
  background-color: rgb(0, 52, 119);
  display: flex;
  align-items: center;
  justify-content: space-around;
  color: white;
}

.copyright {
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 300;
}

.link-bar a {
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 0.8rem;
  font-weight: 300;
  text-decoration: none;
  color: white;
}

.link-bar a:hover {
  text-decoration: underline;
}

</style>
