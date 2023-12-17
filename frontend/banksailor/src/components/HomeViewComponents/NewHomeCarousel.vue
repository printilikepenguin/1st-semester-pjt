<template>
  <Carousel class="custom-carousel" v-bind="settings">
    <Slide v-for="img in imgLinks" :style="{ height }">
      <div class="carousel__item">
        <img :src="img" alt="" style="width: 100%; height: 100%; object-fit: cover;" />
      </div>
    </Slide>

    <template #addons>
      <Navigation />
    </template>
  </Carousel>
</template>

<script setup>
// npm install vue3-carousel
import { Carousel, Slide, Navigation } from "vue3-carousel";
import "vue3-carousel/dist/carousel.css";
import { imgLinks } from "../../constants/imgLinks";

const settings = {
  snapAlign: "center",
  itemsToShow: 1,
  wrapAround: true,
  autoplay: 2500,
};
const height = "100%";
</script>

<style>
.carousel__item {
  min-height: 500px;
  background-color: rgb(28, 54, 89);
  width: 100%;
  height: 100%;
  color: white;
  font-size: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 10px;
}

section {
  height: 100%;
}
.carousel__viewport {
  width: 100%;
  height: 100%;
  overflow: hidden;
}

.carousel__viewport .carousel__track {
  height: 100%;
  width: 100%;
}

.carousel__track .carousel__slide {
  height: 100%;
  width: 100%;
  flex-shrink: 0;
}

.carousel__next {
  box-sizing: content-box;
  /* border: 5px solid white; */
}

.carousel__icon {
  stroke: white;
  fill: white;
  transition: 0.3s all;
}

.carousel__icon:hover {
  transform: scale(1.8);
}
/* .carousel__slide {
  padding: 0px;
} */
</style>
