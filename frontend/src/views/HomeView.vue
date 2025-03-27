<template>
  <div class="home-view">
    <Home />
  </div>
</template>

<script>
import Home from '../components/Home.vue';

export default {
  name: 'HomeView',
  components: {
    Home
  }
}
</script>

<style scoped>
.home-view {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
</style>