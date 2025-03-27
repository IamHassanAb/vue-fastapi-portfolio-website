<template>
  <div class="home">
    <!-- <Header id="home"></Header> -->
    <section class="section" id="home">
      <Header />
    </section>
    <section class="section" id="about">
      <About />
    </section>
    <section class="section" id="projects">
      <Projects />
    </section>
    <section class="section" id="contact">
      <Contact />
    </section>
  </div>
</template>

<script>
import About from './sections/About.vue';
import Projects from './sections/Projects.vue';
import Contact from './sections/Contact.vue';
import Header from './sections/Header.vue';
// import Header from './sections/Header.vue';

export default {
  name: 'Home',
  components: {
    // Home,
    About,
    Projects,
    Contact,
    Header
  }
}
</script>

<style scoped>
</style>