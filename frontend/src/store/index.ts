import { createStore } from 'vuex';

export default createStore({
  state: {
    token: '',
    access_token: '',
    refresh_token: '',
    isAuthenticated: false,
    activeUser: '',
    isPremium: false,
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('access_token')) {
        state.access_token = String(localStorage.getItem('access_token'));
        state.isAuthenticated = true;
      } else {
        state.access_token = '';
        state.isAuthenticated = false;
      }
      if (localStorage.getItem('refresh_token')) {
        state.refresh_token = String(localStorage.getItem('access_token'));
      } else {
        state.refresh_token = '';
      }
    },
    // token is set when user signs in
    setToken(state, token) {
      state.token = token;
      state.isAuthenticated = true;
    },
    removeToken(state) {
      state.token = '';
      state.isAuthenticated = false;
    },
  },
  actions: {
  },
  modules: {
  },
});
