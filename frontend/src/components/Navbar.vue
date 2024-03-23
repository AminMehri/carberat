<template>
  <header dir="rtl" class="navbar" id="header-nav">
    <div class="container-fluid">
      <router-link class="navbar-brand" id="navbar-brand" to="/">
        <img src="../assets/logo192.png" alt="کاربرات" class="img-fluid w-25">
        کاربرات
      </router-link>

      <form class="d-flex position-relative" role="search" id="search-form">

        <input v-model="titleSearch" class="form-control me-2" type="search" placeholder="جستجو ...">

        <div class="position-absolute shadow border rounded w-100" id="search-box">
          <div>
            <div class="row border border-bottom">

              <router-link v-for="a in searchRes" :to=a.slug target="_blank"
                class="bg-secondary d-block p-3 hover-search-result">
                <span class="ms-2 fw-bold thin text-white">{{ a.title }}</span>
                <span class="badge bg-danger">{{ a.badge }}</span>
              </router-link>

            </div>
          </div>
        </div>
      </form>



      <div>
        <i v-if="!darkMode" @click="changeMode" type="button" class="fas fa-sun fs-4"></i>
        <i v-if="darkMode" @click="changeMode" type="button" class="fa fa-moon fs-4"></i>
      </div>

    </div>
  </header>

  <nav class="navbar navbar-expand-lg shadow" id="nav">
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
                <li><router-link class="dropdown-item text-dark" to="/articles">همه مقالات</router-link></li>

                <li v-for="(cat, index) in categoriesData">
                  <div v-if="!cat.parent" class="accordion accordion-flush" id="accordionFlushExample">
                    <div class="accordion-item">
                      <h2 class="accordion-header" id="flush-headingOne">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                          :data-bs-target="`#flush-collapseOne${index}`" aria-expanded="false"
                          aria-controls="flush-collapseOne">
                          {{ cat.title }}
                        </button>
                      </h2>
                      <div :id="`flush-collapseOne${index}`" class="accordion-collapse collapse"
                        aria-labelledby="flush-headingOne" data-bs-parent="#accordionFlushExample">
                        <div class="accordion-body">
                <li v-for="c in cat.children"><router-link class="dropdown-item text-dark" :to="`/category/${c[1]}`">{{ c[0]
                    }}</router-link></li>
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
import { ref, watch } from 'vue'

export default {
  setup() {
    let categoriesData = ref()
    let darkMode = ref(true)
    function changeMode() {
      document.querySelector('html').toggleAttribute('data-dark-mode')
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

    let titleSearch = ref('')
    let searchRes = ref()
    // let searchLoading = ref(false)

    let numbersSearch = 0

    watch([titleSearch], () => {
      numbersSearch += 1
      let currentNum = numbersSearch

      setTimeout(() => {

        if (currentNum == numbersSearch && titleSearch.value.length > 2) {
          // searchLoading.value = true
          searchRes.value = []
          axios
            .post('blog/search/', {
              'slug': titleSearch.value
            })
            .then(response => {
              searchRes.value = response.data
              // searchLoading.value = false
            })
            .catch(error => {
              // searchLoading.value = false
              console.log(error.response);
            })
        } else {
          searchRes.value = []
        }
      }, 1000)
    })

    return {
      darkMode,
      categoriesData,
      titleSearch,
      searchRes,
      changeMode,
    }
  }
}
</script>

<style>
:root {
  --body-color: white;
  --body-color-2: rgba(236, 235, 235, 0.911);
  --font-color: black;
}

[data-dark-mode] {
  --body-color: black;
  --body-color-2: black;
  --font-color: white;
}

@media (prefers-color-scheme: dark) {
  :root {
    --body-color: black;
    --body-color-2: black;
    --font-color: white;
  }
}

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

#search-form {
  width: 50%;
  min-width: 300px;
}

#search-box {
  z-index: 1;
  top: 38px
}

.hover-search-result:hover {
  background-color: rgb(72, 76, 77) !important;
  transition-duration: 0.3s;
}

/* dark mode */
body, .footer, .navbar, .card, .form-control-cantact {
  background-color: var(--body-color) !important;
  color: var(--font-color) !important;
}
.card-text, .card-title, nav a, .navbar-brand, .text-muted-date, .article-title{
  color: var(--font-color) !important;
}
.card-title{
  background-color: var(--font-color) !important; 
  color: var(--body-color) !important;
}

.footer, .navbar{
  background-color: var(--body-color-2) !important;
  color: var(--font-color) !important;
}

</style>