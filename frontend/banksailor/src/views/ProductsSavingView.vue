<template>
  <div class="maincontent">
    <div class="sidebar">
      <ProductsSavingSearch
        :bank-list="bankList"
        @sendSelectedBank="handleSelectedBank"
      />
    </div>
    <div class="content">
      <ProductsSavingList :selected-bank="selectedBank" />
    </div>
  </div>
</template>

<script setup>
import { ref, watchEffect } from "vue";
import { useCounterStore } from "@/stores/counter";
import ProductsSavingList from "../components/ProductViewComponents/ProductsSavingList.vue";
import ProductsSavingSearch from "../components/ProductViewComponents/ProductsSavingSearch.vue";

const bankList = ref([]);
const selectedBank = ref("");
const store = useCounterStore();

// 은행명 리스트 생성하기
const getBankList = () => {
  for (let prdt of store.savings) {
    const bankName = prdt.kor_co_nm;

    // 은행명 중복 검사
    if (!bankList.value.includes(bankName)) {
      bankList.value.push(bankName);
    }
  }
};

watchEffect(() => {
  getBankList();
});

const handleSelectedBank = (bankname) => {
  selectedBank.value = bankname;
};
</script>

<style scoped>
.maincontent {
  display: flex;
  width: 100%;
  justify-content: center;
}

.sidebar {
  width: 25%;
}

.content {
  width: 75%;
}
</style>
