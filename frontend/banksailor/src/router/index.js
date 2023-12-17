import { createRouter, createWebHistory } from "vue-router";
import { useCounterStore } from "@/stores/counter";
import HomeView from "../views/HomeView.vue";
import ProductsView from "../views/ProductsView.vue";
import MapView from "../views/MapView.vue";
import ExchangeView from "../views/ExchangeView.vue";
import ArticleView from "../views/ArticleView.vue";
import ArticleCreateView from "@/views/ArticleCreateView.vue";
import ArticleDetailView from "@/views/ArticleDetailView.vue";
import ProductsDepositView from "@/views/ProductsDepositView.vue";
import ProductsSavingView from "@/views/ProductsSavingView.vue";
import ProductsDepositDetailView from "@/views/ProductsDepositDetailView.vue";
import ProductsSavingDetailView from "@/views/ProductsSavingDetailView.vue";
import SignUpView from "@/views/SignUpView.vue";
import LogInView from "@/views/LogInView.vue";
import ProductsDepositDetailUpdateView from "@/views/ProductsDepositDetailUpdateView.vue";
import ProfileView from "@/views/ProfileView.vue";
import EditInfoView from "@/views/ProfileViewDetails/EditInfoView.vue";
import EditProfileView from "@/views/ProfileViewDetails/EditProfileView.vue";
import RecommendView from "@/views/ProfileViewDetails/RecommendView.vue";
import ProductsSavingDetailUpdateView from "@/views/ProductsSavingDetailUpdateView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "main",
      component: HomeView,
    },
    {
      path: "/home",
      name: "home",
      component: HomeView,
    },
    {
      path: "/products",
      name: "products",
      component: ProductsView,
      children: [
        {
          path: "/deposit",
          name: "deposit",
          component: ProductsDepositView,
        },
        {
          path: "/saving",
          name: "saving",
          component: ProductsSavingView,
        },
      ],
    },
    {
      path: "/map",
      name: "map",
      component: MapView,
    },
    {
      path: "/exchange",
      name: "exchange",
      component: ExchangeView,
    },
    {
      path: "/article",
      name: "article",
      component: ArticleView,
    },
    {
      path: "/create",
      name: "ArticleCreateView",
      component: ArticleCreateView,
    },
    {
      path: "/article/:id",
      name: "ArticleDetailView",
      component: ArticleDetailView,
    },
    {
      path: "/deposit/:id",
      name: "depositdetail",
      component: ProductsDepositDetailView,
    },
    {
      path: "/saving/:id",
      name: "savingdetail",
      component: ProductsSavingDetailView,
    },
    {
      path: "/signup",
      name: "SignUpView",
      component: SignUpView,
    },
    {
      path: "/login",
      name: "LogInView",
      component: LogInView,
    },
    {
      path: "/profile",
      name: "ProfileView",
      component: ProfileView,
      children: [
        {
          path: "/editinfo",
          name: "editinfo",
          component: EditInfoView,
        },
        {
          path: "/editprofile",
          name: "editprofile",
          component: EditProfileView,
        },
        {
          path: "/recommend",
          name: "recommend",
          component: RecommendView,
        },
      ],
    },
    {
      path: "/deposit/:id/:rate",
      name: "depositrateupdate",
      component: ProductsDepositDetailUpdateView,
    },
    {
      path: "/saving/:id/:rate",
      name: "savingrateupdate",
      component: ProductsSavingDetailUpdateView,
    },
  ],
});

router.beforeEach((to, from) => {
  const store = useCounterStore();
  if (to.name === "ArticleView" && !store.isLogin) {
    window.alert("로그인이 필요합니다.");
    return { name: "LogInView" };
  }
  if ((to.name === "SignUpView" || to.name === "LogInView") && store.isLogin) {
    window.alert("이미 로그인 했습니다.");
    return { name: "ArticleView" };
  }
  if (
    (to.name === "recommend" ||
      to.name === "editprofile" ||
      to.name === "editinfo" ||
      to.name === "ProfileView") &&
    !store.isLogin
  ) {
    window.alert("로그인이 필요합니다.");
    return { name: "LogInView" };
  }
});

export default router;
