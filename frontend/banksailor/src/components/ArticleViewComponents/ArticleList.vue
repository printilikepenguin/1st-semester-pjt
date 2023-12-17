<template>
  <table class="table">
    <thead class="thead">
      <th class="th1">번호</th>
      <th class="th2">분류</th>
      <th class="th3">제목</th>
      <th class="th4">작성자</th>
      <th class="th5">작성일</th>
    </thead>
    <tbody id="notice">
      <td class="td1">-</td>
      <td class="td2">공지</td>
      <td class="td3">무분별한 도배, 욕설, 비방은 무통보 삭제될 수 있습니다</td>
      <td class="td4">항해사</td>
      <td class="td5">2000-00-00</td>
    </tbody>
    <ArticleListItem
      v-for="article in store.articles"
      :key="article.id"
      :article="article"
    />
  </table>
</template>

<script setup>
import { useCounterStore } from "@/stores/counter";
import ArticleListItem from "@/components/ArticleViewComponents/ArticleListItem.vue";

const store = useCounterStore();
</script>

<style scoped>
.table {
  width: 100%;
  border-collapse: collapse;
  text-align: center;
}
.thead {
  height: 50px;
  background-color: rgb(233, 201, 142);
  vertical-align: middle;
  text-align: center;
  font-weight: 300; 
  font-family: 'Noto Sans KR', sans-serif; 
  font-size: larger;
}
#notice {
  color: rgb(0, 53, 133);
  text-align: center;
  vertical-align: middle;
  font-weight: 1000;
}
.td1 {
  width: 10%;
  border-collapse: collapse;
  text-align: center;
}
.td2 {
  width: 15%;
  border-collapse: collapse;
  text-align: center;
}
.td3 {
  width: 45%;
  border-collapse: collapse;
  text-align: center;
}
.td4 {
  width: 15%;
  border-collapse: collapse;
  text-align: center;
}
.td5 {
  width: 15%;
  border-collapse: collapse;
  text-align: center;
}
</style>