<template>
  <div class="searchbar-content">
    <div class="type">
      <h4>정기예금</h4>
    </div>
    <p>은행 목록</p>
    <select v-model="selectedBank">
      <option disabled value="">원하시는 은행을 선택하세요</option>
      <option>전체</option>
      <option v-for="bank in bankList" :key="bank">{{ bank }}</option>
    </select>
    <br />
    <br />
    <button class="searchbutton" @click="buttonClick">검색</button>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

const selectedBank = ref("");

const props = defineProps({
  bankList: Array,
});

const router = useRouter();

const emit = defineEmits(["sendSelectedBank"]);
const buttonClick = () => {
  emit("sendSelectedBank", selectedBank.value);
  router.push({ name: "deposit" });
};
</script>

<style scoped>
.searchbar-content {
  margin: 50px;
  width: 80%;
  height: 98%;
  border-right: 1px solid rgb(0, 53, 133);
  padding-right: 10%;
}

.type {
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 900;
  color: rgb(0, 53, 133);
  border-left: 3px solid rgb(0, 53, 133);
  padding-left: 10px;
}

p {
  margin: 0;
  margin-top: 40px;
  margin-bottom: 10px;
  font-family: 'Noto Sans KR', sans-serif;
}

.searchbutton {
  border: none;
  border-radius: 5px;
  background-color: rgb(0, 53, 133);
  color: white;
  cursor: pointer;
  font-family: 'Noto Sans KR', sans-serif;
  transition: background-color 0.1s ease, font-weight 0.1s ease;
}

.searchbutton:hover {
  background-color: rgb(0, 70, 175);
  font-weight: 600;
  color: white;
  font-family: 'Noto Sans KR', sans-serif;
}

select {
  width: 100%;
}

</style>
