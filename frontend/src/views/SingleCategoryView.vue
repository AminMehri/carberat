<template>

	<metainfo>
		<template v-slot:title="{ content }">{{ content }}</template>
	</metainfo>

	<div class="category">
		<div class="container-fluid">
			<div class="row justify-content-center">

				<div class="col-lg-3 col-md-4 col-sm-6 col-12 text-center shadow sidebar">
					<div class="card">
						<h4 class="card-title m-4 badge bold">جدیدترین مقالات این دسته بندی</h4>

						<div v-if="macLoading">
							<MacLoading />
						</div>

						<router-link v-for="article in articlesData" :to="`/article/${article.slug}`"
							class="d-flex align-items-center my-3 p-1">
							<p class="bold  article-title p-2">{{ article.title }}</p>
							<img :src="`http://127.0.0.1:8000${article.thumbnail}`" class="img-thumbnail" :alt="`${article.title}`">
						</router-link>

					</div>
				</div>

				<div class="col-lg-9 col-md-8 col-12 text-justify p-lg-5 p-md-4 p-sm-3 p-2">
					<div v-if="loadingCard">
						<LoadingCard />
					</div>
					<div v-if="!loadingCard" v-for="cat in singleCategoryData"
						class="border p-lg-5 p-md-4 p-sm-3 p-2 text-end">


						<nav dir="rtl" aria-label="breadcrumb">
							<ol class="breadcrumb">
								<li class="breadcrumb-item"><router-link to="/">خانه</router-link></li>
								<span>&nbsp;/&nbsp;</span>
								<li class="breadcrumb-item"><router-link to="/articles">دانشنامه</router-link></li>
								<span>&nbsp;/&nbsp;</span>
								<li class="breadcrumb-item">{{ cat.title }}</li>
							</ol>
						</nav>

						<h1 class="bold">{{ cat.title }}</h1>
						<hr class="w-50 ms-auto">
						<p class=" lh-lg" v-html="cat.content"></p>
					</div>

				</div>

			</div>
		</div>
	</div>
</template>

<script>
import axios from 'axios'
import { ref, watch } from 'vue';
import LoadingCard from '@/components/LoadingCard.vue'
import MacLoading from '@/components/MacLoading.vue'
import { useRoute } from 'vue-router'
import { Swal } from 'sweetalert2'
import { useMeta } from 'vue-meta';

export default {
	components: {
		LoadingCard,
		MacLoading,
	},

	setup() {
		const route = useRoute();

		let singleCategoryData = ref()
		let articlesData = ref([])
		let loadingCard = ref(true)
		let macLoading = ref(true)

		let metaTitle = ref()
		let metaDescription = ref()
		let metaKeyWords = ref()
		let thumbnailImg = ref()

		function getCatData() {
			axios
				.get('blog/category/', {
					params: {
						slug: route.params.slug
					}
				})
				.then(res => {
					singleCategoryData.value = res.data

					metaTitle.value = singleCategoryData.value[0].meta_title
					metaDescription.value = singleCategoryData.value[0].meta_description
					metaKeyWords.value = singleCategoryData.value[0].key_words
					thumbnailImg.value = singleCategoryData.value[0].thumbnail

					var meta = document.createElement('meta');
					meta.name='description';
					meta.setAttribute('content', metaDescription.value);
					document.getElementsByTagName('head')[0].appendChild(meta);

					var meta = document.createElement('meta');
					meta.name='og:description';
					meta.setAttribute('content', metaDescription.value);
					document.getElementsByTagName('head')[0].appendChild(meta);

					var meta = document.createElement('meta');
					meta.name='title';
					meta.setAttribute('content', metaTitle.value);
					document.getElementsByTagName('head')[0].appendChild(meta);

					var meta = document.createElement('meta');
					meta.name='keywords';
					meta.setAttribute('content', metaKeyWords.value);
					document.getElementsByTagName('head')[0].appendChild(meta);

					var meta = document.createElement('meta');
					meta.name='canonical';
					meta.setAttribute('content', `https://carberat.com/article/${route.params.slug}`);
					document.getElementsByTagName('head')[0].appendChild(meta);

					var meta = document.createElement('meta');
					meta.name='og:image';
					meta.setAttribute('content', `https://carberat.com${thumbnailImg.value}`);
					document.getElementsByTagName('head')[0].appendChild(meta);

					document.title  = `کاربرات | ${metaTitle.value}`

					loadingCard.value = false
				})
				.catch(error => {
					console.log(error);
					loadingCard.value = false
				})
		}
		getCatData()

		axios
			.get('blog/specific-articles/', {
				params: {
					slug: route.params.slug
				}
			})
			.then(res => {
				articlesData.value = res.data
				macLoading.value = false
			})
			.catch(error => {
				console.log(error.response);
				macLoading.value = false
			})
		
		useMeta({
			robots: "index, follow",
			googlebot: "index, follow",
			author: "اشکان رزمی",
			owner: "امین مهری",
			'og:type': "contact-carberat",
			'og:title': "carberat",
			'og:url': `https://carberat.com/article/${route.params.slug}`,
			'twitter:site': "https://twitter.com/aminem_mehri",
			'twitter:card': "Summary Card",
		});

		return {
			singleCategoryData,
			articlesData,
			loadingCard,
			macLoading,
			getCatData
		}
	},

	watch: {
		$route() {
			this.getCatData()
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

.img-thumbnail {
	width: 33%;
	height: auto;
	min-width: 75px
}

@media screen and (max-width: 767px) {
	.sidebar {
		min-width: 300px;
	}	
}
</style>