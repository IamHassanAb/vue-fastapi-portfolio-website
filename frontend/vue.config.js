const { basename } = require('path');

module.exports = {
  publicPath: process.env.NODE_ENV === "production" ? "/vue-fastapi-portfolio-website/" : "/", // Change to relative path
  lintOnSave: false,
  devServer: {
    port: 8080,
    open: true
  },
  configureWebpack: {
    resolve: {
      alias: {
        '@': require('path').resolve(__dirname, 'src')
      }
    }
  }
};