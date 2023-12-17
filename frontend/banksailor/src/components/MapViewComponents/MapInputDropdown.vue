<template>
  <div class="container1">
    <select class="select" @change="onAddress1Change">
      <option value="null" disabled selected hidden>
        특별시/광역시/도를 선택하세요
      </option>
      <option disabled value="">Please select one</option>
      <option v-for="item in address1" :key="item.code" :value="item.code">
        {{ item.name }}
      </option>
    </select>

    <select class="select" @change="onAddress2Change">
      <option value="null" disabled selected hidden>
        구 / 군을 선택하세요
      </option>
      <option disabled value="">Please select one</option>
      <template v-for="item in address2" :key="item.code">
        <option v-if="item.name != selectedAddress1" :value="item.code">
          {{ item.name.split(" ").pop() }}
        </option>
      </template>
    </select>

    <select class="select" @change="onAddress3Change">
      <option value="null" disabled selected hidden>동을 선택하세요</option>
      <option disabled value="">Please select one</option>
      <template v-for="item in address3" :key="item.code">
        <option
          v-if="item.name != selectedAddress1 + ' ' + selectedAddress2"
          :value="item.code"
        >
          {{ item.name.split(" ").pop() }}
        </option>
      </template>
    </select>

    <select class="select" v-model="selectedBank">
      <option value="null" disabled selected hidden>은행을 선택해주세요</option>
      <option disabled value="">Please select one</option>
      <option v-for="bank in banks" :key="bank">{{ bank }}</option>
    </select>

    <button class="search-btn" @click="sendMapKeyword">검색!</button>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";
import Swal from "sweetalert2";
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
const emit = defineEmits(["sendMapKeyword"]);

const selectedAddress1 = ref(null);
const selectedAddress1Code = ref(null);

const selectedAddress2 = ref(null);
const selectedAddress2Code = ref(null);

const selectedAddress3 = ref(null);
const selectedAddress3Code = ref(null);

const selectedBank = ref(null);

const address1 = ref([]);
const address2 = ref([]);
const address3 = ref([]);

const keyword = ref(null);

onMounted(() => {
  axios({
    method: "get",
    url: "https://grpc-proxy-server-mkvo6j4wsq-du.a.run.app/v1/regcodes?regcode_pattern=*00000000",
  })
    .then((res) => {
      address1.value = res.data.regcodes;
      // console.log(exchangeresult.value);
    })
    .catch((err) => {
      console.log(err);
    });
});

// const currentAreas = ref(address[address1.value] || []);

const onAddress1Change = (event) => {
  address2.value = null;
  address3.value = null;
  selectedBank.value = null;
  selectedAddress1.value = event.target.selectedOptions[0].textContent;
  selectedAddress1Code.value = event.target.value.slice(0, 2);

  axios({
    method: "get",
    url: `https://grpc-proxy-server-mkvo6j4wsq-du.a.run.app/v1/regcodes?regcode_pattern=${selectedAddress1Code.value}*000000`,
  })
    .then((res) => {
      address2.value = res.data.regcodes;
    })
    .catch((err) => {
      console.log(err);
    });
};

const onAddress2Change = (event) => {
  address3.value = null;
  selectedBank.value = null;
  selectedAddress2.value = event.target.selectedOptions[0].textContent;
  selectedAddress2Code.value = event.target.value.slice(0, 4);
  console.log(selectedAddress2.value);
  console.log(selectedAddress2Code.value);
  axios({
    method: "get",
    url: `https://grpc-proxy-server-mkvo6j4wsq-du.a.run.app/v1/regcodes?regcode_pattern=${selectedAddress2Code.value}*`,
  })
    .then((res) => {
      address3.value = res.data.regcodes;
    })
    .catch((err) => {
      console.log(err);
    });
};

const onAddress3Change = (event) => {
  selectedBank.value = null;
  selectedAddress3.value = event.target.selectedOptions[0].textContent;
  selectedAddress3Code.value = event.target.value.slice(0, 4);
};

const banks = [
  "KEB하나은행",
  "SC제일은행",
  "국민은행",
  "신한은행",
  "외환은행",
  "우리은행",
  "한국시티은행",
  "지방은행",
  "경남은행",
  "광주은행",
  "대구은행",
  "부산은행",
  "전북은행",
  "제주은행",
  "특수은행",
  "기업은행",
  "농협",
  "수협",
  "한국산업은행",
  "한국수출입은행",
];

const sendMapKeyword = function () {
  if (
    selectedAddress1.value == null ||
    selectedAddress2.value == null ||
    selectedAddress3.value == null ||
    selectedBank.value == null
  ) {
    Toast.fire({
      icon: "warning",
      title: "모든 항목을 선택해주세요!",
    });
    return;
  } else {
    keyword.value =
      selectedAddress1.value +
      selectedAddress2.value +
      selectedAddress3.value +
      selectedBank.value;
    emit("sendMapKeyword", keyword.value);
  }
};
</script>

<style scoped>
.container1 {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  margin-right: 50px;
}

.select {
  margin: 10px;
  padding: 8px;
  border: 1px solid #4db7e5;
  border-radius: 5px;
  background-color: white;
  color: #1c5f82;
}

.search-btn {
  margin-top: 10px;
  border: none;
  border-radius: 5px;
  background-color: rgb(7, 152, 242);
  color: white;
  cursor: pointer;
  margin-left: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.search-btn:hover {
  background-color: rgb(17, 132, 222);
  font-weight: 700;
  color: white;
}
</style>
