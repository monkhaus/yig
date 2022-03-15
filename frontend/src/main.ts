import { createApp } from 'vue';
import axios from 'axios';
import App from './App.vue';
import './registerServiceWorker';
import router from './router';
import store from './store';


let gAuthClientId = '910584800498-v7b3bnrgkm3tk6tqm7lfv5554mdlm36q.apps.googleusercontent.com';

// axios.defaults.baseURL = 'https://api.videoideagenerator.com/'
axios.defaults.baseURL = 'http://0.0.0.0:8000/';


createApp(App).use(store).use(router, axios).mount('#app');
