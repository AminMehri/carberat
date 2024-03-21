import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import ArticlesView from '../views/ArticlesView.vue'
import SingleArticleView from '../views/SingleArticleView.vue'
import PathNotFound from '../views/PathNotFound.vue'


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView
  },
  {
    path: '/articles',
    name: 'articles',
    component: ArticlesView
  },
  {
    path: '/article/:slug',
    name: 'single-article',
    component: SingleArticleView
  },
  {
    path: '/:pathMatch(.*)*', 
    name: 'not_found',
    component: PathNotFound
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
