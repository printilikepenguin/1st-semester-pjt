<template>
  <div class="containerbody">
    <div class="loginarea">
      <h1 class="title">로그인</h1>
      <form @submit.prevent="logIn" class="customform">
        <label for="username">아이디 </label>
        <input type="text" v-model.trim="username" id="username" />
        <label for="password">비밀번호 </label>
        <input type="password" v-model.trim="password" id="password" />
        <input type="submit" value="로그인" class="submit" />
      </form>
      <hr />
      <p class="register-prompt">
        혹시 회원이 아니신가요?
        <RouterLink :to="{ name: 'SignUpView' }" class="register-link"
          >회원가입</RouterLink
        >
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useCounterStore } from "@/stores/counter";

const store = useCounterStore();
const username = ref(null);
const password = ref(null);

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value,
  };
  store.logIn(payload);
};
</script>

<style scoped>
.containerbody {
  width: 100%;
  height: 100vh;
  background-color: rgb(232, 240, 254);
  /* background-image: linear-gradient(
      rgba(255, 255, 255, 0.4),
      rgba(255, 255, 255, 0.4)
    ),
    url("@/assets/backgroundimg.png");
  background-size: cover;
  background-repeat: no-repeat; */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.loginarea {
  background-color: white;
  width: 40%;
  text-align: center;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
}

.customform {
  display: flex;
  flex-direction: column;
}

.title {
  color: hsl(216, 100%, 26%);
  font-weight: 600;
  font-size: 3rem;
}

label {
  color: #4db7e5;
}

input {
  margin-bottom: 30px;
  padding: 8px;
  border: 1px solid #4db7e5;
  border-radius: 5px;
}

input[type="submit"] {
  background-color: #1c5f82;
  color: white;
  padding: 8px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  box-shadow: 0 4px 4px rgba(0, 0, 0, 0.5);
}

hr {
  border: 0;
  height: 1px;
  background-color: #4db7e5;
  margin: 20px 0;
}

.register-prompt {
  color: #4db7e5;
  font-size: 1.2em;
  text-align: center;
}

.register-link {
  color: #1c5f82;
  text-decoration: none;
  font-weight: bold;
  padding: 0 5px;
}

.register-link:hover {
  color: #4db7e5;
}

.submit:hover {
  background-color: #4db7e5;
}
</style>
