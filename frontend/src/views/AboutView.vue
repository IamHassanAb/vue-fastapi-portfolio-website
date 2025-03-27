<template>
  <div class="about-view">
    <About />
  </div>
</template>

<script>
import About from '../components/About.vue';

export default {
  components: {
    About
  }
}
</script>

<style scoped>
.about-view {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
</style>