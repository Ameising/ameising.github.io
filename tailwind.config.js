/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./content/**/*.{html,js,md}", "./themes/**/*.{html,js,md}"],
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
