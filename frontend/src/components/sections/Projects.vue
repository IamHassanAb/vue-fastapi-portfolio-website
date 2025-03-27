<template>
  <section id="projects" class="projects-section">
    <div class="container">
      <div class="section-header">
        <h2 class="gradient-text">Featured Projects</h2>
        <p class="section-description">A collection of my recent work and contributions</p>
      </div>

      <div class="projects-grid">
        <article v-for="project in projects" :key="project.id" class="project-card">
          <div class="project-content">
            <h3 class="project-title">{{ project.title }}</h3>
            <p class="project-description">{{ project.description }}</p>
            <div class="project-tech" v-if="project.technologies">
              <span v-for="tech in project.technologies" :key="tech" class="tech-tag">
                {{ tech }}
              </span>
            </div>
          </div>
          <div class="project-actions">
            <span v-for="link in project.links" :key="link" class="tech-tag">
              <a :href="link.link" target="_blank" rel="noopener" class="project-link">
                {{ link.name }}
                <span class="icon">→</span>
              </a>
          </span>
          </div>
        </article>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      projects: [
        {
          id: 1,
          title: 'RAG Chatbot',
          description: `Developed a context-aware conversational AI chatbot using LangChain, FastAPI, and Vue.js
Designed a modular 5-stage workflow (Query → Pre-Processing → Resource Validation → Response Generation → Clarification)
reducing API calls by 30%
Integrated LangChain components (RunnableBranch, LLMChain) to enhance dynamic logic control and response precision
Implemented proactive clarification logic that resolved over 10% of ambiguous queries.
Planned future enhancements including PostgreSQL-based cost optimization, real-time web search integration, and AWS migration`,
          technologies: ['Vue.js', 'FastAPI', 'LangChain'],
          links: [{name:'Frontend',link:'https://github.com/IamHassanAb/vue-fe-chatbot'},{name:'Backend',link:'https://github.com/IamHassanAb/chatbot_utility_service'}]
        },
        {
          id: 2, 
          title: 'Twitter Sentiment Analysis',
          description: 'Preprocessed and cleaned Twitter data for sentiment analysis. ' +
             'Implemented text vectorization using TF-IDF, Word2Vec, and GloVe. ' +
             'Trained and evaluated machine learning models on the vectorized data. ' +
             'Analyzed classifier effectiveness identifying the best-performing combination. ' +
             'Compared model performance across different vectorization techniques.',
          technologies: ['Tensorflow','nltk', 'pandas','numpy','Scikit-Learn'],
          links: [{name:'Colab Notebook',link:'https://colab.research.google.com/drive/1M_7WTi3p3scSvp46lY0tLr8qgEEo6Uwu'}]
        },
        {
          id: 3,
          title: 'ATM-External State Machine',
          description: 'Contributed to engineering services, harnessing state design pattern for the development of these services. ' +
             'Participated in developing 5+ critical services: Mini-Statements, UBPS, Credit-Card Payments, Demand Draft, and Customer Address Change. ' +
             'Collaborated with Stakeholder for the development of these services',
          technologies: ['Quarkus', 'Microservices'],
          links: [{name:'View Project',link:'/404'}]
        },
        {
          id: 4,
          title: 'Project Three',
          description: `Contributed to engineering frontend and backend APIs, achieving latency reduction through Dockerized deployments and code refactoring.
Participated in developing and delivering RESTful APIs (Flask/Quarkus) and Vue.js dashboards, accelerating transaction speeds and boosting user productivity.
Collaborated with Stakeholder implementing Agile methodologies to understand and develop requirements.
Developed with Stakeholder implementing Agile methodologies to understand and develop requirements.`,
          technologies: ['Vue.js', 'Flask','Quarkus'],
          links: [{name:'View Project',link:'/404'}]
        },
        {
          id: 5,
          title: 'Sudoku Solver',
          description: 'A brief description of Project Three. Implementing scalable backend architecture with modern tools.',
          technologies: ['OpenCV', 'Python', 'Keras'],
          links: [{name:'View Project',link:'/404'}]
        }
      ]
    };
  }
};
</script>

<style scoped>
.projects-section {
  padding: 6rem 0;
  background: #000000;
  min-height: 100vh;
}

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
  text-align: center;
  margin-bottom: 4rem;
}

.gradient-text {
  background: linear-gradient(135deg, #4348c8 0%, #ffffff 100%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.section-description {
  color: #888;
  font-size: 1.2rem;
  max-width: 600px;
  margin: 0 auto;
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.project-card {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 12px;
  padding: 2rem;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: 300px;
}

.project-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

.project-title {
  color: #fff;
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.project-description {
  color: #888;
  line-height: 1.6;
  margin-bottom: 1.5rem;
  text-align: justify;
}

.project-tech {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
  justify-content: center;
}

.project-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
  justify-content: center;
}

.tech-tag {
  background: rgba(67, 72, 200, 0.2);
  color: #4348c8;
  padding: 0.3rem 0.8rem;
  border-radius: 20px;
  font-size: 0.9rem;
  transition: color 0.3s ease;
}
.tech-tag:hover {
  color: #ffffff;
}
.project-link {
  color: #4348c8;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-weight: 500;
  transition: color 0.3s ease;
}

.project-link:hover {
  color: #ffffff;
}

.icon {
  transition: transform 0.3s ease;
}

.project-link:hover .icon {
  transform: translateX(5px);
}

@media (max-width: 768px) {
  .gradient-text {
    font-size: 2rem;
  }
  
  .projects-grid {
    grid-template-columns: 1fr;
  }
  
  .project-card {
    min-height: auto;
  }
}
</style>