import { createRouter, createWebHashHistory } from 'vue-router' // Change to hash history
import Home from '../components/Home.vue'
import NotFound from '../components/sections/NotFound.vue'

const routes = [
  {
    path: '/', // Remove array, use a single path
    name: 'Home',
    component: Home,
    meta: { scrollSections: true }
  },
  {
    path: '/:pathMatch(.*)*', // Catch-all for 404s
    name: 'NotFound',
    component: NotFound
  }
]

const router = createRouter({
  history: createWebHashHistory(process.env.NODE_ENV === "production" ? "/vue-fastapi-portfolio-website/" : "/"), // Use hash mode
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (to.hash) {
      return {
        el: to.hash,
        behavior: 'smooth',
        top: 100 // Offset for fixed header
      }
    }
    return savedPosition || { top: 0 }
  }
})

export default router
