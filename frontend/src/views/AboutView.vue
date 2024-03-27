<template>

  <metainfo>
    <template v-slot:title="{ content }">{{ content }}</template>
  </metainfo>
  
  <div class="about">
    <h1>This is an about page</h1>
  </div>
</template>

<script>
export default {
  setup() {
    useMeta({
      title: "درباره ما | کاربرات",
      description: "در کاربرات شما میتوانید بروز ترین مقالات راجب به انواع ماشین ها و قطعات و نحوه تعمیر آنها در سریعترین زمان ممکن بخوانید",
      robots: "index, follow",
      keywords: "کاربرات, خودرو, مقاله خودرو, مقاله ماشین, تعمیر ماشین",
      googlebot: "index, follow",
      author: "اشکان رزمی",
      owner: "امین مهری",
      canonical: "https://carberat.com/about",
      'og:type': "about-carberat",
      'og:title': "carberat",
      'og:description': "در کاربرات شما میتوانید بروز ترین مقالات راجب به انواع ماشین ها و قطعات و نحوه تعمیر آنها در سریعترین زمان ممکن بخوانید.",
      'og:site_name': "کاربرات|درباره ما",
      'og:url': "https://carberat.com/about",
      'og:image': "https://carberat.com/media/image.jpg",
      'twitter:title': "کاربرات|درباره ما",
      'twitter:description': "در کاربرات شما میتوانید بروز ترین مقالات راجب به انواع ماشین ها و قطعات و نحوه تعمیر آنها در سریعترین زمان ممکن بخوانید.",
      'twitter:site': "https://twitter.com/aminem_mehri",
      'twitter:card': "Summary Card",
      'twitter:image': "https://carberat.com/media/image.jpg",
    });
  }
}
</script>
