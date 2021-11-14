import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/show/:name',
    name: 'Home',
    component: Home,
  },
  {
    path: '/sender/:name',
    name: 'Sender',
    component: () => import(/* webpackChunkName: "sender" */ '../views/Sender.vue'),
  },
];

const router = new VueRouter({
  base: '/v3',
  routes,
});

export default router;
