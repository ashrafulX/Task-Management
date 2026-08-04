/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html", //root label
    ".//tempaltes/**/*.html", //inside apps
    "./static/**/*.js",
    "./**/templates/**/*.html", // safer for Django apps
  
    
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

