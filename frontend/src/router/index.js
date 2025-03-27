import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/Home.vue'
import NotFound from '../components/sections/NotFound.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: { scrollSections: true } // Enable section scrolling
  },
  {
    path: '/:pathMatch(.*)*', // Catch all 404s
    name: 'NotFound',
    component: NotFound
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    // Handle hash links (section scrolling)
    if (to.hash) {
      return {
        el: to.hash,
        behavior: 'smooth',
        top: 100 // Offset for fixed header
      }
    }
    // Return to saved position or top
    return savedPosition || { top: 0 }
  }
})

export default router