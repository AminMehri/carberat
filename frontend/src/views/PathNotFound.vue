<template>

	<metainfo>
		<template v-slot:title="{ content }">{{ content }}</template>
	</metainfo>

	<div class="PageNotFound">
		<div class="container text-center p-5">
			<h1 id="text-404">404</h1>
			<p >.صفحه مورد نظر شما یافت نشد</p>
			<hr>
		</div>
	</div>

</template>

<script>
import { useMeta } from 'vue-meta'

export default {
	setup() {
		useMeta({
			robots: "noindex, nofollow",
			googlebot: "noindex, nofollow",
    	});
	}
}
</script>

<style>
#text-404 {
	font-size: clamp(7rem, 40vmin, 20rem);
}
</style>