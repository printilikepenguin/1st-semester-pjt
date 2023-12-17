<template>
  <div class="titlepart">
    <h1 class="title">게시판</h1>
  </div>

  <div class="container2">
    <form @submit.prevent="searchArticle" class="search-bar">
      <select v-model="key_for_search">
        <option disabled value="">선택</option>
        <option value="category">분류</option>
        <option value="title" :selected="true">제목</option>
        <option value="content">내용</option>
        <option value="user">작성자</option>
      </select>
      &nbsp;
      <!-- 줄바꿈없이 간격띄우는 인자 -->
      <input type="text" v-model="value_for_search" />
      &nbsp;
      <input type="submit" value="  검색  " />
    </form>

    <div class="board">
      <div v-if="searchfinish === true">
        <h3
          style="
            text-align: center;
            margin-top: 40px;
            font-weight: 400;
            font-family: 'Noto Sans KR', sans-serif;
            color: rgb(0, 53, 133);
          "
        >
          총 {{ filtered_article.length }}건의 검색결과가 있습니다
        </h3>
        <hr />
        <div>
          <table class="table">
            <thead class="thead">
              <th class="th1">번호</th>
              <th class="th2">분류</th>
              <th class="th3">제목</th>
              <th class="th4">작성자</th>
              <th class="th5">작성일</th>
            </thead>

            <tbody class="tbody1">
              <tr v-for="article in filtered_article" :key="article.id">
                <td class="td1">{{ article.id }}</td>
                <td class="td2">{{ article.category }}</td>
                <td>
                  <RouterLink
                    class="td3"
                    :to="{
                      name: 'ArticleDetailView',
                      params: { id: article.id },
                    }"
                  >
                    <p>{{ article.title }}</p>
                  </RouterLink>
                </td>
                <td class="td4">{{ article.username }}</td>
                <td class="td5">{{ article.created_at.slice(0, 10) }}</td>
              </tr>
            </tbody>
          </table>

          <button @click="searchfinish = !searchfinish">목록가기</button>
        </div>
      </div>

      <div v-else class="board">
        <ArticleList />

        <div
          v-show="store.isLogin === true"
          style="display: flex; justify-content: flex-end; margin-top: 5%"
        >
          <RouterLink :to="{ name: 'ArticleCreateView' }">
            <button>새글쓰기</button>
          </RouterLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import Swal from "sweetalert2";
import { onMounted, computed, ref } from "vue";
import { useCounterStore } from "@/stores/counter";
import { RouterLink } from "vue-router";
import axios from "axios";
import ArticleList from "@/components/ArticleViewComponents/ArticleList.vue";

const store = useCounterStore();
const searchfinish = ref(false);
const key_for_search = ref(null);
const value_for_search = ref("");

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

onMounted(() => {
  store.getArticles();
});

const filtered_article = computed(() => {
  if (key_for_search.value && value_for_search.value) {
    const key = key_for_search.value;
    const value = value_for_search.value;
    if (key === "all") {
      return store.articles.filter(
        (article) =>
          store.articles.category.includes(value) ||
          store.articles.title.includes(value) ||
          store.articles.content.includes(value) ||
          store.articles.user.includes(value)
      );
    } else {
      return store.articles.filter((article) => article[key].includes(value));
    }
  } else {
    return store.articles.value;
  }
});

const searchArticle = function () {
  if (!value_for_search.value) {
    Toast.fire({
      icon: "warning",
      title: "검색어를 입력해주세요!",
    });
  } else {
    searchfinish.value = true;
  }
};
</script>

<style scoped>
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
  font-family: "Noto Sans KR", sans-serif;
  color: rgb(0, 53, 133);
}
.container2 {
  margin: 0 auto;
  height: 91vh;
  padding: 5%;
  width: 80%;
  background-color: white;
  box-shadow: 5px 5px 10px 5px lightgray;
  border-radius: 20px;
  margin-bottom: 50px;
  padding-bottom: 50px;
}
.thead {
  height: 50px;
  background-color: rgb(233, 201, 142);
  vertical-align: middle;
  text-align: center;
  font-weight: 300;
  font-family: "Noto Sans KR", sans-serif;
  font-size: larger;
}

button {
  border-radius: 30px;
  padding-bottom: 4px;
  width: 80px;
  height: 35px;
  color: white;
  background-color: rgb(0, 53, 133);
}
button:hover {
  background-color: #4db7e5;
  border: solid 1px #4db7e5;
}
.search-bar {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
}
.search-bar select,
.search-bar input[type="text"],
.search-bar button {
  padding: 8px;
  margin: 0 5px;
  border-radius: 4px;
  border: 1px solid #ccc;
  font-size: 14px;
}
.search-bar input[type="submit"] {
  padding: 8px;
  margin: 0 5px;
  border-radius: 4px;
  border: 1px solid #ccc;
  font-size: 14px;
  background-color: rgb(0, 53, 133);
  color: white;
  border: none;
  cursor: pointer;
}
.search-bar input:hover {
  background-color: #4db7e5;
  border: 1px solid #4db7e5;
}

.tbody1 {
  vertical-align: middle;
  border-bottom: 1px solid darkgray;
}
.td1 {
  width: 10%;
  vertical-align: middle;
  border-collapse: collapse;
  text-align: center;
  font-family: "Noto Sans KR", sans-serif;
}
.td2 {
  width: 15%;
  vertical-align: middle;
  border-collapse: collapse;
  text-align: center;
  font-family: "Noto Sans KR", sans-serif;
}
.td3 {
  width: 45%;
  vertical-align: middle;
  border-collapse: collapse;
  text-align: center;
  font-family: "Noto Sans KR", sans-serif;
  color: black;
}
.td4 {
  width: 15%;
  vertical-align: middle;
  border-collapse: collapse;
  text-align: center;
  font-family: "Noto Sans KR", sans-serif;
}
.td5 {
  width: 15%;
  vertical-align: middle;
  border-collapse: collapse;
  text-align: center;
  font-family: "Noto Sans KR", sans-serif;
}
</style>
