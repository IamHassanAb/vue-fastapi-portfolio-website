<template>
  <div class="contact-view">
    <h1>Contact Me</h1>
    <Contact />
  </div>
</template>

<script>
import Contact from '@/components/Contact.vue';

export default {
  name: 'ContactView',
  components: {
    Contact
  }
};
</script>

<style scoped>
.contact-view {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}
</style>