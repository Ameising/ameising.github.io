/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./htmx/**/*.py", "./website/**/*.py", "./resources/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/typography'),
    require("daisyui"),
  ],
  daisyui: {
    themes: ["light", "dark", ],
  },
}
