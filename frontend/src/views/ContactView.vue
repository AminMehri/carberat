<template>

	<metainfo>
    <template v-slot:title="{ content }">{{ content }}</template>
  </metainfo>

	<div class="container ContactUs">
		<div class="row">
			<div class="col-md-8 mx-auto">
				<p class="fs-5 mt-3">شما میتوانید از طریق فرم زیر با ما در ارتباط. لطفا انتقادات و پیشنهاد های خود را به
					ما
					منتقل
					کرده و زمینه پیشرفت ما را فراهم سازید. همچنین میتوانید از طریق ایمیل و شماره همراه زیر نیز با ما
					ارتباط برقرار
					کنید.</p>
			</div>
		</div>
		<section class="my-4 border p-5 shadow">

			<div class="row">

				<div class="col-md-9 mb-md-0 mb-5">
					<form id="contact-form">

						<div v-if="loading">
							<LoadingCard />
						</div>

						<div class="row">


							<div class="col-md-6">
								<div class="form-floating mb-3">
									<input v-model="fullName" type="name" class="form-control form-control-cantact"
										id="nameInput" placeholder="example">
									<label for="nameInput">نام و نام خانوادگی</label>
								</div>
							</div>

							<div class="col-md-6">
								<div class="form-floating mb-3">
									<input v-model="email" type="email" class="form-control form-control-cantact"
										id="emailInput" placeholder="name@example.com">
									<label for="emailInput">ایمیل</label>
								</div>
							</div>

						</div>

						<div class="row">
							<div class="col-md-12">
								<div class="form-floating mb-3">
									<input v-model="subject" type="text" class="form-control form-control-cantact"
										id="subjectInput" placeholder="example">
									<label for="subjectInput">موضوع</label>
								</div>
							</div>
						</div>

						<div class="row">

							<div class="col-md-12">

								<div class="form-floating mb-3">
									<textarea v-model="content" class="form-control form-control-cantact"
										placeholder="Leave a message here" id="textareaInput"
										style="height: 100px"></textarea>
									<label for="textareaInput">پیام</label>
								</div>

							</div>
						</div>

					</form>

					<div class="text-center text-md-left">
						<a @click="sendMessage()" class="btn btn-primary">ارسال</a>
					</div>
					<div class="status"></div>
				</div>
				<!--Grid column-->

				<!--Grid column-->
				<div class="col-md-3 text-center">
					<ul class="list-unstyled mb-0">
						<li><svg xmlns="http://www.w3.org/2000/svg" width="45" height="45" fill="currentColor"
								class="bi bi-geo-alt-fill" viewBox="0 0 16 16">
								<path
									d="M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10zm0-7a3 3 0 1 1 0-6 3 3 0 0 1 0 6z" />
							</svg>
							<p>ایران, مشهد</p>
						</li>

						<li dir="ltr"><svg xmlns="http://www.w3.org/2000/svg" width="45" height="45" fill="currentColor"
								class="bi bi-telephone-fill" viewBox="0 0 16 16">
								<path fill-rule="evenodd"
									d="M1.885.511a1.745 1.745 0 0 1 2.61.163L6.29 2.98c.329.423.445.974.315 1.494l-.547 2.19a.678.678 0 0 0 .178.643l2.457 2.457a.678.678 0 0 0 .644.178l2.189-.547a1.745 1.745 0 0 1 1.494.315l2.306 1.794c.829.645.905 1.87.163 2.611l-1.034 1.034c-.74.74-1.846 1.065-2.877.702a18.634 18.634 0 0 1-7.01-4.42 18.634 18.634 0 0 1-4.42-7.009c-.362-1.03-.037-2.137.703-2.877L1.885.511z" />
							</svg>
							<p>+ 98 915 231 44**</p>
						</li>

						<li><svg xmlns="http://www.w3.org/2000/svg" width="45" height="45" fill="currentColor"
								class="bi bi-envelope-fill" viewBox="0 0 16 16">
								<path
									d="M.05 3.555A2 2 0 0 1 2 2h12a2 2 0 0 1 1.95 1.555L8 8.414.05 3.555ZM0 4.697v7.104l5.803-3.558L0 4.697ZM6.761 8.83l-6.57 4.027A2 2 0 0 0 2 14h12a2 2 0 0 0 1.808-1.144l-6.57-4.027L8 9.586l-1.239-.757Zm3.436-.586L16 11.801V4.697l-5.803 3.546Z" />
							</svg>
							<p>aminmehri45@gmail.com</p>
						</li>
					</ul>
				</div>
				<!--Grid column-->

			</div>

		</section>
	</div>
</template>


<script>
import Swal from 'sweetalert2'
import { ref } from "vue";
import axios from 'axios'
import LoadingCard from '@/components/LoadingCard.vue';
import { useMeta } from 'vue-meta';

export default {
	components: {
		LoadingCard
	},
	setup() {
		useMeta({
      title: "تماس با ما | کاربرات",
      description: "در کاربرات شما میتوانید بروز ترین مقالات راجب به انواع ماشین ها و قطعات و نحوه تعمیر آنها در سریعترین زمان ممکن بخوانید",
      robots: "index, follow",
      keywords: "کاربرات, خودرو, مقاله خودرو, مقاله ماشین, تعمیر ماشین",
      googlebot: "index, follow",
      author: "اشکان رزمی",
      owner: "امین مهری",
      canonical: "https://carberat.com/contact",
      'og:type': "contact-carberat",
      'og:title': "carberat",
      'og:description': "در کاربرات شما میتوانید بروز ترین مقالات راجب به انواع ماشین ها و قطعات و نحوه تعمیر آنها در سریعترین زمان ممکن بخوانید.",
      'og:site_name': "کاربرات|تماس با ما",
      'og:url': "https://carberat.com/contact",
      'og:image': "https://carberat.com/media/image.jpg",
      'twitter:title': "کاربرات|تماس با ما",
      'twitter:description': "در کاربرات شما میتوانید بروز ترین مقالات راجب به انواع ماشین ها و قطعات و نحوه تعمیر آنها در سریعترین زمان ممکن بخوانید.",
      'twitter:site': "https://twitter.com/aminem_mehri",
      'twitter:card': "Summary Card",
      'twitter:image': "https://carberat.com/media/image.jpg",
    });

		let fullName = ref('')
		let email = ref('')
		let subject = ref('')
		let content = ref('')

		let loading = ref(false)


		function sendMessage() {
			if (document.getElementById('nameInput').value.length != 0 && document.getElementById('emailInput').value.length != 0 && document.getElementById('subjectInput').value.length != 0 && document.getElementById('textareaInput').value.length != 0) {
				loading.value = true
				axios
					.post('blog/contact/', {
						'full_name': fullName.value,
						'email': email.value,
						'subject': subject.value,
						'content': content.value,
					})
					.then(response => {
						Swal.fire({
							title: 'هورا!',
							text: "پیام شما با موفقیت ارسال شد.",
							icon: 'success',
						});

						loading.value = false

						fullName.value = '';
						email.value = '';
						subject.value = '';
						content.value = '';
					})
					.catch(error => {
						loading.value = false
						Swal.fire({
							text: "لطفا مقادیر مورد نظر را به درستی وارد کنید",
							icon: 'error',
						});
					})

			} else {
				Swal.fire({
					title: 'وای!',
					text: "لطفا تمام فیلد های مورد نیاز را به درستی تکمیل فرمایید.",
					icon: 'warning',
				});
			}

		}


		return {
			sendMessage,
			fullName,
			email,
			subject,
			content,
			loading
		}
	},
}
</script>