import { createRouter, createWebHistory } from "vue-router";
import Home from "./views/Home.vue";
import ProductForm from "./components/ProductForm.vue";
import ProductList from "./components/ProductList.vue";

const routes = [
    { path: "/", component: Home },
    { path: "/add-product", component: ProductForm },
    { path: "/product-list", component: ProductList },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
