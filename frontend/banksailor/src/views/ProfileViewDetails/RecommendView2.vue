<template>
  <div class="container1">
    <div class="container1">
      <p>
        당신과 같은 20대 {{ myPortfolio[0].saving_style }} 유저는 이런 상품을
        선택했어요~!
      </p>

      <div v-for="recommend in recommend_list">
        <div class="line-box">
          <RouterLink
            :to="{
              name: 'savingdetail',
              params: { id: recommend.fin_prdt_cd },
            }"
          >
            {{ recommend.kor_co_nm }} - {{ recommend.fin_prdt_nm }}
          </RouterLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";
import { useCounterStore } from "@/stores/counter";
import { useRouter } from "vue-router";
import axios from "axios";

const store = useCounterStore();
const userInfo = store.userInfo;
const portfolio = store.portfolio;
const myPortfolio = computed(() => {
  return portfolio.filter((item) => item.user === userInfo.id);
});
const recommend_list = ref([]);

let like_saving = ""; // 변수를 바깥에서 선언
if (store.userInfo.like_saving.length === 0) {
  like_saving = "00266451"; //
} else {
  like_saving = store.userInfo.like_saving[0].fin_prdt_cd;
}

onMounted(() => {
  recommend();
});

const recommend = function () {
  if (myPortfolio.value.length > 0) {
    const saving_style = myPortfolio.value[0].saving_style; // 첫 번째 요소의 saving_style 가져오기

    axios({
      method: "post",
      url: `${store.API_URL}/products/iwillrecommendyou/`,
      data: {
        age: userInfo.age,
        salary: userInfo.salary,
        money: userInfo.money,
        saving_style: saving_style,
        like_saving: like_saving,
      },
      headers: {
        Authorization: `Token ${store.token}`,
      },
    })
      .then((res) => {
        console.log(res.data);
        recommend_list.value = res.data;
      })
      .catch((error) => {
        console.log(error);
      });
  }
};
</script>

<style scoped>
.container1 {
  width: 70%;
  background-color: white;
  border-radius: 30px;
}
</style>
