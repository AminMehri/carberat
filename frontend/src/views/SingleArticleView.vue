<template>
	<div class="home">
		<div class="container-fluid">
			<div class="row">

				<div class="col-lg-3 col-md-4 col-sm-6 col-12 text-center shadow">
					<div class="card">
						<h4 class="card-title m-4 badge bold">جدیدترین مقالات</h4>

						<div v-if="macLoading">
							<MacLoading />
						</div>

						<router-link v-for="article in articlesData" @click="getArticleData(article.slug)" :to="`/article/${article.slug}`"
							class="d-flex align-items-center my-3">
							<p class="bold article-title">{{ article.title }}</p>
							<img :src="`http://127.0.0.1:8000${article.thumbnail}`" class="img-thumbnail w-25 " alt="" srcset="">
						</router-link>

					</div>
				</div>

				<div class="col-lg-9 col-md-8 col-12 text-justify p-lg-5 p-md-4 p-sm-3 p-2">
					<div v-if="loadingCard">
						<LoadingCard />
					</div>
					<div v-if="!loadingCard" v-for="art in singleArticleData" class="border p-lg-5 p-md-4 p-sm-3 p-2 text-end">


						<nav dir="rtl" aria-label="breadcrumb">
							<ol class="breadcrumb">
								<li class="breadcrumb-item"><router-link to="/">خانه</router-link></li>
								<span>&nbsp;/&nbsp;</span>
								<li class="breadcrumb-item"><router-link to="/articles">دانشنامه</router-link></li>
								<span>&nbsp;/&nbsp;</span>
								<div v-for="cat in art.category">
									<li class="breadcrumb-item"><router-link
											:to="`/category/${cat[1]}`">{{ cat[0] }}</router-link>&nbsp;/&nbsp;</li>
								</div>
								<li class="breadcrumb-item">{{ art.title }}</li>
							</ol>
						</nav>

						<h1 class="bold">{{ art.title }}</h1>
						<hr class="w-50 ms-auto">
						<p class="lh-lg" v-html="art.content"></p>
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
import { useRoute } from 'vue-router'
import { Swal } from 'sweetalert2'


export default {
	components: {
		LoadingCard,
		MacLoading,
	},

	setup() {
		const route = useRoute();

		let singleArticleData = ref()
		let articlesData = ref([])
		let loadingCard = ref(true)
		let macLoading = ref(true)

		let slug = ref(route.params.slug)

		function getArticleData(sl) {
			document.body.scrollTop = 0; // For Safari
			document.documentElement.scrollTop = 0;
			if (sl) {
				slug.value = sl
			} else {
				slug.value = route.params.slug
			}
			axios
				.get('blog/article/', {
					params: {
						slug: slug.value
					}
				})
				.then(res => {
					singleArticleData.value = res.data
					loadingCard.value = false
				})
				.catch(error => {
					console.log(error.response);
					loadingCard.value = false
				})
		}
		getArticleData()
		axios
			.get('blog/articles/')
			.then(res => {
				articlesData.value = res.data
				macLoading.value = false
			})
			.catch(error => {
				console.log(error.response);
				macLoading.value = false
			})

		return {
			singleArticleData,
			articlesData,
			getArticleData,
			loadingCard,
			macLoading
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

.article-title:hover,
.article-title:focus {
	text-decoration: underline;
}
</style>