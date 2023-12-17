<template>
  <div class="container-main">
    <!-- <h1>The World's Best Financial Site</h1> -->
    <div class="boxes">
      <div class="carousel1">
        <NewHomeCarousel />
      </div>
      <div class="sidebox">
        <div class="box1" @click="goExchange">
          <img src="/src/assets/currency-icon.png" alt="" class="icon ms-4" />
          <div class="exchange me-4">
            <img src="/src/assets/arrow.png" alt="" width="60" />
            <h3>환율 정보</h3>
          </div>
        </div>
        <div class="box2" @click="goMap">
          <img src="/src/assets/map-icon.png" alt="" class="icon ms-4" />
          <div class="map me-4">
            <img src="/src/assets/arrow.png" alt="" width="60" />
            <h3>내 근처 은행</h3>
          </div>
        </div>
      </div>
    </div>
    <HomeLinkBar class="HomeLinkBar"/>
  </div>
</template>

<script setup>
import NewHomeCarousel from "./NewHomeCarousel.vue";
import HomeLinkBar from "./HomeLinkBar.vue";
import { useRouter } from "vue-router";

const router = useRouter();

const goExchange = () => {
  router.push({ name: "exchange" });
};

const goMap = () => {
  router.push({ name: "map" });
};
</script>

<style scoped>
/* h1 {
  margin-bottom: 50px;
  color: rgb(28, 54, 89);
} */

.boxes {
  /* background-color: pink; */
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  column-gap: 20px;
  width: 100%;
  height: 500px;
  margin-bottom: 60px;
}

.carousel1 {
  background-color: lavender;
  flex: 2;
  height: 100%;
  overflow: hidden;
  box-shadow: 5px 5px 5px 1px lightgray;
}

.sidebox {
  display: flex;
  flex-direction: column;
  width: 20%;
  height: 100%;
  row-gap: 20px;
}
.box1,
.box2 {
  flex: 1;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 5px 5px 5px 1px lightgray;
}

.box1 {
  background-color: rgb(1, 66, 163);
  color: rgb(139, 139, 139);
}

.box2 {
  flex: 1;
  background-color: rgb(159, 159, 155);
}

.exchange h3 {
  font-family: "Noto Sans KR", sans-serif;
}

.map h3 {
  font-family: "Noto Sans KR", sans-serif;
}

.boxes div {
  border-radius: 20px;
  transition: 0.2s all;
}

.box1:hover {
  background-color: rgb(0, 53, 133);
  transform: scale(1.02);
  color: white;
  cursor: pointer;
}

.box2:hover {
  color: white;
  transform: scale(1.02);
  background-color: rgb(136, 136, 134);
  cursor: pointer;
}

.icon {
  width: 45%;
  /* height: 50%; */
  transition: 0.3s all;
}

.container-main {
  width: 100%;
  /* height: 600px; */
  padding: 50px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: white;
}

.exchange {
  display: flex;
  flex-direction: column;
  align-items: end;
  row-gap: 10px;
}

.map {
  display: flex;
  flex-direction: column;
  align-items: end;
  row-gap: 10px;
}

.HomeLinkBar {
  margin-top: 70px;
}

</style>
