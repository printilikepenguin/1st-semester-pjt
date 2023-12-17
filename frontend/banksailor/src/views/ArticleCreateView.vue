<template>
  <div class="titlepart">
    <h1 class="title">새글쓰기</h1>
  </div>

  <div class="container2">
    <form @submit.prevent="createArticle" class="customform">

      <div class="form-group">
        <label class="form-label" for="category">카테고리</label>
        <select v-model="selectedCategory" id="category">
          <option
            v-for="category in categoryList"
            :key="category.id"
            :value="category.value"
          >
            {{ category.value }}
          </option>
        </select>
      </div>

      <div class="form-group">
        <label class="form-label" for="title">제목</label>
        <input
          type="text"
          v-model.trim="title"
          id="title"
          class="form-control"
          placeholder="제목 입력, 최대 100자까지 가능합니다"
        />
      </div>

      <div class="form-group">
        <label class="form-label" for="content">내용</label>
        <textarea
          v-model.trim="content"
          id="content"
          class="form-control form-control-textarea"
          placeholder="내용을 입력해주세요"
        ></textarea>
      </div>

      <input type="submit" value="저장" class="form-submit"/>

    </form>

    <button class="btn" @click="moveToList()">목록</button>

  </div>
</template>

<script setup>
import Swal from "sweetalert2";
import axios from "axios";
import { ref } from "vue";
import { useCounterStore } from "@/stores/counter";
import { useRouter } from "vue-router";

const store = useCounterStore();
const router = useRouter();
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
const content = ref(null);
const selectedCategory = ref(null);
const categoryList = [
  {
    id: 1,
    value: "잡담",
  },
  {
    id: 2,
    value: "리뷰",
  },
];

const createArticle = function () {
  axios({
    method: "post",
    url: `${store.API_URL}/articles/articles/`,
    data: {
      title: title.value,
      content: content.value,
      category: selectedCategory.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      // console.log(res)
      router.push({ name: "article" });
    })
    .catch((err) => {
      Toast.fire({
        icon: "warning",
        title: "빈칸을 모두 채워주세요!",
      });
    });
};

const moveToList = () => {
  router.push({ name: "article" });
};
</script>

<style scoped>
.container2 {
  margin: 0 auto;
  width: 80%;
  background-color: white;;
  box-shadow: 5px 5px 10px 5px lightgray;
  border-radius: 20px;
  margin-bottom: 50px;
  padding-bottom: 50px;
}
.titlepart {
  width: 100%;
  height: 200px;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 30px;
  border-bottom: 2px solid lightgray;
  /* border-bottom: 2px solid hsl(216, 100%, 26%); */
}
.title {
  margin-top: 40px;
  font-size: 3rem;
  font-weight: 400;
  font-family: 'Noto Sans KR', sans-serif;
  color: rgb(0, 53, 133);
}
.customform {
  max-width: 900px;
  height: 60vh;
  margin: 20px auto;
  padding: 20px;
  border-radius: 10px;
  font-family: 'Noto Sans KR', sans-serif; 
}
.form-group {
  margin-bottom: 3%;
  font-family: 'Noto Sans KR', sans-serif; 
}

.form-label {
  text-align: left;
  display: block;
  margin-bottom: 5px;
  color: #1c5f82;
  font-family: 'Noto Sans KR', sans-serif; 
}

.form-control {
  width: 100%;
  padding: 10px;
  border: 1px solid #cccccc;
  border-radius: 5px;
}

.form-control-textarea {
  height: 300px;
}

.form-submit {
  padding: 10px 20px;
  color: #ffffff;
  background-color: rgb(0, 53, 133);
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.form-submit:hover {
  background-color: #4db7e5;
}

.btn {
  display: block;
  width: 100px;
  margin: 20px auto;
  padding: 10px;
  color: #ffffff;
  background-color: rgb(0, 53, 133);
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-family: 'Noto Sans KR', sans-serif; 
}

.btn:hover {
  background-color: #4db7e5;
}
</style>
