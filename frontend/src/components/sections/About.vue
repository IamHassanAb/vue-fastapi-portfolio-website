<template>
  <section class="about">
    <div class="container">
      <header class="section-header">
        <h1 class="gradient-text">About Me</h1>
        <p class="lead-text">
          Software Design Engineer with experience modernizing applications and refactoring legacy code using Quarkus, Flask, and Vue. Skilled in
building scalable systems, developing AI-powered solutions with FastAPI, Numpy, Pandas, Scikit-Learn and LangChain, optimizing
performance and creating ML pipelines. Certified in LLM-powered applications, Data Science, and AWS, with a strong passion for
continuous learning.
          </p>
        <!-- <p class="lead-text">
          Transforming raw data into strategic insights through advanced analytics and machine learning.
        </p> -->
      </header>

      <div class="grid-layout" style="">
        <!-- <article class="card">
          <h2>Background</h2>
          <div class="decorative-line"></div>
          <p class="body-text">
            📊 Data Scientist with 5+ years experience in predictive modeling and data mining.<br>
            🎓 Computer Science Graduate from Stanford University<br>
            🏆 Kaggle Competition Finalist 2023<br>
            💡 Passionate about ethical AI and explainable ML
          </p>
        </article> -->

          <article class="card skill-grid">
            <h2>Skills</h2>
            <div class="decorative-line"></div>
            <ul class="skill-list">
              <li v-for="(skill, index) in skills" 
              :key="index" 
              class="card skill-item"
              :style="{'--delay': `${index * 0.15}s`}">
                <div class="skill-icon"><img :src="skill.source" :style="{scale: skill.scale, z}"/></div>
                <span class="skill-label">{{ skill.name }}</span>
                <div class="skill-progress"><p class="skill-description">{{ skill.description }}</p></div>
              </li>
            </ul>
          </article>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'About',
  data() {
    return {
      skills: [
        { 
          source: "images/python.png", 
          name: 'Python', 
          description: 'A high-level, general-purpose programming language focused on readability.', 
          progress: '95%' ,
          scale: 1, 
        },
        { 
          source: 'images/langchain.png', 
          name: 'LangChain', 
          description: 'A framework focused on integration of LLMs into applications.', 
          progress: '90%' ,
          scale: 1
        },
        { 
          source: 'images/fastapi.png', 
          name: 'FastAPI', 
          description: 'A fast, async Python framework for building APIs with automatic validation, OpenAPI docs, and high performance, ideal for scalable applications.', 
          progress: '92%' ,
          scale: 1
        },
        { 
          source: 'images/scikitlearn.png', 
          name: 'Scikit-Learn', 
          description: 'Scikit-learn is a powerful Python library for machine learning, offering simple and efficient tools for data mining, analysis, and modeling.', 
          progress: '85%' ,
          scale: 1
        },
        { 
          source: "images/mysql.png", 
          name: 'MySQL', 
          description: 'MySQL is a fast, reliable, and open-source relational database management system (RDBMS) widely used for web applications and enterprise solutions.', 
          progress: '94%' ,
          scale: 1
        },
        { 
          source: 'images/quarkus.png', 
          name: 'Quarkus Java', 
          description: 'Quarkus is a Kubernetes-native Java framework optimized for fast startup, low memory usage, and cloud-native microservices. ', 
          progress: '88%' ,
          scale: 1
        },
      ]
    };
  },
  mounted() {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
        }
      });
    }, { threshold: 0.1 });

    const skillItems = document.querySelectorAll('.skill-item');
    skillItems.forEach(item => observer.observe(item));
  }
};
</script>

<style scoped>
.about {
  /* Remove sticky and fixed height */
  width: 100%;
  min-height: 100vh; /* Changed from height to min-height */
  background-color: #000000;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  color: #e6f1ff;
  position: relative; /* Changed from sticky */
}

.container {
  display: flex;
  flex-direction: column;
  width: 100%;
  min-height: 100%; /* Changed from fixed height */
  margin: 0 auto;
  padding: 0 1.5rem;
  justify-content: space-between;
  padding-bottom: 100px;
  flex: 1; /* Added to allow proper flex growth */
}

.section-header {
  display: flex;
  flex-direction: column;
  text-align: center;
  margin-bottom: 3rem;
}

.gradient-text {
  background: linear-gradient(135deg, #4348c8 0%, #ffffff 100%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.lead-text {
  color: #fff;
  font-size: 1.25rem;
  max-width: 600px;
  margin: 0 auto;
  line-height: 1.6;
  text-align: justify;
}

.grid-layout {
  display: flex;
  flex-direction: column;
  align-self: center;
  /* align-self: flex-end; */
  /* flex-wrap: wrap; */
  /* grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); */
  gap: 2rem;
  margin-top: 2rem;
  
}

.card {
  /* align-items: center; */
  background: rgb(0, 0, 0);
  border-radius: 16px;
  padding: 2rem;
  box-shadow: 0 8px 24px rgba(255, 255, 255, 0.336);
  transition: transform 0.3s ease;
  /* width: 100%; */
}

.card:hover {
  transform: translateY(-5px);
}

.decorative-line {
  width: 60px;
  height: 4px;
  background: #4348c8;
  margin: 1rem 0;
  border-radius: 2px;
}

.skill-list {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 1.5rem;
  /* width: 100%; */
}

.skill-item {
  display: grid;
  position: relative;
  padding: 1rem;
  background: #f5f7fb;
  border-radius: 8px;
  overflow: hidden;
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.6s ease, transform 0.6s ease;
  animation-delay: var(--delay);
}

.skill-item.visible {
  opacity: 1;
  transform: translateY(0);
}

@keyframes fadeInUp {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}


.skill-label {
  color: #000000;
  display: block;
  font-weight: 600;
  margin-bottom: 0.25rem;
  position: relative;
  z-index: 1;
  margin-bottom: 0;
  align-self: flex-end;
}



.skill-icon {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
}
.skill-icon img {
  display: block;
  width: 100%;
  height: 100%;
  transition: transform 0.3s ease-in-out;
}

.skill-progress {
  position: absolute;
  left: 0;
  top: 0;
  height: 100%;
  background: rgba(67, 72, 200, 0.1);
  transition: width 0.6s cubic-bezier(0.4, 0, 0.2, 1);
  width: 0; /* Start at 0 width */
}

.skill-item:hover .skill-progress {
  width: 100%; /* Will be set by the inline style */

}

.skill-icon .skill-description {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background: rgba(0, 0, 0, 0.7);
  color: #fff;
  opacity: 0;
  transition: opacity 0.3s ease-in-out;
}

.skill-icon:hover .skill-description {
  opacity: 1;
}

.body-text {
  color: #5c6370;
  line-height: 1.7;
  font-size: 1.05rem;
}

@media (max-width: 768px) {
  .grid-layout {
    grid-template-columns: 1fr;
  }
  
  .gradient-text {
    font-size: 2rem;
  }
}
</style>