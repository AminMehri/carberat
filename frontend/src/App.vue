<template>
  <Navbar/>
  <router-view/>
  <Footer />
</template>


<script>
import Navbar from '@/components/Navbar.vue'
import Footer from '@/components/Footer.vue'


export default {
  name: 'HomeView',
  components: {
    Navbar,
    Footer
  }, 
  watch: {
    $route() {
      if (document.querySelector("[name='description']")) document.querySelector("[name='description']").remove()
      if (document.querySelector("[name='og:description']")) document.querySelector("[name='og:description']").remove()
      if (document.querySelector("[name='title']")) document.querySelector("[name='title']").remove()
      if (document.querySelector("[name='keywords']")) document.querySelector("[name='keywords']").remove()
      if (document.querySelector("[name='canonical']")) document.querySelector("[name='canonical']").remove()
      if (document.querySelector("[name='og:image']")) document.querySelector("[name='og:image']").remove()
    }
  }
}
</script>

<style>
@font-face {
  font-family: 'Vazir';
  src: url('@/assets/fonts/Vazir.woff2') format('woff2'),
  url('@/assets/fonts/Vazir.woff') format('woff'),
  url('@/assets/fonts/Vazir.ttf') format('truetype');
}
@font-face {
  font-family: 'Vazir-Bold';
  src: url('@/assets/fonts/Vazir-Bold.woff2') format('woff2'),
  url('@/assets/fonts/Vazir-Bold.woff') format('woff'),
  url('@/assets/fonts/Vazir-Bold.ttf') format('truetype');
}
@font-face {
  font-family: 'Vazir-Thin';
  src: url('@/assets/fonts/Vazir-Thin.woff2') format('woff2'),
  url('@/assets/fonts/Vazir-Thin.woff') format('woff'),
  url('@/assets/fonts/Vazir-Thin.ttf') format('truetype');
}
@font-face {
  font-family: 'Vazir-Light';
  src: url('@/assets/fonts/Vazir-Light.woff2') format('woff2'),
  url('@/assets/fonts/Vazir-Light.woff') format('woff'),
  url('@/assets/fonts/Vazir-Light.ttf') format('truetype');
}

#app {
  font-family: Vazir;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
a{
  text-decoration: none !important;
}

.swal2-popup{
	font-family: Vazir !important;
	direction: rtl;
	font-size: .8rem !important;
}

.swal2-title{
	font-family: Vazir-Bold !important;
}

.bold{
  font-family: Vazir-Bold !important;
}
.thin{
  font-family: Vazir-Thin !important;
}
.light{
  font-family: Vazir-Light !important;
}

</style>
