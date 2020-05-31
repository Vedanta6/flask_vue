<template>
  <div id="app">
    <div class="cover-container d-flex h-100 p-2 mx-auto flex-column">
      <NavBar />
      <div id="app-container">
        <router-view/>
      </div>
      <Footer />
    </div>
  </div>
</template>

<script>
  import NavBar from '@/components/NavBar.vue'
  import Footer from '@/components/Footer.vue'

  export default {
    name: 'app',
    components: {
      NavBar,
      Footer
    },
  }
</script>
