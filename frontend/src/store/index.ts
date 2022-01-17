import { createStore } from 'vuex';

export default createStore({
  state: {
    token: '',
    isAuthenticated: false,
    activeUser: '',
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('token')) {
        state.token = String(localStorage.getItem('token'));
        state.isAuthenticated = true;
      } else {
        state.token = '';
        state.isAuthenticated = false;
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
