<template>
  <div class="container2">
    <div v-if="isLoading">
      <div class="loading">
        <FadeLoader :loading="isLoading" />
      </div>
    </div>
    <div v-else class="real">
      <h1 class="title">기본 정보 수정</h1>
      <Form
        @submit.prevent="UpdateInfo"
        :validation-schema="schema"
        v-slot="{ errors }"
        class="FF"
      >
        <form @submit.prevent="UpdateInfo" class="customform">
          <br />
          <div class="inputarea">
            <p class="label">닉네임</p>
            <Field
              name="nickname"
              v-model="nickname"
              :model-value="store.userInfo.nickname"
            />

            <p class="label">이메일</p>
            <Field
              name="email"
              v-model="email"
              :model-value="store.userInfo.email"
            />
            <span class="warning">{{ errors.email }}</span>

            <p class="label">현재 자산</p>
            <Field
              name="money"
              type="number"
              v-model="money"
              :model-value="store.userInfo.money"
            />
            <span class="warning">{{ errors.money }}</span>

            <p class="label">연봉</p>
            <Field
              name="salary"
              type="number"
              v-model="salary"
              :model-value="store.userInfo.salary"
            />
            <span class="warning">{{ errors.salary }}</span>
            <br />
            <button type="submit" value="가입하기" class="submit">
              수정하기
            </button>
          </div>
        </form>
      </Form>
      <div class="chartarea">
        <h3 class="subtitle">내가 가입한 상품</h3>
        <div class="chart1">
          <p class="saving">[예금]</p>
          <DepositChart />
        </div>
        <div class="chart1">
          <p class="saving">[적금]</p>
          <SavingChart />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import Swal from "sweetalert2";
import DepositChart from "../../components/ProfileViewComponents/DepositChart.vue";
import SavingChart from "../../components/ProfileViewComponents/SavingChart.vue";
import { useCounterStore } from "@/stores/counter";
import { onMounted, watchEffect, ref, computed } from "vue";
import FadeLoader from "vue-spinner/src/FadeLoader.vue";
import { Form, Field, defineRule } from "vee-validate";
import axios from "axios";
const store = useCounterStore();
const isLoading = ref(true);
// const username = ref("");

const email = ref(null);
const nickname = ref("");
const money = ref("");
const salary = ref("");

const like_deposit = ref(null);
const like_saving = ref(null);

// const changed = computed(() => {
//   return (
//     nickname.value !== store.userInfo.nickname ||
//     money.value !== store.userInfo.money ||
//     salary.value !== store.userInfo.salary ||
//     email.value !== store.userInfo.email
//   );
// });

onMounted(async () => {
  try {
    store.getUserInfo();
    // username.value = store.userInfo.username;
    // email.value = store.userInfo.email;
    // nickname.value = store.userInfo.nickname;
    // age.value = store.userInfo.age;
    // money.value = store.userInfo.money;
    // salary.value = store.userInfo.salary;
    like_deposit.value = store.userInfo.like_deposit;
    like_saving.value = store.userInfo.like_saving;
    isLoading.value = false;
  } catch (err) {
    // console.error(err);
  }
});

const UpdateInfo = async function () {
  if (isFormValid) {
    try {
      await axios.put(
        `${store.API_URL}/accounts/find/update/`,
        {
          email: email.value || store.userInfo.email,
          nickname: nickname.value || store.userInfo.nickname,
          salary: salary.value || store.userInfo.salary,
          money: money.value || store.userInfo.money,
        },
        {
          headers: {
            Authorization: `Token ${store.token}`,
          },
        }
      );
      await store.getUserInfo();
      Swal.fire("성공", "정보가 업데이트되었습니다.", "success");
    } catch (error) {
      console.error(error);
    }
  } else {
    Swal.fire("오류", "유효하지 않은 정보입니다.", "error");
  }
};

defineRule("validEmail", (value) => {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (regex.test(value)) {
    return true;
  }
  return "올바른 이메일 형식이어야 합니다.";
});

defineRule("validAge", (value) => {
  const age = parseInt(value);
  if (!isNaN(age) && age >= 1 && age <= 130) {
    return true;
  }
  return "1에서 130 사이의 숫자여야 합니다.";
});

defineRule("validPositiveNumber", (value) => {
  const number = parseFloat(value);
  if (!isNaN(number) && number >= 0) {
    return true;
  }
  return "0 이상의 숫자여야 합니다.";
});

defineRule("required", (value) => {
  if (!value) {
    return "필수 입력 항목입니다.";
  }
  return true;
});

const schema = {
  // username: "required",
  email: "required|validEmail",
  nickname: "required",
  age: "required|validAge",
  money: "required|validPositiveNumber",
  salary: "required|validPositiveNumber",
};

const isFormValid = computed(() => {
  return (
    nickname.value &&
    money.value &&
    salary.value &&
    email.value &&
    !errors.email &&
    !errors.money &&
    !errors.salary
  );
});
</script>

<style scoped>
.warning {
  color: red;
  margin-bottom: 20px;
}
.container2 {
  width: 75%;
  height: auto;
  margin-bottom: 2.5%;
  overflow-x: hidden;
  background-color: white;
  box-shadow: 5px 5px 10px 5px lightgray;
  border-radius: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 30px;
}

.container2::-webkit-scrollbar {
  width: 10px; /* 스크롤바의 너비 */
}

.container2::-webkit-scrollbar-thumb {
  height: 20%; /* 스크롤바의 길이 */
  background: rgb(0, 53, 133); /* 스크롤바의 색상 */
  border-radius: 10px;
}

.container2::-webkit-scrollbar-track {
  background: rgba(33, 122, 244, 0.1); /*스크롤바 뒷 배경 색상*/
}

.container2::-webkit-scrollbar-thumb {
  height: 50%;
}
.customform {
  width: 80%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.FF {
  width: 100%;
  display: flex;
  justify-content: center;
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

.chartarea {
  margin-top: 70px;
  width: 100%;
  text-align: center;
  padding: 0px 40px;
}

.saving {
  font-size: 20px;
  font-weight: 800;
  color: rgb(7, 152, 242);
  background-color: rgb(205, 234, 190);
  padding-bottom: 5px;
}

.chart1 {
  border: 3px solid rgb(205, 234, 190);
  margin-bottom: 40px;
}

input[type="number"]::-webkit-outer-spin-button,
input[type="number"]::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

.label {
  color: RGB(0, 53, 133);
  margin-top: 5px;
  margin-bottom: 0px;
  text-align: center;
}

input {
  margin-bottom: 13px;
  padding: 8px;
  border-radius: 5px;
  width: 100%;
  border: 0.5px solid RGB(0, 53, 133);
}

.inputarea {
  display: flex;
  flex-direction: column;
  align-items: start;
  width: 70%;
}

.submit {
  background-color: #1c5f82;
  width: 60%;
  color: white;
  padding: 8px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  box-shadow: 0 4px 4px rgba(0, 0, 0, 0.5);
  align-self: center;
}

.submit:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.subtitle {
  width: 100%;
  text-align: center;
  margin: 30px 0px;
  font-size: 2rem;
  font-weight: 400;
  font-family: "Noto Sans KR", sans-serif;
  color: rgb(0, 53, 133);
  border-bottom: 1px solid grey;
  padding-bottom: 30px;
}

.real {
  width: 100%;
}
</style>
