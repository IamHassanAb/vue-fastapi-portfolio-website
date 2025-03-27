# Data Scientist Portfolio

This is a portfolio website created for a Data Scientist using Vue.js with a Neumorphism design style. The portfolio showcases the skills, projects, and contact information of the data scientist.

## Project Structure

The project is organized as follows:

```
data-scientist-portfolio
├── public
│   ├── index.html          # Main HTML file for the application
│   └── favicon.ico         # Favicon for the portfolio website
├── src
│   ├── assets
│   │   └── styles
│   │       └── neumorphism.css  # CSS styles implementing Neumorphism design
│   ├── components
│   │   ├── About.vue       # Component displaying information about the data scientist
│   │   ├── Contact.vue     # Component providing contact information
│   │   ├── Home.vue        # Component serving as the landing page
│   │   └── Projects.vue    # Component listing the data scientist's projects
│   ├── views
│   │   ├── AboutView.vue   # View using the About component
│   │   ├── ContactView.vue # View using the Contact component
│   │   ├── HomeView.vue    # View using the Home component
│   │   └── ProjectsView.vue # View using the Projects component
│   ├── App.vue             # Root component of the Vue application
│   └── main.js             # Entry point of the Vue application
├── package.json            # Configuration file for npm
├── README.md               # Documentation for the project
└── vue.config.js           # Configuration settings for the Vue CLI
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd data-scientist-portfolio
   ```

2. **Install dependencies:**
   ```
   npm install
   ```

3. **Run the application:**
   ```
   npm run serve
   ```

4. **Open your browser and navigate to:**
   ```
   http://localhost:8080
   ```

## Features

- **Neumorphism Design:** The portfolio utilizes a modern Neumorphism design style for a sleek and contemporary look.
- **Responsive Layout:** The website is designed to be responsive and works well on various screen sizes.
- **Showcase Projects:** A dedicated section to display projects with descriptions and links.
- **Contact Form:** A contact section to allow visitors to reach out.

## License

This project is licensed under the MIT License.