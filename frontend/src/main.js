import { createApp } from 'vue';
import App from './App.vue';
// import '../src/assets/styles/tailwind.css'; // Ensure Tailwind CSS is imported
import router from './router';
import './assets/styles/style.css';

createApp(App)
  .use(router)
  .mount('#app');