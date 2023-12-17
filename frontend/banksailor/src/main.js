import piniaPluginPersistedstate from "pinia-plugin-persistedstate";
import { createApp, provide } from "vue";
import { createPinia } from "pinia";
import App from "./App.vue";
import router from "./router";
import VueApexCharts from "vue3-apexcharts";
import VueSweetalert2 from "vue-sweetalert2";
import "sweetalert2/dist/sweetalert2.min.css";

import { defineRule } from "vee-validate";
import { required, email, min } from "@vee-validate/rules";
defineRule("required", required);
defineRule("email", email);
defineRule("min", min);

const app = createApp(App);
const pinia = createPinia();

pinia.use(piniaPluginPersistedstate);
// app.use(createPinia())
app.use(pinia);
app.use(router);
app.use(VueApexCharts);
app.use(VueSweetalert2);
app.mount("#app");
// provide("swal", app.config.globalProperties.$swal);
