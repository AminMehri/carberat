<template>
  <div dir="rtl" class="articles">
    <div class="container-fluid">
      <div class="row">

				
				<div class="col-lg-8 col-md-10 col-10 m-5 p-4">
					<div class="border p-5 rounded">

						<nav aria-label="breadcrumb">
							<ol class="breadcrumb">
								<li class="breadcrumb-item"><router-link to="/">خانه</router-link></li>
								<span>&nbsp;/&nbsp;</span>
								<li class="breadcrumb-item active" aria-current="page">دانشنامه</li>
							</ol>
						</nav>

						<h1 class="bold ">دانشنامه</h1>

					</div>

          <router-link v-for="art in articlesData" :to="`/article/${art.slug}`" dir="rtl" class="mb-3">
            <div class="row align-items-center category-card">

              <div class="col-md-4">
                <img :src="`http://127.0.0.1:8000${art.thumbnail}`" class="img-fluid rounded-start" alt="...">
              </div>
              
              <div class="col-md-8">
                <div class="card-body text-dark">
                  <h3 class="card-title bold my-3 ">{{art.title}}</h3>
                  <p class="card-text text-dark lh-lg" v-html="art.description"></p>
                  <p class="card-text"><small class="text-muted">{{art.date}}</small></p>
                </div>
              </div>

            </div>
          </router-link>

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


export default{
  components: {
    LoadingCard,
    MacLoading,
  },

  setup(){
    let articlesData = ref([])
    let loadingCard = ref(true)
    let macLoading = ref(true)

    axios
      .get('blog/articles/')
      .then(res => {
        articlesData.value = res.data
        loadingCard.value = false
      })
      .catch(error => {
        console.log(error.response);
        loadingCard.value = false
      })
    
    return {
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
</style>
