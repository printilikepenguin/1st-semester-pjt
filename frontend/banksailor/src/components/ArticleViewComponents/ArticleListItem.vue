<template>
  <tbody class="tbody3">
    <td class="td1">{{ article.id }}</td>
    <td class="td2">{{ article.category }}</td>
    <td class="td3">
      <RouterLink
        :to="{ name: 'ArticleDetailView', params: { id: article.id } }" class="custom-link"
      >
        <p>{{ article.title }}</p>
      </RouterLink>
    </td>
    <td class="td4">
      <p>{{ article.username }}</p>
    </td>
    <td class="td5">{{ article.created_at.slice(0,10) }}</td>
  </tbody>
</template>


<script setup>
import { useCounterStore } from "@/stores/counter";
import { RouterLink } from "vue-router";

const store = useCounterStore();
defineProps({
  article: Object,
});
</script>


<style scoped>
.tbody3 {
  vertical-align: middle;
  border-bottom: 1px solid darkgray;
}

/* .tbody3:last-child {
  border-bottom: 2px solid black;
} */


/* .table>:not(:first-child) {
  border-bottom: 1px solid black;
} */
.td1 {
  width: 10%;
  vertical-align: middle;
  border-collapse: collapse;
  text-align: center;
  font-family: 'Noto Sans KR', sans-serif; 
}
.td2 {
  width: 15%;
  vertical-align: middle;
  border-collapse: collapse;
  text-align: center;
  font-family: 'Noto Sans KR', sans-serif; 
}
.td3 {
  width: 45%;
  vertical-align: middle;
  border-collapse: collapse;
  text-align: center;
  font-family: 'Noto Sans KR', sans-serif; 
}
.td4 {
  width: 15%;
  vertical-align: middle;
  border-collapse: collapse;
  text-align: center;
  font-family: 'Noto Sans KR', sans-serif; 
}
.td5 {
  width: 15%;
  vertical-align: middle;
  border-collapse: collapse;
  text-align: center;
  font-family: 'Noto Sans KR', sans-serif; 
}
.custom-link {
  font-weight: 500;
  color: black;
  text-decoration: underline;
}
</style>