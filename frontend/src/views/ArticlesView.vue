<template>

  <metainfo>
    <template v-slot:title="{ content }">{{ content }}</template>
  </metainfo>
  
  <div dir="rtl" class="articles">
    <div class="container-fluid">
      <div class="row justify-content-center">


        <div class="col-lg-8 col-md-10 col-10 m-5 p-4">
          <div class="border p-5 rounded">

            <nav aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item"><router-link to="/">خانه</router-link></li>
                <span>&nbsp;/&nbsp;</span>
                <li class="breadcrumb-item" aria-current="page">دانشنامه</li>
              </ol>
            </nav>

            <h1 class="bold ">دانشنامه</h1>

          </div>

          <router-link v-for="art in articlesData" :to="`/article/${art.slug}`" dir="rtl" class="mb-3">
            <div class="row align-items-center category-card">

              <div class="col-lg-4">
                <img :src="`http://127.0.0.1:8000${art.thumbnail}`" class="img-fluid rounded-start" :alt="`${art.title}`">
              </div>

              <div class="col-lg-8">
                <div class="card-body">
                  <h3 class="card-title bold my-3 p-2 rounded">{{ art.title }}</h3>
                  <p class="card-text lh-lg" v-html="art.description"></p>
                  <p class="card-text"><small class="text-muted-date">{{ art.date }}</small></p>
                </div>
              </div>

            </div>
          </router-link>

          <nav aria-label="Page navigation example">
            <ul class="pagination d-flex justify-content-center">
              <li v-for="index in Math.floor(articlesData.length/10)+1" class="page-item">
                <a @click="getArticlesData(index*10-10)" class="page-link" href="#">{{index}}</a>
              </li>
            </ul>
          </nav>

        </div>

      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios'
import { ref } from 'vue';
import LoadingCard from '@/components/LoadingCard.vue'
import MacLoading from '@/components/MacLoading.vue'
import { useMeta } from 'vue-meta'

export default {
  components: {
    LoadingCard,
    MacLoading,
  },

  setup() {
    useMeta({
      title: "مقالات | کاربرات",
      description: "در کاربرات شما میتوانید بروز ترین مقالات راجب به انواع ماشین ها و قطعات و نحوه تعمیر آنها در سریعترین زمان ممکن بخوانید",
      robots: "index, follow",
      keywords: "کاربرات, خودرو, مقاله خودرو, مقاله ماشین, تعمیر ماشین",
      googlebot: "index, follow",
      author: "اشکان رزمی",
      owner: "امین مهری",
      canonical: "https://carberat.com/articles",
      'og:type': "articles-carberat",
      'og:title': "carberat",
      'og:description': "در کاربرات شما میتوانید بروز ترین مقالات راجب به انواع ماشین ها و قطعات و نحوه تعمیر آنها در سریعترین زمان ممکن بخوانید.",
      'og:site_name': "کاربرات|مقالات",
      'og:url': "https://carberat.com/articles",
      'og:image': "https://carberat.com/media/image.jpg",
      'twitter:title': "کاربرات|مقالات",
      'twitter:description': "در کاربرات شما میتوانید بروز ترین مقالات راجب به انواع ماشین ها و قطعات و نحوه تعمیر آنها در سریعترین زمان ممکن بخوانید.",
      'twitter:site': "https://twitter.com/aminem_mehri",
      'twitter:card': "Summary Card",
      'twitter:image': "https://carberat.com/media/image.jpg",
    });

    let articlesData = ref([])
    let loadingCard = ref(true)
    let macLoading = ref(true)

    let lastShow = ref(0)

    function getArticlesData(ls) {
      if(ls) {
        lastShow.value = ls
      } else {
        lastShow.value = 0
      }
      axios
        .get('blog/articles/', {
          params: {
            lastShow: lastShow.value
          }
        })
        .then(res => {
          articlesData.value = res.data
          loadingCard.value = false
        })
        .catch(error => {
          console.log(error.response);
          loadingCard.value = false
        })
    }
    getArticlesData()
    

    return {
      articlesData,
      loadingCard,
      macLoading,
      lastShow,
      getArticlesData
    }
  }
}
</script>

<style scoped>
.category-card:hover,
.category-card:focus {
  box-shadow: 10px 5px 5px black;
  opacity: 0.6;
  transition-duration: 0.3s;
}
</style>
