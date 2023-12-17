<template>
  <div class="container2">
    <Form
      class="formarea"
      @submit.prevent="signUp"
      :validation-schema="schema"
      v-slot="{ errors }"
    >
      <h1 class="title">회원가입</h1>
      <form @submit.prevent="signUp" class="formarea1">
        <div class="inputarea">
          <p class="label">아이디</p>
          <div class="username">
            <div class="usernameinput">
              <Field
                name="username"
                v-model="username"
                placeholder="사용하고 싶은 아이디을 입력해주세요."
              />
              <div class="warning">{{ errors.username }}</div>
            </div>
            <button @click="checkId">중복확인버튼</button>
          </div>

          <p class="idconfirm" v-show="isChecked == 2" style="color: red">
            중복된 아이디 입니다.
          </p>
          <p class="idconfirm" v-show="isChecked == 1" style="color: green">
            사용 가능한 아이디 입니다.
          </p>

          <p class="label">이메일</p>
          <Field
            name="email"
            v-model="email"
            placeholder="이메일을 입력해주세요."
          />
          <span class="warning">{{ errors.email }}</span>

          <p class="label">비밀번호</p>
          <Field
            name="password1"
            type="password"
            v-model="password1"
            placeholder="비밀번호를 입력해주세요."
          />
          <span class="warning">{{ errors.password1 }}</span>

          <p class="label">비밀번호 확인</p>
          <Field name="password2" type="password" v-model="password2" />
          <span class="warning">{{ errors.password2 }}</span>

          <p class="label">닉네임</p>
          <Field
            name="nickname"
            v-model="nickname"
            placeholder="닉네임을 입력해주세요."
          />
          <span class="warning">{{ errors.nickname }}</span>

          <p class="label">나이</p>
          <Field
            name="age"
            type="number"
            v-model="age"
            placeholder="나이를 입력해주세요."
          />
          <span class="warning">{{ errors.age }}</span>

          <p class="label">현재 자산</p>
          <Field
            name="money"
            type="number"
            v-model="money"
            placeholder="현재 자산을 입력해주세요."
          />
          <span class="warning">{{ errors.money }}</span>

          <p class="label">연봉</p>
          <Field
            name="salary"
            type="number"
            v-model="salary"
            placeholder="연봉을 입력해주세요."
          />
          <span class="warning">{{ errors.salary }}</span>
          <button
            :disabled="!isFormValid"
            type="submit"
            value="가입하기"
            class="submit"
          >
            가입하기
          </button>
        </div>
      </form>
    </Form>
  </div>
</template>

<script setup>
import { Form, Field, defineRule } from "vee-validate";
import { useCounterStore } from "@/stores/counter";
import { ref, computed } from "vue";
import axios from "axios";

defineRule("confirmed", (value, [target]) => {
  if (value == target) {
    return true;
  }
  return "비밀번호가 일치하지 않습니다.";
});

defineRule("required", (value) => {
  if (!value) {
    return "필수 입력 항목입니다.";
  }
  return true;
});

defineRule("different", (value, [target]) => {
  if (value !== target) {
    return true;
  }
  return "위험성이 높은 패스워드입니다. 다른 값을 입력해주세요.";
});

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

defineRule("minlen", (value) => {
  if (value.length > 5) {
    return true;
  }
  return "비밀번호가 너무 짧습니다";
});

const schema = {
  username: "required",
  email: "required|validEmail",
  password1: "required|minlen|different:@username",
  password2: "required|confirmed:@password1",
  nickname: "required",
  age: "required|validAge",
  money: "required|validPositiveNumber",
  salary: "required|validPositiveNumber",
};

const store = useCounterStore();
const username = ref(null);
const password1 = ref(null);
const password2 = ref(null);
const email = ref(null);
const nickname = ref(null);
const age = ref(null);
const money = ref(null);
const salary = ref(null);
const isChecked = ref(null);

const checkId = function () {
  // 아이디 값이 존재하면 axios 요청
  if (username.value) {
    axios({
      // 조회니까 get
      method: "get",
      //  중복확인 하는 URL로
      url: `${store.API_URL}/accounts/find/duplicateID/`,
      // get 이여서 params? 사용
      params: {
        username: username.value,
      },
      // 요청 성공시
    })
      .then((res) => {
        // console.log(res);
        // isChecked 로 p 태그 조작
        if (isChecked.value) {
          // res.data == 1인 경우 아이디가 존재하지않는 경우이므로 사용 문구
          if (res.data == 1) {
            if (isChecked.value == 2) {
              isChecked.value = 1;
            }
          }
          // res.data == 2인 경우 아이디가 존재하기 떄문에 사용불가 문구
          else if (res.data == 2) {
            if (isChecked.value == 1) {
              isChecked.value = 2;
            }
          }
        } else {
          isChecked.value = res.data;
        }
      })
      .catch((error) => {
        console.log(error);
      });
  } else {
    isChecked.value = null;
    alert("아이디를 입력해주세요");
  }
};

const isFormValid = computed(() => {
  return (
    username.value &&
    password1.value &&
    password2.value &&
    email.value &&
    nickname.value &&
    age.value &&
    money.value &&
    salary.value &&
    isChecked.value === 1
  );
});

const signUp = function () {
  if (isFormValid.value) {
    const payload = {
      username: username.value,
      password1: password1.value,
      password2: password2.value,
      email: email.value,
      nickname: nickname.value,
      age: age.value,
      money: money.value,
      salary: salary.value,
    };
    console.log(payload);
    store.signUp(payload);
  }
};
</script>

<style scoped>
.container2 {
  background-color: rgb(232, 240, 254);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 91vh;
  margin: 0px 0px;
}

.warning {
  color: red;
  margin-bottom: 20px;
}

.formarea {
  background-color: white;
  width: 50%;
  margin-top: 30px;
  border-radius: 15px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
}

.formarea1 {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-bottom: 30px;
}

.title {
  color: hsl(216, 100%, 26%);
  font-weight: 600;
  font-size: 3rem;
  text-align: center;
  margin-top: 40px;
}

.username {
  display: flex;
  width: 100%;
  align-items: center;
  justify-content: start;
}

.username input {
  width: 90%;
  border: 1px solid #4db7e5;
  border-radius: 5px;
  margin-bottom: 0px;
}

.username button {
  border: 1px solid #4db7e5;
  border-radius: 5px;
  cursor: pointer;
  background-color: #1c5f82;
  color: white;
  width: 150px;
  height: 32px;
  margin-bottom: 30px;
}

input {
  margin-bottom: 0px;
  padding: 8px;
  border: 1px solid #4db7e5;
  border-radius: 5px;
  width: 100%;
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

.submit {
  background-color: #1c5f82;
  width: 60%;
  color: white;
  padding: 8px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  box-shadow: 0 4px 4px rgba(0, 0, 0, 0.5);
}

.submit:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.submit:not(:disabled):hover {
  background-color: #4db7e5;
}

.label {
  color: #4db7e5;
  margin-top: 5px;
  margin-bottom: 0px;
  text-align: center;
}

.inputarea {
  display: flex;
  flex-direction: column;
  align-items: start;
  width: 60%;
  margin-top: 30px;
}

.idconfirm {
  margin-top: 0;
  padding-top: 0;
}

input[type="number"]::-webkit-outer-spin-button,
input[type="number"]::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

.usernameinput {
  width: 70%;
}
</style>
