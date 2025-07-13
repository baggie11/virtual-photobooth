// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from '../components/LandingPage.vue'
import PhotoPage from '../components/PhotoPage.vue'
import StylePage from '../components/StylePage.vue'


const routes = [
  { path: '/', name: 'Home', component: LandingPage },
  { path: '/photo', name: 'PhotoPage', component: PhotoPage },
  { path: '/style', name: 'StyleSelector', component: StylePage }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
