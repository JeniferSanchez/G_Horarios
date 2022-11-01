import { createRouter, createWebHashHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'
import HomeView from '../views/HomeView.vue'
import Edit from '../components/Edit.vue'
import editCoor from '../components/editCoor.vue'

const routes = [
  {
    path: '/',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/Inicio',
    name: 'Inicio',
    component: HomeView
  },
  {
    path: '/edit/:doc_cedula',
    name: 'edit',
    component: Edit
  },
  {
    path: '/editCoor/:coor_cedula',
    name: 'editCoor',
    component: editCoor
  },
  {
    path: '/Docente',
    name: 'Docente',
    // route level code-splitting
    // this generates a separate chunk (Docente.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "Docente" */ '../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
