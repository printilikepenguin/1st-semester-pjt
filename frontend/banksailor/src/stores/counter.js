import { ref, computed } from "vue";
import { defineStore } from "pinia";
import { useRouter } from "vue-router";
import axios from "axios";
import Swal from "sweetalert2";

export const useCounterStore = defineStore(
  "counter",
  () => {
    const router = useRouter();
    const articles = ref([]);
    const comments = ref([]);
    const userInfo = ref([]);
    const portfolio = ref([]);
    const API_URL = "http://127.0.0.1:8000";
    const token = ref(null);
    const isLogin = computed(() => {
      if (token.value === null) {
        return false;
      } else {
        return true;
      }
    });
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

    const signUp = function (payload) {
      console.log(payload);
      const {
        username,
        password1,
        password2,
        email,
        nickname,
        age,
        money,
        salary,
      } = payload;

      axios({
        method: "post",
        url: `${API_URL}/accounts/signup/`,
        data: {
          username,
          password1,
          password2,
          email,
          nickname,
          age,
          money,
          salary,
          // financial_products
        },
      })
        .then((res) => {
          const password = password1;
          logIn({ username, password });
        })
        .catch((err) => {
          console.log("??????????");
          console.log(err.json);
        });
    };

    const logIn = function (payload) {
      const { username, password } = payload;

      axios({
        method: "post",
        url: `${API_URL}/accounts/login/`,
        data: {
          username,
          password,
        },
      })
        .then((res) => {
          console.log(res.data);
          token.value = res.data.key;
          getUserInfo();
          router.push({ name: "home" });
        })
        .catch((err) => {
          Toast.fire({
            icon: "error",
            title: "아이디 또는 비밀번호가 일치하지 않습니다",
          });
          console.log(err);
        });
    };

    const logOut = function () {
      axios({
        method: "post",
        url: `${API_URL}/accounts/logout/`,
      })
        .then((res) => {
          token.value = null;
          router.push({ name: "home" });
        })
        .catch((err) => {
          console.log(err);
        });
    };

    const getArticles = function () {
      axios({
        method: "get",
        url: `${API_URL}/articles/articles/`,
        // headers: {
        //   Authorization: `Token ${token}`,
        // },
      })
        .then((res) => {
          console.log(res);
          articles.value = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    };
    //
    const deposits = ref([]);
    const savings = ref([]);

    const getDeposits = () => {
      axios({
        method: "get",
        url: `${API_URL}/products/deposit/`,
      })
        .then((response) => {
          deposits.value = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    };

    const createArticle = function () {
      axios({
        method: "post",
        url: `${API_URL}/articles/articles/`,
      })
        .then((res) => {
          console.log(res.data);
        })
        .catch((error) => {
          console.log(error);
        });
    };

    const getComments = function () {
      axios({
        method: "get",
        url: `${API_URL}/articles/comments/`,
      })
        .then((res) => {
          comments.value = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    };

    const createComments = function () {
      axios({
        method: "post",
        url: `${API_URL}/articles/articles/<int:article_pk>/comments/`,
      })
        .then((res) => {
          console.log(res.data);
        })
        .catch((error) => {
          console.log(error);
        });
    };

    const getSavings = () => {
      axios({
        method: "get",
        url: `${API_URL}/products/saving/`,
      })
        .then((response) => {
          savings.value = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    };

    const getUserInfo = async function () {
      try {
        await axios({
          method: "get",
          url: `${API_URL}/accounts/user/`,
          headers: {
            Authorization: `Token ${token.value}`,
          },
        });

        // getUserInfo 호출 후에 프로필 정보가 업데이트될 때까지 기다림
        await new Promise((resolve) => setTimeout(resolve, 5)); // 적절한 대기 시간 설정

        // 업데이트된 프로필 정보를 가져옴
        const response = await axios({
          method: "get",
          url: `${API_URL}/accounts/user/`,
          headers: {
            Authorization: `Token ${token.value}`,
          },
        });

        userInfo.value = response.data;
        return response.data;
      } catch (error) {
        console.log(error);
      }
    };

    const getPortfolio = function () {
      axios({
        method: "get",
        url: `${API_URL}/accounts/find/input_portfolioData/`,
      })
        .then((res) => {
          portfolio.value = res.data;
          console.log(portfolio);
        })
        .catch((err) => {
          console.log(err);
        });
    };

    return {
      articles,
      API_URL,
      getArticles,
      createArticle,
      createComments,
      getComments,
      deposits,
      getDeposits,
      savings,
      getSavings,
      logIn,
      logOut,
      signUp,
      isLogin,
      token,
      getUserInfo,
      userInfo,
      Toast,
      getPortfolio,
      portfolio,
    };
  },
  { persist: true }
);
