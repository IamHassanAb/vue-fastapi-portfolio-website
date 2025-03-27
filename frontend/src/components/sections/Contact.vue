<template>
  <section id="contact" class="contact-section">
    <div class="container">
      <div class="section-header">
        <h2 class="gradient-text">Get In Touch</h2>
        <p class="section-description">Have a question or want to work together? Let's connect!</p>
      </div>

      <div class="contact-content">
        <div class="contact-info">
          <div class="info-item">
            <i class="fas fa-envelope"></i>
            <a href="mailto:hassanab220.work@gmail.com">Email Me</a>
          </div>
          <div class="info-item">
            <i class="fab fa-linkedin"></i>
            <a href="https://www.linkedin.com/in/hassan-abbas-848549209/" target="_blank" rel="noopener">LinkedIn Profile</a>
          </div>
          <div class="info-item">
            <i class="fab fa-github"></i>
            <a href="https://github.com/IamHassanAb" target="_blank" rel="noopener">GitHub Profile</a>
          </div>
        </div>

        <form class="contact-form" @submit.prevent="submitForm('api')">
          <div class="form-group">
            <input 
              type="text" 
              id="name" 
              v-model="name" 
              placeholder="Your Name"
              required 
            />
          </div>
          
          <div class="form-group">
            <input 
              type="email" 
              id="email" 
              v-model="email" 
              placeholder="Your Email"
              required 
            />
          </div>
          
          <div class="form-group">
            <textarea 
              id="message" 
              v-model="message" 
              placeholder="Your Message"
              rows="5"
              required
            ></textarea>
          </div>

          <button type="submit" class="submit-btn">
            Send Message
            <span class="btn-icon">→</span>
          </button>
        </form>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      name: '',
      email: '',
      message: ''
    };
  },
  methods: {
    async submitForm(choice) {

      if (!this.name || !this.email || !this.message) {
        return this.showError('Please fill in all fields');
      }

      this.isSubmitting = true;
      
      try {
        if (choice == "api"){
          // Use the correct endpoint (replace with your actual backend URL)
          const API_URL = 'http://127.0.0.1:8000/send-email'; // Must match your FastAPI address
          
          const response = await fetch(API_URL, {
            method: 'POST',
            mode: 'cors', // Explicitly enable CORS mode
            credentials: 'include', // Only if using cookies/sessions
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              From: this.email,
              Body: this.message,
              Subject: 'New Contact Form Submission'
            })
          });

          if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || `HTTP error! status: ${response.status}`);
          }

          const data = await response.json();
          this.showSuccess(data.message || 'Message sent successfully!');
          this.resetForm();
        } else {
            const mailtoLink = `mailto:${'hassanab220.work@gmail.com'}?subject=New Contact Form Submission&body=From: ${this.email}%0D%0A%0D%0A${encodeURIComponent(this.message)}`;
            window.location.href = mailtoLink;
        }
          
      } catch (error) {
        console.error('Error:', error);
        this.showError(error.message || 'Failed to send message. Please try again later.');
      } finally {
        this.isSubmitting = false;
      }
    },
    resetForm() {
      this.name = '';
      this.email = '';
      this.message = '';
    },
    showSuccess(message) {
      // Consider using a toast notification instead
      alert(message);
    },
    showError(message) {
      alert(message);
    }
  }
};
</script>

<style scoped>
.contact-section {
  padding: 6rem 0;
  background: #000000;
  min-height: 100vh;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
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

.contact-content {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 4rem;
  align-items: start;
}

.contact-info {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.info-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  color: #fff;
}

.info-item a {
  color: #fff;
  text-decoration: none;
  transition: color 0.3s ease;
}

.info-item a:hover {
  color: #4348c8;
}

.contact-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.form-group {
  position: relative;
}

input,
textarea {
  width: 100%;
  padding: 1rem;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  color: #fff;
  font-size: 1rem;
  transition: all 0.3s ease;
}

input:focus,
textarea:focus {
  outline: none;
  border-color: #4348c8;
  background: rgba(255, 255, 255, 0.1);
}

.submit-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 1rem 2rem;
  background: #4348c8;
  color: #fff;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.submit-btn:hover {
  background: #5357d6;
  transform: translateY(-2px);
}

.btn-icon {
  transition: transform 0.3s ease;
}

.submit-btn:hover .btn-icon {
  transform: translateX(5px);
}

@media (max-width: 768px) {
  .contact-content {
    grid-template-columns: 1fr;
    gap: 2rem;
  }

  .contact-info {
    order: 2;
  }

  .contact-form {
    order: 1;
  }

  .gradient-text {
    font-size: 2rem;
  }
}
</style>