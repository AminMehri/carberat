<template>
  <header dir="rtl" class="navbar bg-light" id="header-nav">
    <div class="container-fluid">
      <router-link class="navbar-brand" id="navbar-brand" to="/">
        <img src="../assets/logo192.png" alt="کاربرات" class="img-fluid w-25">
        کاربرات
      </router-link>

      <form class="d-flex w-50" role="search">
        <input class="form-control me-2" type="search" placeholder="جستجو ..." aria-label="Search">
      </form>

      <div>
        <i v-if="!darkMode" @click="changeMode" type="button" class="fas fa-sun text-light fs-4"></i>
        <i v-if="darkMode" @click="changeMode" type="button" class="fa fa-moon fs-4"></i>
      </div>

    </div>
  </header>

  <nav class="navbar navbar-expand-lg bg-light">
    <div class="container-fluid">
      <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar"
        aria-controls="offcanvasNavbar">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">
        <div class="offcanvas-header">
          <h5 class="offcanvas-title ms-auto" id="offcanvasNavbarLabel">
            <img src="../assets/logo192.png" alt="کاربرات" class="img-fluid w-25">
            کاربرات
          </h5>
          <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
        </div>
        <div class="offcanvas-body">
          <ul class="navbar-nav justify-content-end flex-grow-1 pe-3">
            <li class="nav-item">
              <router-link class="nav-link" to="/guide">راهنما</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/about">درباره ما</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/contact">ارتباط با ما</router-link>
            </li>
            <li class="nav-item dropdown">
              <router-link class="nav-link dropdown-toggle" to="/articles" role="button" data-bs-toggle="dropdown"
                aria-expanded="false">
                دانشنامه
              </router-link>
              <ul class="dropdown-menu text-end main-dropdown">
                <li><router-link class="dropdown-item" to="/articles">همه مقالات</router-link></li>

                <li v-for="(cat, index) in categoriesData">
                  <div v-if="!cat.parent" class="accordion accordion-flush" id="accordionFlushExample">
                    <div class="accordion-item">
                      <h2 class="accordion-header" id="flush-headingOne">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                          :data-bs-target="`#flush-collapseOne${index}`" aria-expanded="false" aria-controls="flush-collapseOne">
                          {{cat.title}}
                        </button>
                      </h2>
                      <div :id="`flush-collapseOne${index}`" class="accordion-collapse collapse" aria-labelledby="flush-headingOne"
                        data-bs-parent="#accordionFlushExample">
                        <div class="accordion-body">
                          <li v-for="c in cat.children"><router-link class="dropdown-item" :to="`/category/${c[1]}`">{{c[0]}}</router-link></li>
                        </div>
                      </div>
                    </div>
                  </div>
                </li>

              </ul>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/">خانه</router-link>
            </li>
          </ul>
        </div>

      </div>
    </div>
  </nav>


</template>

<script>
import Swal from 'sweetalert2'
import axios from 'axios'
import { ref } from 'vue'

export default {
  setup() {
    let categoriesData = ref()
    let darkMode = ref(true)
    function changeMode() {
      if (darkMode.value == true) {
        document.getElementById('header-nav').className = 'navbar bg-dark'
        document.getElementById('navbar-brand').className = 'navbar-brand text-light'
      }
      else {
        document.getElementById('header-nav').className = 'navbar bg-light'
        document.getElementById('navbar-brand').className = 'navbar-brand text-dark'
      }
      darkMode.value = !darkMode.value
    }

    axios
      .get('blog/categories/')
      .then(res => {
        categoriesData.value = res.data
        console.log(categoriesData.value);
      })
      .catch(error => {
        console.log(error.response);
      })

    return {
      darkMode,
      categoriesData,
      changeMode,
    }
  }
}
</script>

<style scoped>
.dropdown:hover .dropdown-menu {
    display: block;
    margin-top: 0;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  border-top: 1px solid #4b4d4e3f
}

nav a:hover,
nav a:focus {
  border-bottom: 2px solid #ccc;
  transition-duration: 0.1s
}

@media screen and (max-width: 991px) {
  .offcanvas {
    direction: rtl;
  }
}
</style>