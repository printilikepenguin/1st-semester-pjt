<template>
  <div class="gradation"></div>
  <div class="containerbody">
    <NewHome />
  </div>
</template>

<script setup>
import { useCounterStore } from "@/stores/counter";
import { onMounted } from "vue";
import NewHome from "@/components/HomeViewComponents/NewHome.vue";

const store = useCounterStore();

onMounted(() => {
  store.getDeposits;
  store.getSavings;
});
</script>

<style scoped>
.containerbody {
  width: 100%;
  height: 100vh;
  /* margin: 0 auto; */
  background-color: white;
}
</style>
