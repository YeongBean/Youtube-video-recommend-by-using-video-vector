import Vue from 'vue';
import VueRouter from 'vue-router';
import axios from 'axios';
import Home from '../views/Home.vue';

Vue.prototype.$axios = axios;
const apiRootPath = process.env.NODE_ENV !== 'production'
  ? 'http://localhost:8000/api/'
  : '/api/';
Vue.prototype.$apiRootPath = apiRootPath;
axios.defaults.baseURL = apiRootPath;

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
