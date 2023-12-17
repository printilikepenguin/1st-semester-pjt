<template>
  <div class="totalcontainer">
    <template v-if="isLoading">
      <div class="loading">
        <FadeLoader :loading="isLoading" />
      </div>
    </template>
    <template v-else>
      <div class="calculatorbody">
        <h4>오늘의 날짜 : {{ now_date }}</h4>
        <div class="container2">
          <div class="exchangearea">
            <div class="inputbox">
              <input type="number" class="priceinput" v-model="price" />
              <select class="select" v-model="fromCountry">
                <option value="null" disabled selected hidden>통화</option>
                <option disabled value="">Please select one</option>
                <option
                  v-for="item in CountriesList"
                  :key="item.id"
                  :value="item.cur_unit"
                >
                  {{ item.cur_unit }}
                  <!-- <option>{{ item.cur_unit }}</option> -->
                </option>
              </select>
            </div>
            <Arrow />
            <div class="inputbox">
              <div class="exchangeresult">
                <div>{{ exchangeresult }}</div>
                <div>₩</div>
              </div>
            </div>
          </div>
          <p>* 엔화/인도네시아 루피아는 100단위, 나머지는 모두 1단위</p>
          <button @click="getExchangeResult" class="search-btn">
            환율 추적
          </button>
        </div>
      </div>

      <div v-if="isshow" class="compare">
        <div class="compare-header">
          <span style="display: inline"
            >오늘과 비교해보고 싶은 날짜를 입력해주세요(기본값 : 어제)</span
          >
          <form @submit.prevent="comparesearch">
            <input type="date" v-model="howlong" />
            <input type="submit" value="Submit" class="diffsearch" />
          </form>
        </div>
        <div class="compare-cards1">
          <div v-for="item in diff" class="card1">
            <div class="card-content">
              <div class="card-item1">{{ item[0] }}</div>
              <div class="card-item1">
                {{ item[1] }}
              </div>
              <div
                class="card-item1"
                :class="{ 'red-text': item[2] > 0, 'blue-text': item[2] < 0 }"
              >
                {{ item[2] }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </template>
  </div>
</template>
<script setup>
import FadeLoader from "vue-spinner/src/FadeLoader.vue";
import { ref, onMounted } from "vue";
import Swal from "sweetalert2";
import axios from "axios";
import { useCounterStore } from "@/stores/counter";
import Arrow from "@/components/ExchangeViewComponents/Arrow.vue";

var now_date = new Date().toISOString().substr(0, 10).replace("T", " ");

const isLoading = ref(false);
const isshow = ref(false);
const store = useCounterStore();
const exchangeresult = ref("");
const fromCountry = ref(null);
const price = ref(null);
const diff = ref(null);
const howlong = ref(null);

var st_date = new Date()
  .toISOString()
  .substr(0, 10)
  .replace("T", " ")
  .replace("-", "")
  .replace("-", "");

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

const getExchangeResult = async function (order) {
  if (price.value == null) {
    Toast.fire({
      icon: "warning",
      title: "금액를 입력해주세요",
    });
    return;
  }
  if (fromCountry.value == null) {
    Toast.fire({
      icon: "warning",
      title: "변환할 통화를 선택해주세요",
    });
    return;
  }
  try {
    isLoading.value = true;
    const response = await axios.get(
      `${store.API_URL}/exchange/currency/${fromCountry.value}/${price.value}/${st_date}/-1`
    );

    if (diff.value == null) {
      exchangeresult.value = response.data.exchangeresult;
      // diff.value = response.data.diff;
    } else {
      exchangeresult.value = response.data.exchangeresult;
      // diff.value = response.data.diff;
      isshow.value = true;
    }
  } catch (error) {
    console.error("Error fetching recommendations:", error);
    Toast.fire({
      icon: "error",
      title: "환율 데이터를 가져오는 중 오류가 발생했습니다",
    });
  } finally {
    isLoading.value = false; // 로딩 완료
  }
};

const selectedCountry1 = (event) => {
  fromCountry.value = event.target.value;
};

onMounted(async () => {
  try {
    isLoading.value = true;
    const response = await axios.get(
      `${store.API_URL}/exchange/currency/KRW/1000/${st_date}/-1`
    );

    diff.value = response.data.diff;
    isshow.value = true;
  } catch (error) {
    console.error("Error fetching recommendations:", error);
    Toast.fire({
      icon: "error",
      title: "환율 데이터를 가져오는 중 오류가 발생했습니다",
    });
  } finally {
    isLoading.value = false; // 로딩 완료
  }
});

const comparesearch = async function () {
  console.log(howlong.value);
  const today = new Date().toISOString().split("T")[0];
  if (howlong.value > today) {
    Toast.fire({
      icon: "error",
      title: "오늘 이후 날짜는 선택할 수 없습니다.",
    });
    howlong.value = "";
    return;
  }

  try {
    isLoading.value = true;
    const response = await axios.get(
      `${store.API_URL}/exchange/currency/KRW/1000/${st_date}/${howlong.value}`
    );

    diff.value = response.data.diff;
    isshow.value = true;
  } catch (error) {
    console.error("Error fetching recommendations:", error);
    Toast.fire({
      icon: "error",
      title: "환율 데이터를 가져오는 중 오류가 발생했습니다",
    });
  } finally {
    isLoading.value = false; // 로딩 완료
  }
};

const CountriesList = [
  { id: 0, cur_unit: "AED" },
  { id: 1, cur_unit: "ATS" },
  { id: 2, cur_unit: "AUD" },
  { id: 3, cur_unit: "BEF" },
  { id: 4, cur_unit: "BHD" },
  { id: 5, cur_unit: "CAD" },
  { id: 6, cur_unit: "CHF" },
  { id: 7, cur_unit: "CNH" },
  { id: 8, cur_unit: "DEM" },
  { id: 9, cur_unit: "DKK" },
  { id: 10, cur_unit: "ESP(100)" },
  { id: 11, cur_unit: "EUR" },
  { id: 12, cur_unit: "FIM" },
  { id: 13, cur_unit: "FRF" },
  { id: 14, cur_unit: "GBP" },
  { id: 15, cur_unit: "HKD" },
  { id: 16, cur_unit: "IDR(100)" },
  { id: 17, cur_unit: "ITL(100)" },
  { id: 18, cur_unit: "JPY(100)" },
  { id: 20, cur_unit: "KWD" },
  { id: 21, cur_unit: "MYR" },
  { id: 22, cur_unit: "NLG" },
  { id: 23, cur_unit: "NOK" },
  { id: 24, cur_unit: "NZD" },
  { id: 25, cur_unit: "SAR" },
  { id: 26, cur_unit: "SEK" },
  { id: 27, cur_unit: "SGD" },
  { id: 28, cur_unit: "THB" },
  { id: 29, cur_unit: "USD" },
  { id: 30, cur_unit: "XOF" },
];
</script>
<style scoped>
h4 {
  margin-bottom: 10px;
}
.totalcontainer {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.calculatorbody {
  width: 80%;
  background-color: white;
  border-radius: 15px;
  padding: 20px 20px;
}

.exchangearea {
  width: 100%;
  height: 90%;
  display: flex;
  justify-content: space-between;
}

.exchangeresult {
  width: 70%;
  display: flex;
  justify-content: space-between;
}

.selectcountry {
  font-size: 120%;
  margin: 0px 10px;
}

.priceinput {
  background-color: transparent;
  border: none;
  width: 70%;
}

.priceinput:focus {
  border-color: blue;
  outline: none;
}

.exchangeicon {
  font-size: 5rem;
  margin: 0px 15px;
}

.exchangeresult {
  width: 70%;
}

p {
  align-self: flex-start;
  width: 100%;
}

input[type="number"]::-webkit-outer-spin-button,
input[type="number"]::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

.search-btn {
  margin-top: 10px;
  border: none;
  width: 100px;
  height: 50px;
  border-radius: 5px;
  background-color: rgb(7, 152, 242);
  color: white;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

.search-btn:hover {
  background-color: rgb(17, 132, 222);
  font-weight: 700;
  color: white;
}

.select {
  width: 70px;
  font-size: 20px;
  border: none;
  background-color: transparent;
}

.card {
  width: 300px;
}

.totalcontainer {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.calculatorbody {
  margin-bottom: 20px;
}

.container2 {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.exchangearea {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 20px;
}

.inputbox {
  display: flex;
  align-items: center;
  margin: 0 20px;
  outline: none;
  width: 45%;
  height: 100%;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
  background-color: rgb(234, 218, 190);
  font-size: 30px;
}

.exchangeresult {
  display: flex;
  align-items: center;
}

.compare {
  width: 80%;
  max-height: 400px;
  overflow-y: scroll;
  background-color: white;
  border-radius: 15px;
  padding: 30px 30px;
  overflow-x: scroll;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.compare-title1 {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 10px;
}

.compare-cards1 {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  padding: 30px 0px;
  overflow: auto;
}

.card1 {
  width: 200px;
  height: 100px;
  background-color: #f5f5f5;
  border-radius: 10px;
  padding: 10px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.card-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.card-item1 {
  font-size: 16px;
  line-height: 1.2;
}

.red-text {
  color: red;
}

.blue-text {
  color: blue;
}

.compare-header {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.diffsearch {
  font-family: "Noto Sans KR", sans-serif;
  background-color: rgb(0, 53, 133);
  color: white;
  transition: background-color 0.1s ease;
  border: none;
  margin-left: 10px;
  border-radius: 5px;
}

.diffsearch:hover {
  background-color: rgb(0, 70, 175);
}
</style>
