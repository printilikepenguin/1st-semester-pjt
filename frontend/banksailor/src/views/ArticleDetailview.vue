<template>
  <div class="titlepart-detail">
    <h1 class="title-detail">게시판</h1>
  </div>

  <div class="container-detail">
    <div v-if="article"> 

      <div v-if="currentState"> <!-- 게시글 일반 화면 -->
        <div class="article-head">
          <p class="article-title">{{ article.title }}</p>
          <div style="display: flex; justify-content: space-between;">
            <p style="border-left: solid 5px orange; padding-left: 30px; font-family: 'Noto Sans KR', sans-serif; color: gray;">{{ article.category }}</p>
            <p style="font-family: 'Noto Sans KR', sans-serif; color: gray;">{{ article.username }}, {{ article.created_at.substring(0, 10) }}</p>
          </div>
        </div>
        <div class="article-content">
          <p>{{ article.content }}</p>
        </div>
      </div>

      <div v-else> <!-- 수정화면 -->
        <form @submit.prevent="editArticle" class="customform">
          
          <div class="form-group">
            카테고리:
            <select v-model="article.category">
              <option
                v-for="category in categoryList"
                :key="category.id"
                :value="article.category"
              >
                {{ category.value }}
              </option>
            </select>
          </div>

          <div class="form-group">
            <label for="title" class="form-label">제목:</label>
            <input type="text" v-model="article.title" class="form-control"/>
          </div>

          <div class="form-group">
            <label for="content" class="form-label">내용:</label>
            <textarea type="text" v-model="article.content" class="form-control form-control-textarea"></textarea>
          </div>

          <button v-show="!currentState">완료</button>
          <button @click="$router.go(0)" style="margin-left: 2%;">취소</button>
        </form>
      </div>
    </div> <!-- v-if article-->
    
    <div class="buttons">
      <div v-if="article && article.username === userInfo.username" style="margin: 2%;">
        <button v-show="currentState" @click="onClickEvent()">수정</button>&nbsp;
        <button @click="deleteArticle()">삭제</button>
      </div>
      <button @click="moveToList()" style="margin: 2%;">목록</button>
    </div>
    
    <div>
      <CommentList :article="article" />
    </div>
  
  </div> <!-- container-detail -->

</template>

<script setup>
import axios from "axios";
import { onMounted, ref, inject } from "vue";
import { useCounterStore } from "@/stores/counter";
import { useRouter, useRoute } from "vue-router";
import CommentList from "@/components/ArticleViewComponents/CommentList.vue";

const store = useCounterStore();
const route = useRoute();
const router = useRouter();
const article = ref(null);
const title = ref(null);
const content = ref(null);
const category = ref(null);
const userInfo = store.userInfo;
const currentState = ref(true);
const comments_content = ref(null);
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

onMounted(() => {
  store.getComments(),
    axios({
      method: "get",
      url: `${store.API_URL}/articles/articles/${route.params.id}/`,
    })
      .then((res) => {
        // console.log(res.data)
        article.value = res.data;
        // console.log(article);
      })
      .catch((err) => {
        console.log(err);
      });
});

const moveToList = () => {
  router.push({ name: "article" });
};

const onClickEvent = () => {
  currentState.value = !currentState.value;
};

const editArticle = function () {
  currentState.value = !currentState.value;
  axios({
    method: "put",
    url: `${store.API_URL}/articles/articles/${route.params.id}/`,
    data: {
      title: article.value.title,
      content: article.value.content,
      category: article.value.category,
    },
  })
    .then((res) => {
      currentState.value = true;
    })
    .catch((error) => {
      console.log(error);
    });
};

const deleteArticle = function (request, article_pk) {
  axios({
    method: "delete",
    url: `${store.API_URL}/articles/articles/${route.params.id}/`,
  })
    .then((res) => {
      console.log("삭제완");
      alert("삭제 시 복구되지 않습니다.");
      router.push({ name: "article" });
    })
    .catch((err) => {
      console.log(err);
    });
};
</script>

<style scoped>
.container-detail {
  margin: 0 auto;
  padding: 5%;
  width: 80%;
  background-color: white;;
  box-shadow: 5px 5px 10px 5px lightgray;
  border-radius: 20px;
  margin-bottom: 50px;
  padding-bottom: 50px;
}
.titlepart-detail {
  width: 100%;
  height: 200px;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 30px;
  border-bottom: 2px solid lightgray;
  /* border-bottom: 2px solid hsl(216, 100%, 26%); */
}
.title-detail {
  margin-top: 40px;
  font-size: 3rem;
  font-weight: 400;
  font-family: 'Noto Sans KR', sans-serif;
  color: rgb(0, 53, 133);
}
.article-title {
  width: 90%;
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 2.5rem;
  font-weight: 600;
  margin-top: 50px;
  color: rgb(0, 53, 133);
  padding-left: 30px;
}
.article-content {
  padding-top: 10%;
  padding-bottom: 10%;
  font-family: 'Noto Sans KR', sans-serif;
  font-size: larger;
}
.buttons {
  display: flex;
  justify-content: right;
}

.header p {
  display: inline;
  margin-right: 10px;
}

.main {
  margin: 20px;
  font-size: 1rem;
  line-height: 1.6;
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

.comment-box {
  margin: 20px;
}

textarea {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  resize: vertical;
}

input[type="submit"] {
  padding: 8px 16px;
  background-color: #1c5f82;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

input[type="submit"]:hover {
  background-color: #144362;
}

button {
  border: solid 3px rgb(233, 201, 142);
  border-radius: 30px;
  padding-bottom: 4px;
  width: 80px;
  height: 35px;
  color: black;
  background-color: rgb(233, 201, 142);
  font-family: 'Noto Sans KR', sans-serif;
}
button:hover {
  background-color: #4db7e5;
  border: solid 3px #4db7e5;
}
</style>
