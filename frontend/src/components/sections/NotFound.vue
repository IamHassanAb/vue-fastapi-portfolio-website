<template>
    <div class="not-found">
        <h1>404</h1>
        <p>Oops! The page you are looking for does not exist.</p>
        <router-link to="/">Go back to Home</router-link>
    </div>
</template>

<script>
export default {
    name: 'NotFound'
}
</script>

<style scoped>
.not-found {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
    text-align: center;
    background-color: #000000;
    color: #4348c8;
}

.not-found h1 {
    font-size: 6rem;
    margin: 0;
}

.not-found p {
    font-size: 1.5rem;
    margin: 1rem 0;
}

.not-found a {
    color: #007bff;
    text-decoration: none;
    font-size: 1.2rem;
}

.not-found a:hover {
    text-decoration: underline;
}
</style>