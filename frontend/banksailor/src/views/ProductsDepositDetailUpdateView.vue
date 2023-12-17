<template>
  <main>
    <div class="linkbar">
      <a href="#" @click.prevent="goBack">뒤로가기</a>
    </div>
    <div class="titlepart">
      <h1 class="title">금리정보 수정</h1>
    </div>
    <div class="detail-content">
      <div class="info-list">
        <div class="info">
          <div class="info-title">
            현재 금리
          </div>
          <div class="info-content">
            {{ this.$route.query.rateValue ? this.$route.query.rateValue : '없음' }}
          </div> 
        </div>
        <div class="info">
          <div class="info-title">
            수정 금리 입력
          </div>
          <div class="info-content">
            <form @submit.prevent="updateRate">
              <input type="number" step="0.0001" id="newRate" v-model="newRate">
              <input type="submit" value="수정" class="submit-button">
            </form >
          </div> 
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios'
import { useCounterStore } from "@/stores/counter";


const router = useRouter()
const route = useRoute()
const store = useCounterStore()

const newRate = ref(null)

const sendMail = () => {
  axios({
    method: 'get',
    url: `${store.API_URL}/products/email/`,
    params: {
      prdtCode: route.params.id,
      oldRate: route.query.rateValue,
      newRate: newRate.value,
      period: route.params.rate
    }
  })
    .then((response) => {
      console.log(response)
    })
    .catch((error) => {
      console.log(error)
    })
}

const updateRate = () => {
  axios({
    method: "put",
    url: `${store.API_URL}/products/deposit/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
    data: {
      rate: newRate.value,
      rateType: route.params.rate
    }
  })
    .then((response) => {
      alert('금리가 수정되었습니다.');
      store.getDeposits()
      sendMail()
      router.push({ name: 'depositdetail', params: { id: route.params.id }})
    })
    .catch((error) => {
      console.log(error);
    });
};




const goBack = () => {
  router.push({ name: 'depositdetail', params: { id: route.params.id } } )
}  
</script>

<style scoped>

main {
  width: 100%;
  display: flex;
  flex-direction: column;
  /* margin-bottom: 10px; */
}

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
  font-family: 'Noto Sans KR', sans-serif;
  color: rgb(0, 53, 133);
}

.linkbar {
  margin-left: 20px;
}


.linkbar a {
  font-family: 'Noto Sans KR', sans-serif;
  color: black;
  text-decoration: none;
}

.detail-content {
  width: 80%;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  background-color: white;;
  box-shadow: 5px 5px 10px 5px lightgray;
  border-radius: 20px;
  margin-bottom: 600px;

}

.info-list {
  display: flex;
  flex-direction: column;
  margin: 50px;
  margin-bottom: 25px;
}

.info {
  padding-top: 15px;
  padding-bottom: 15px;
  display: flex;
  flex-direction: row;
  border-bottom: 1px solid lightgray;
}

.info-title {
  width: 20%;
  font-family: 'Noto Sans KR', sans-serif;
  font-weight: 500;
}
.info-content {
  width: 80%;
  font-family: 'Noto Sans KR', sans-serif;
}

.submit-button {
  font-family: 'Noto Sans KR', sans-serif;
  background-color: rgb(0, 53, 133);
  color: white;
  transition: background-color 0.1s ease;
  margin-left: 1rem;
}

.submit-button:hover {
  background-color: rgb(0, 70, 175);
}

</style>