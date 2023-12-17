<template>
  <div>
    <apexchart
      type="bar"
      height="350"
      :options="chartOptions"
      :series="series"
    ></apexchart>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import { useCounterStore } from "@/stores/counter";
import VueApexCharts from "vue3-apexcharts";
const store = useCounterStore();

const saving = ref(store.userInfo.like_saving);
const categories = saving.value.map((item) => item.fin_prdt_nm);

const series = ref([
  { name: "AVG", data: [] },
  { name: "MAX", data: [] },
]);

const avgSeries = series.value.find((item) => item.name === "AVG");
const maxSeries = series.value.find((item) => item.name === "MAX");

for (const item of saving.value) {
  let count = 0;
  let sum = 0;
  if (item.rate_6 !== null) {
    count++;
    sum += item.rate_6;
  }
  if (item.rate_12 !== null) {
    count++;
    sum += item.rate_12;
  }
  if (item.rate_24 !== null) {
    count++;
    sum += item.rate_24;
  }
  if (item.rate_36 !== null) {
    count++;
    sum += item.rate_36;
  }
  const avg = sum / count;
  avgSeries.data.push(avg);

  const data = [];
  if (item.rate_6_max !== null) {
    data.push(item.rate_6_max);
  }
  if (item.rate_12_max !== null) {
    data.push(item.rate_12_max);
  }
  if (item.rate_24_max !== null) {
    data.push(item.rate_24_max);
  }
  if (item.rate_36_max !== null) {
    data.push(item.rate_36_max);
  }
  const max = Math.max(...data);
  maxSeries.data.push(max);
}

const chartOptions = ref({
  chart: {
    type: "bar",
    height: 350,
  },
  plotOptions: {
    bar: {
      horizontal: false,
      columnWidth: "55%",
      endingShape: "rounded",
    },
  },
  dataLabels: {
    enabled: false,
  },
  stroke: {
    show: true,
    width: 2,
    colors: ["transparent"],
  },
  xaxis: {
    categories: categories,
  },
  yaxis: {
    title: {
      text: "금리",
    },
  },
  fill: {
    opacity: 1,
  },
  tooltip: {
    y: {
      formatter: function (val) {
        return val;
      },
    },
  },
});
</script>
