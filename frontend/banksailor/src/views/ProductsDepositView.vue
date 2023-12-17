<template>
  <div class="maincontent">
    <div class="sidebar">
      <ProductsDepositSearch
        :bank-list="bankList"
        @sendSelectedBank="handleSelectedBank"
      />
    </div>
    <div class="content">
      <ProductsDepositList :selected-bank="selectedBank" />
    </div>
  </div>
</template>

<script setup>
import { ref, watchEffect } from "vue";
import { useCounterStore } from "@/stores/counter";
import ProductsDepositList from "../components/ProductViewComponents/ProductsDepositList.vue";
import ProductsDepositSearch from "../components/ProductViewComponents/ProductsDepositSearch.vue";

const bankList = ref([]);
const selectedBank = ref("");
const store = useCounterStore();

// 은행명 리스트 생성하기
const getBankList = () => {
  for (let prdt of store.deposits) {
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
