import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/sender',
    name: 'Sender',
    component: () => import(/* webpackChunkName: "sender" */ '../views/Sender.vue'),
  },
];

const router = new VueRouter({
  base: '/3',
  routes,
});

export default router;
