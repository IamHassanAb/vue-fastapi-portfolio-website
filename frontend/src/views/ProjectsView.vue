<template>
  <div class="projects-view">
    <h1>Projects</h1>
    <Projects />
  </div>
</template>

<script>
import Projects from '../components/Projects.vue';

export default {
  name: 'ProjectsView',
  components: {
    Projects
  }
}
</script>

<style scoped>
.projects-view {
  padding: 20px;
  background: var(--background-color);
  border-radius: 20px;
  box-shadow: 8px 8px 20px rgba(0, 0, 0, 0.2), 
              -8px -8px 20px rgba(255, 255, 255, 0.7);
}
</style>