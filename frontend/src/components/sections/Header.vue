<template>
    <header class="full-page-header">
        <div class="nav-container">
            <div class="logo">
                <a href="#">
                    <img src="images/pixel_character.png" alt="Logo" class="logo-img" />
                </a>
            </div>
            <nav class="main-nav">
                <a href="#" @click.prevent="scrollToSection('home')" class="nav-link">Home</a>
                <a href="#about" @click.prevent="scrollToSection('about')" class="nav-link">About</a>
                <a href="#projects" @click.prevent="scrollToSection('projects')" class="nav-link">Projects</a>
                <a href="#contact" @click.prevent="scrollToSection('contact')" class="nav-link">Contact</a>
            </nav>
            <button class="share-button" @click="share" aria-label="Share">
                <span>Share</span>
            </button>
        </div>

        <div class="hero-content">
            <div class="hero-text">
                <h1 class="hero-title">
                Hello! <br>
                I am <span>&nbspHassan&nbsp</span>
                </h1>
            
                <p class="hero-subtitle">Software Engineer | AI/ML</p>
            </div>
        </div>

        <div class="cta-container">
            <a href="" @click.prevent="shareCV" class="cta-button">
                Get My CV
            </a>
            <a href="#contact" @click.prevent="scrollToSection('contact')" class="cta-button">
                Get In Touch
            </a>
            <a href="#about" @click.prevent="scrollToSection('about')" class="cta-button">
                More About Me
            </a>
        </div>
    </header>
</template>

<script>
export default {
    name: 'Header',
    methods: {
        shareCV() {
            console.log('Starting CV download...');
            const file_path = 'assets/Hassan_Abbas_Resume_AI_ML_Engineer_Software_Developer.pdf';
            console.log('File path:', file_path);

            const link = document.createElement('a');
            link.href = file_path;
            link.download = 'Hassan_Abbas_Resume.pdf';
            console.log('Created download link element');
            
            document.body.appendChild(link);
            console.log('Added link to document body');
            link.click();
            console.log('Triggered download click');
            document.body.removeChild(link);
            console.log('Removed link from document body');
            console.log('Download complete');
        },
        scrollToSection(sectionId) {
            document.getElementById(sectionId).scrollIntoView({ behavior: 'smooth' });
        },
        share() {
            const url = window.location.href;
            navigator.clipboard.writeText(url).then(() => {
            alert('Website link copied to clipboard!');
            }).catch(err => {
            console.error('Failed to copy: ', err);
            });
        }
    }
}
</script>

<style>
.full-page-header {
    position: relative;
    width: 100%;
    height: 100vh;
    background-color: #4347c83b;
    padding: 1.5rem;
    display: flex;
    flex-direction: column;
    color: #e6f1ff;
}

.nav-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 2rem;
    background: rgba(10, 25, 47, 0.95);
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1000;
    backdrop-filter: blur(10px);
}

.logo-img {
    width: 40px;
    height: 40px;
    transition: transform 0.3s ease;
}

.logo-img:hover {
    transform: scale(1.1);
}

.main-nav {
    display: flex;
    gap: 2rem;
}

.nav-link {
    text-decoration: none;
    color: #e6f1ff;
    font-size: 1rem;
    padding: 0.5rem 1rem;
    transition: all 0.3s ease;
    position: relative;
}

.nav-link::after {
    content: '';
    position: absolute;
    width: 0;
    height: 2px;
    bottom: 0;
    left: 50%;
    background-color: #64ffda;
    transition: all 0.3s ease;
}

.nav-link:hover::after {
    width: 100%;
    left: 0;
}

.share-button {
    border: 1px solid #64ffda;
    background: transparent;
    color: #64ffda;
    padding: 0.75rem 1.5rem;
    border-radius: 4px;
    font-size: 1rem;
    cursor: pointer;
    transition: all 0.3s ease;
}

.share-button:hover {
    background: rgba(100, 255, 218, 0.1);
    transform: translateY(-2px);
}

.hero-content {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: left;
    padding: 0 2rem;
}

.hero-text {
    max-width: 800px;
}

.hero-title {
    font-size: clamp(40px, 8vw, 80px);
    line-height: 1.1;
    margin-bottom: 1rem;
    color: #64ffda;
}
.hero-title span {
    color: #ffffff;
    background-color: #00ffc3;
    transition: all 0.3s ease;
}
.hero-title span:hover {
    color: #00ffc3;
    background-color: #000000;
}
.hero-subtitle {
    font-size: clamp(16px, 4vw, 24px);
    color: #8892b0;
}

.cta-container {
    display: flex;
    justify-content: center;
    gap: 2rem;
    padding: 2rem;
    margin-bottom: 2rem;
}

.cta-button {
    text-decoration: none;
    padding: 1rem 2rem;
    border: 2px solid #64ffda;
    color: #64ffda;
    border-radius: 4px;
    transition: all 0.3s ease;
    font-weight: 500;
}

.cta-button:hover {
    background: rgba(100, 255, 218, 0.1);
    transform: translateY(-2px);
}

@media (max-width: 768px) {
    .nav-container {
        padding: 1rem;
    }

    .main-nav {
        display: none;
    }

    .hero-content {
        text-align: center;
        padding: 0 1rem;
    }

    .cta-container {
        flex-direction: column;
        align-items: center;
        gap: 1rem;
    }

    .cta-button {
        width: 100%;
        text-align: center;
    }
}
</style>