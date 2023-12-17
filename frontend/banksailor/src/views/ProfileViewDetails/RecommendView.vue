<template>
  <div class="container2">
    <div v-if="isLoading">
      <div class="loading">
        <FadeLoader :loading="isLoading" />
      </div>
    </div>
    <div v-else>
      <h2 class="title">
        {{ store.userInfo.username }}님과 유사한 사용자들이 많이 가입한 상품들
      </h2>
      <div class="listarea">
        <div class="product-list">
          <h2 class="type">예금</h2>
          <ul>
            <li v-for="deposit in depositList" :key="deposit.id">
              {{ deposit.fin_prdt_nm }}
            </li>
          </ul>
        </div>

        <div class="product-list">
          <h2 class="type">적금</h2>
          <ul>
            <li v-for="saving in savingList" :key="saving.id">
              {{ saving.fin_prdt_nm }}
            </li>
          </ul>
        </div>
      </div>
      <div class="chartarea">
        <h3 class="subtitle">차트</h3>
        <div class="chart1">
          <p class="saving">[예금]</p>
          <RecommendDepositChart :data="depositList" />
        </div>
        <div class="chart1">
          <p class="saving">[적금]</p>
          <RecommendSavingChart :data="savingList" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import RecommendDepositChart from "../../components/ProfileViewComponents/RecommendDepositChart.vue";
import RecommendSavingChart from "../../components/ProfileViewComponents/RecommendSavingChart.vue";
import FadeLoader from "vue-spinner/src/FadeLoader.vue";
import { useCounterStore } from "@/stores/counter";
import { onMounted, ref } from "vue";
import axios from "axios";
const store = useCounterStore();
const isLoading = ref(true);
const depositList = ref([]);
const savingList = ref([]);

onMounted(() => {
  getRecommend();
});

const getRecommend = async function () {
  try {
    isLoading.value = true;
    const response = await axios.post(
      `${store.API_URL}/products/recommend/`,
      null,
      {
        headers: {
          Authorization: `Token ${store.token}`,
        },
      }
    );
    depositList.value = response.data.deposits || [];
    savingList.value = response.data.savings || [];
    isLoading.value = false;
  } catch (error) {
    console.error("Error fetching recommendations:", error);
  } finally {
    isLoading.value = false; // 로딩 완료
  }
};
</script>

<style scoped>
.container2 {
  width: 70%;
  margin-bottom: 2.5%;
  background-color: white;
  border-radius: 30px;
  box-shadow: 5px 5px 10px 5px lightgray;
  height: auto;
  overflow-x: hidden;
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

.loading {
  z-index: 2;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  box-shadow: rgba(0, 0, 0, 0.1) 0 0 0 9999px;
}

.title {
  width: 100%;
  text-align: center;
  margin: 30px 0px;
  font-size: 2rem;
  font-weight: 400;
  font-family: "Noto Sans KR", sans-serif;
  color: rgb(0, 53, 133);
  border-bottom: 1px solid grey;
  padding-bottom: 20px;
}

.listarea {
  display: flex;
  justify-content: space-around;
}

.product-list {
  margin: 20px;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  margin: 8px 0;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
  cursor: pointer;
  text-align: left;
}

.type {
  text-align: center;
}

.chartarea {
  margin-top: 40px;
  width: 100%;
  text-align: center;
  padding: 0px 40px;
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

.chart1 {
  margin-bottom: 40px;
}

.saving {
  font-size: 20px;
  font-weight: 800;
  color: rgb(7, 152, 242);
  background-color: rgb(190, 214, 234);
  padding-bottom: 5px;
}
</style>
