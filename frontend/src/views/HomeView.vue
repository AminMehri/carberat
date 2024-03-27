<template>

  <metainfo>
    <template v-slot:title="{ content }">{{ content }}</template>
  </metainfo>

  <div class="home">
    <div class="container-fluid">
      <div class="row">

        <div class="col-lg-3 col-md-4 col-sm-6 col-12 text-center shadow">
          <div class="card">
            <h4 class="card-title m-4 badge bold">جدیدترین مقالات</h4>

            <div v-if="macLoading"><MacLoading /></div>
            
            <router-link v-for="article in articlesData" :to="`/article/${article.slug}`" class="d-flex align-items-center my-3 p-1">
              <p class="bold article-title p-2">{{article.title}}</p>
              <img :src="`http://127.0.0.1:8000${article.thumbnail}`" class="img-thumbnail" :alt="`${article.title}`">
            </router-link>

          </div>
        </div>

        <div class="col-lg-9 col-md-8 col-sm-6 col-12 p-lg-4 p-md-3 p-sm-2">
          
          <div class="border p-lg-4 p-md-3 p-sm-2 rounded">
            <div v-if="loadingCard"><LoadingCard/></div>
            
            <router-link v-for="cat in categoriesData" :to="`/category/${cat.slug}`" dir="rtl" class="mb-3">
              <div class="row align-items-center category-card">

                <div class="col-lg-4">
                  <img :src="`http://127.0.0.1:8000${cat.thumbnail}`" class="img-fluid rounded-start" :alt="`${cat.title}`">
                </div>
                
                <div class="col-lg-8">
                  <div class="card-body">
                    <h5 class="card-title badge bold fs-4 my-3">{{cat.title}}</h5>
                    <p class="mt-0 thin" v-if=cat.parent>زیر مجموعه‌ {{ cat.parent }}</p>
                    <p class="card-text lh-lg" v-html="cat.description"></p>
                  </div>
                </div>

              </div>
            </router-link>
          </div>

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
import { useMeta } from 'vue-meta';

export default{
  components: {
    LoadingCard,
    MacLoading,
  },

  setup(){
    useMeta({
      title: "صفحه اصلی | کاربرات",
      description: "در کاربرات شما میتوانید بروز ترین مقالات راجب به انواع ماشین ها و قطعات و نحوه تعمیر آنها در سریعترین زمان ممکن بخوانید",
      robots: "index, follow",
      keywords: "کاربرات, خودرو, مقاله خودرو, مقاله ماشین, تعمیر ماشین",
      googlebot: "index, follow",
      author: "اشکان رزمی",
      owner: "امین مهری",
      canonical: "https://carberat.com/",
      'og:type': "carberat",
      'og:title': "carberat",
      'og:description': "در کاربرات شما میتوانید بروز ترین مقالات راجب به انواع ماشین ها و قطعات و نحوه تعمیر آنها در سریعترین زمان ممکن بخوانید.",
      'og:site_name': "کاربرات|صفحه اصلی",
      'og:url': "https://carberat.com/",
      'og:image': "https://carberat.com/media/image.jpg",
      'twitter:title': "کاربرات|صفحه اصلی",
      'twitter:description': "در کاربرات شما میتوانید بروز ترین مقالات راجب به انواع ماشین ها و قطعات و نحوه تعمیر آنها در سریعترین زمان ممکن بخوانید.",
      'twitter:site': "https://twitter.com/aminem_mehri",
      'twitter:card': "Summary Card",
      'twitter:image': "https://carberat.com/media/image.jpg",
    });

    let categoriesData = ref([])
    let articlesData = ref([])
    let loadingCard = ref(true)
    let macLoading = ref(true)

    axios
      .get('blog/categories/')
      .then(res => {
        categoriesData.value = res.data
        loadingCard.value = false
      })
      .catch(error => {
        console.log(error.response);
        loadingCard.value = false
      })
    
    axios
      .get('blog/main-articles/')
      .then(res => {
        articlesData.value = res.data
        macLoading.value = false
      })
      .catch(error => {
        console.log(error.response);
        macLoading.value = false
      })
    
    return {
      categoriesData,
      articlesData,
      loadingCard,
      macLoading
    }
  }
}
</script>

<style scoped>
.category-card:hover, .category-card:focus {
	box-shadow: 10px 5px 5px black;
  opacity: 0.6;
  transition-duration: 0.3s;
}

.article-title:hover, .article-title:focus {
  text-decoration: underline;
}

.img-thumbnail{
  width: 33%;
  height: auto;
  min-width: 75px
}
</style>
