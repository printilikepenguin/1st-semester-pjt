<template>
  <div class="container-pofol">
    <h1 class="title">포트폴리오 수정</h1>

    <div v-if="shouldShowEditForm" class="form">
      <!-- 이미 유형을 저장해놨을 때-->
      <div class="ment" style="color: orange">
        현재 당신의 유형은
        <h3 style="color: rgb(0, 53, 133); font-weight: 800">
          {{ myPortfolio[0].saving_style }}!!
        </h3>
        제일 선호하는 은행은
        <h3 style="color: rgb(0, 53, 133); font-weight: 800">
          {{ myPortfolio[0].favorite_bank }}
        </h3>
        입니다!
      </div>
      <RouterLink :to="{ name: 'recommend' }" class="ment">
        <p>
          다른 {{ myPortfolio[0].saving_style }} 유저가 선택한 적금상품
          확인하기♪
        </p></RouterLink
      >

      <form @submit.prevent="handleSubmit" class="edit-form">
        <h3
          style="
            margin: 2%;
            text-align: left;
            font-family: 'Noto Sans KR', sans-serif;
            color: rgb(219, 180, 107);
          "
        >
          취향이 바뀌셨나요?
        </h3>
        <div>
          <label for="ID">ID : </label>
          <input type="text" v-model="userInfo.username" />
        </div>

        <h3
          style="
            margin: 2%;
            text-align: left;
            font-family: 'Noto Sans KR', sans-serif;
            color: rgb(219, 180, 107);
          "
        >
          저축 스타일
        </h3>
        <div class="container">
          <div class="heros">
            <div class="hero">
              <label for="알뜰형" class="image"></label>
            </div>
            <div class="hero">
              <label for="도전형" class="image"></label>
            </div>
            <div class="hero">
              <label for="성실형" class="image"></label>
            </div>
          </div>
        </div>

        <div class="container">
          <div class="heros">
            <div class="hero-label">
              <input
                type="radio"
                id="알뜰형"
                name="saving_style"
                value="알뜰형"
                v-model="saving_style"
                class="radio-input"
              />
              <label for="알뜰형">알뜰형</label>
            </div>
            <div class="hero-label">
              <input
                type="radio"
                id="도전형"
                name="saving_style"
                value="도전형"
                v-model="saving_style"
                class="radio-input"
              />
              <label for="도전형">도전형</label>
            </div>
            <div class="hero-label">
              <input
                type="radio"
                id="성실형"
                name="saving_style"
                value="성실형"
                v-model="saving_style"
                class="radio-input"
              />
              <label for="성실형">성실형</label>
            </div>
          </div>
        </div>

        <div class="bank-select">
          <label
            for="favorite_bank"
            style="
              margin: 2%;
              text-align: left;
              font-family: 'Noto Sans KR', sans-serif;
              color: rgb(219, 180, 107);
            "
            ><h3>최애은행</h3></label
          >
          <select v-model="favorite_bank">
            <option v-for="bank in banks" :key="bank" :value="bank">
              {{ bank }}
            </option>
          </select>
        </div>
        <input type="submit" value="저장하기" class="form-submit" />
      </form>
    </div>

    <div v-else class="form">
      <!-- 처음 유형을 저장할 때!-->
      <h3 class="ment">당신의 유형을 선택하고 맞춤 상품을 확인하세요!</h3>
      <div class="first-select-form">
        <h3
          style="
            margin: 2%;
            text-align: left;
            font-family: 'Noto Sans KR', sans-serif;
            color: rgb(219, 180, 107);
          "
        >
          저축 스타일
        </h3>
        <div class="container">
          <div class="heros">
            <div class="hero">
              <label for="알뜰형" class="image"></label>
            </div>
            <div class="hero">
              <label for="도전형" class="image"></label>
            </div>
            <div class="hero">
              <label for="성실형" class="image"></label>
            </div>
          </div>
        </div>

        <form @submit.prevent="handleSubmit">
          <div class="container">
            <div class="heros">
              <div class="hero-label">
                <input
                  type="radio"
                  id="알뜰형"
                  name="saving_style"
                  value="알뜰형"
                  v-model="saving_style"
                  class="radio-input"
                />
                <label for="알뜰형">알뜰형</label>
              </div>
              <div class="hero-label">
                <input
                  type="radio"
                  id="도전형"
                  name="saving_style"
                  value="도전형"
                  v-model="saving_style"
                  class="radio-input"
                />
                <label for="도전형">도전형</label>
              </div>
              <div class="hero-label">
                <input
                  type="radio"
                  id="성실형"
                  name="saving_style"
                  value="성실형"
                  v-model="saving_style"
                  class="radio-input"
                />
                <label for="성실형">성실형</label>
              </div>
            </div>
          </div>

          <div class="bank-select">
            <label
              for="favorite_bank"
              style="
                margin: 2%;
                text-align: left;
                font-family: 'Noto Sans KR', sans-serif;
                color: rgb(219, 180, 107);
              "
              ><h3>최애은행</h3></label
            >
            <select v-model="favorite_bank">
              <option v-for="bank in banks" :key="bank" :value="bank">
                {{ bank }}
              </option>
            </select>
          </div>
          <input type="submit" value="저장하기" />
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";
import { useCounterStore } from "@/stores/counter";
import { useRouter } from "vue-router";
import axios from "axios";
import Swal from "sweetalert2";

const Toast = Swal.mixin({
  toast: true,
  position: "top-end",
  showConfirmButton: false,
  timer: 3000,
  timerProgressBar: true,
  didOpen: (toast) => {
    toast.addEventListener("mouseenter", Swal.stopTimer);
    toast.addEventListener("mouseleave", Swal.resumeTimer);
  },
});

const store = useCounterStore();
const router = useRouter();
const userInfo = store.userInfo;
const portfolio = ref([]);
const saving_style = ref("");
const favorite_bank = ref("");
const banks = [
  "KEB하나은행",
  "SC제일은행",
  "국민은행",
  "신한은행",
  "외환은행",
  "우리은행",
  "한국시티은행",
  "지방은행",
  "경남은행",
  "광주은행",
  "대구은행",
  "부산은행",
  "전북은행",
  "제주은행",
  "특수은행",
  "기업은행",
  "농협",
  "수협",
  "한국산업은행",
  "한국수출입은행",
];
const savingStyles = ["알뜰형", "도전형", "성실형"];

const myPortfolio = computed(() => {
  return portfolio.value.filter((item) => item.user === userInfo.id);
});

onMounted(() => {
  getPortfolio();
});
console.log(userInfo);
const getPortfolio = function () {
  axios({
    method: "get",
    url: `${store.API_URL}/accounts/find/input_portfolioData/`,
  })
    .then((res) => {
      portfolio.value = res.data;
      console.log(portfolio);
    })
    .catch((err) => {
      console.log(err);
    });
};

const shouldShowEditForm = computed(() => {
  return portfolio.value.some((item) => item.user === userInfo.id);
});

const handleSubmit = function () {
  if (shouldShowEditForm.value) {
    editPortfolio(portfolio.value.find((item) => item.user === userInfo.id).id);
  } else {
    createPortfolio();
  }
};

const createPortfolio = function () {
  axios({
    method: "post",
    url: `${store.API_URL}/accounts/find/input_portfolioData/`,
    data: {
      user: userInfo.id,
      saving_style: saving_style.value,
      favorite_bank: favorite_bank.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      console.log(res.data);
      Toast.fire({
        icon: "success",
        title: "정상적으로 저장되었습니다!",
      });
      router.go(0);
    })
    .catch((error) => {
      console.log(error);
    });
};

const editPortfolio = function (portfolioId) {
  axios({
    method: "put",
    url: `${store.API_URL}/accounts/find/get_portfolioData/${portfolioId}`,
    data: {
      user: userInfo.id,
      saving_style: saving_style.value,
      favorite_bank: favorite_bank.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      console.log(res.data);
      getPortfolio();
      Toast.fire({
        icon: "success",
        title: "수정 완료!",
      });
    })
    .catch((error) => {
      console.log(error);
    });
};
</script>

<style scoped>
.container-pofol {
  width: 75%;
  margin-bottom: 2.5%;
  height: auto;
  overflow-x: hidden;
  background-color: white;
  box-shadow: 5px 5px 10px 5px lightgray;
  border-radius: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 30px;
  padding-bottom: 80px;
}
.container-pofol::-webkit-scrollbar {
  width: 10px; /* 스크롤바의 너비 */
}

.container-pofol::-webkit-scrollbar-thumb {
  height: 20%; /* 스크롤바의 길이 */
  background: rgb(0, 53, 133); /* 스크롤바의 색상 */
  border-radius: 10px;
}

.container-pofol::-webkit-scrollbar-track {
  background: rgba(33, 122, 244, 0.1); /*스크롤바 뒷 배경 색상*/
}

.container-pofol::-webkit-scrollbar-thumb {
  height: 50%;
}
.title {
  width: 100%;
  text-align: center;
  margin: 30px 0px;
  font-size: 3rem;
  font-weight: 400;
  font-family: "Noto Sans KR", sans-serif;
  color: rgb(0, 53, 133);
  border-bottom: 1px solid grey;
  padding-bottom: 30px;
}
.form {
  width: 100%;
}
.first-select-form {
  width: 90%;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  background-color: #f8f8f8;
}
.ment {
  text-align: center;
  margin-top: 40px;
  margin-bottom: 40px;
  font-weight: 400;
  font-family: "Noto Sans KR", sans-serif;
  color: rgb(0, 53, 133);
}
.radio-div {
  width: 30%;
  height: 84px;
  margin: 4px;
  border: 3px solid #fff;
  border-radius: 10px;
  box-sizing: border-box;
  background-color: #555;
  overflow: hidden;
  transform: skewX(-14deg);
  transition: transform 0.1s, background-color 0.6s;
}
.form label {
  display: block;
  margin-bottom: 5px;
}

.form input[type="text"],
.form select {
  width: 100%;
  padding: 8px;
  margin-bottom: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
  box-sizing: border-box;
}

.form input[type="submit"] {
  width: 100%;
  padding: 10px;
  border: none;
  border-radius: 5px;
  background-color: rgb(0, 53, 133);
  color: white;
  cursor: pointer;
}

.form input[type="submit"]:hover {
  background-color: #4db7e5;
}
.edit-form {
  width: 90%;
  margin-bottom: 30%;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  background-color: #f8f8f8;
}
.radio-group {
  display: flex;
  flex-wrap: wrap;
}

.radio-item {
  margin-right: 20px;
  margin-bottom: 10px;
}

.radio-label {
  display: inline-block;
  padding: 8px 12px;
  border: 1px solid #1c5f82;
  border-radius: 20px;
  color: #1c5f82;
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s;
}

.radio-label:hover {
  background-color: #1c5f82;
  color: white;
}
.container {
  /* padding: 50px 0; */
}

.container .heros {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  max-width: 700px;
  margin: 0 auto;
}

.container .heros .hero {
  width: 30%;
  height: 84px;
  margin: 4px;
  border: 3px solid #fff;
  border-radius: 10px;
  box-sizing: border-box;
  background-color: #555;
  overflow: hidden;
  transform: skewX(-14deg);
  transition: transform 0.1s, background-color 0.6s;
}

.container .heros .hero-label {
  width: 30%;
  height: 84px;
  font-weight: 400;
  font-family: "Noto Sans KR", sans-serif;
}

.container .heros .hero:hover {
  background-color: #ff9c00;
  transform: skewX(-14deg) scale(1.3);
  z-index: 1;
}

.container .heros .hero .image {
  width: 140%;
  height: 100%;
  transform: skew(14deg) translateX(-16px);
  background-position: center;
  background-size: 90px;
  background-repeat: no-repeat;
}

.container .heros .hero:nth-child(1) .image {
  background-image: url("https://raw.githubusercontent.com/printilikepenguin/forUserContent/master/piggy-bank-1270926_1280-removebg-preview.png");
}
.container .heros .hero:nth-child(2) .image {
  background-image: url("https://raw.githubusercontent.com/printilikepenguin/forUserContent/master/combat-diver-60545_1280-removebg-preview.png");
}
.container .heros .hero:nth-child(3) .image {
  background-image: url("https://raw.githubusercontent.com/printilikepenguin/forUserContent/master/sea-7695699_1280-removebg-preview.png");
}
</style>
