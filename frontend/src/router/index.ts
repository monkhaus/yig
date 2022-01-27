import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import store from '../store';
import Home from '../views/Home.vue';
import SignUp from '../views/SignUp.vue';
import LogIn from '../views/LogIn.vue';
import Play from '../views/Play.vue';
import Sync from '../views/Sync.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: {
      title: 'Home',
    },
  },
  {
    path: '/about',
    name: 'About',
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp,
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn,
  },
  {
    path: '/sync',
    name: 'Sync',
    component: Sync,
    meta: {
      requireLogin: true,
      title: 'Sync',
    },
  },
  {
    path: '/play',
    name: 'Play',
    component: Play,
    meta: {
      requireLogin: true,
      title: 'Play',
    },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next('/log-in');
  } else {
    next();
  }
});

export default router;
