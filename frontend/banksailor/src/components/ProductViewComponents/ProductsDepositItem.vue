<template>
  <div class="record">
    <div class="box1">{{ product.dcls_month }}</div>
    <div class="box2">{{ product.kor_co_nm }}</div>
    <div class="box3"><a href='#' @click.prevent="goDetail">{{ product.fin_prdt_nm }}</a></div>
    <div class="box4">{{ product.rate_6 }}</div>
    <div class="box5">{{ product.rate_12 }}</div>
    <div class="box6">{{ product.rate_24 }}</div>
    <div class="box7">{{ product.rate_36 }}</div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router';

const props = defineProps({
  product: Object
})

const router = useRouter()

const product = ref(props.product)

const goDetail = () => {
  router.push({ name: 'depositdetail', params: { id: product.value.fin_prdt_cd } })
}



</script>

<style scoped>
  .record {
    width: 100%;
    height: 50px;
    border-bottom: 1px solid lightgray;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    transition: background-color 0.1s;
  }

  .box1 {
    width: 10%;
    text-align: center;
  }

  .box2 {
    width: 18%;
    text-align: center; 
  }

  .box3 {
    width: 32%;
    text-align: center; 
  }

  .box4 {
    width: 10%;
    text-align: center; 
  }

  .box5 {
    width: 10%;
    text-align: center; 
  }

  .box6 {
    width: 10%;
    text-align: center; 
  }

  .box7 {
    width: 10%;
    text-align: center; 
  }

  a {
    color: black;
  }

  .record:hover {
  background-color: rgb(255, 245, 191);
  }

</style>