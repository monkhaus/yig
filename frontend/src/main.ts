import { createApp } from 'vue';
import axios from 'axios';
import App from './App.vue';
import './registerServiceWorker';
import router from './router';
import store from './store';

// axios.defaults.baseURL = 'https://api.youtubeideagenerator.com/'
axios.defaults.baseURL = 'http://0.0.0.0:8000';

createApp(App).use(store).use(router, axios).mount('#app');
