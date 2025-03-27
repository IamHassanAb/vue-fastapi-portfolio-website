
Copy
<template>
  <div id="app">
    <!-- <Home /> -->
    <main>
      <router-view v-slot="{ Component }">
        <transition name="fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </main>
  </div>
</template>

<script>
import Home from './components/Home.vue';
export default {
  name: 'App',
  components: {
    Home,
  },
  methods: {
    scrollToSection(sectionId) {
      const section = document.getElementById(sectionId);
      if (section) {
        section.scrollIntoView({ behavior: 'smooth' });
      }
    }
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#app {
  text-align: center;
  width: 100%;
}

.section {
  /* padding: 20px; */
  /* margin: 20px; */
  background: #000; /* Dark background for pixel theme */
  /* border: 2px solid #fff; Pixelated border */
  /* font-family: "Pixelify Sans", serif; Pixel font */
}
</style>