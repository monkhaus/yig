import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import store from '../store';
import Home from '../views/Home.vue';
import About from '../views/About.vue';
import Collection from '../views/Collection.vue';
import LogIn from '../views/LogIn.vue';
import Play from '../views/Play.vue';
import Sync from '../views/Sync.vue';
import How from '../views/How.vue';
import Success from '../views/Success.vue';

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
    component: About,
  },
  {
    path: '/how',
    name: 'How',
    component: How,
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
    path: '/collection',
    name: 'Collection',
    component: Collection,
    meta: {
      requireLogin: true,
      title: 'Collection',
    },
  },
  {
    path: '/success',
    name: 'Success',
    component: Success,
    meta: {
      requireLogin: true,
      title: 'Success',
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
