<template>
    <div class="not-found">
        <h1>503</h1>
        <h1>🚧</h1>
        <p>Oops! This page is under construction.</p>
        <router-link to="/">⬅ Return Home</router-link>
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
    background: linear-gradient(135deg, #4348c8, #1c1e55);
    color: #ffffff;
    padding: 20px;
}

.not-found h1 {
    font-size: 5rem;
    margin: 0;
    animation: fadeIn 1s ease-in-out;
}

.not-found p {
    font-size: 1.5rem;
    margin: 1rem 0;
    animation: fadeIn 1.5s ease-in-out;
}

.not-found a {
    display: inline-block;
    margin-top: 15px;
    padding: 10px 20px;
    font-size: 1.2rem;
    color: #2B6CB0;
    background: #ffffff;
    border-radius: 25px;
    text-decoration: none;
    transition: 0.3s ease-in-out;
}

.not-found a:hover {
    background: #e3f2fd;
    color: #1A365D;
    transform: scale(1.05);
}

/* Fade-in animations */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(-10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>
