/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        accent: {
          DEFAULT: '#00736a',
          hover: '#008a7f',
          glow: 'rgba(0,115,106,0.15)',
          dark: '#005c54',
        },
        surface: '#0f1629',
        card: '#1a1f2e',
        elevated: '#1e293b',
        border: '#1e293b',
        'border-light': '#2a3a60',
        muted: '#5b6f99',
        'text-secondary': '#94a3c8',
        'text-primary': '#e8edf5',
      },
      fontFamily: {
        sans: ['Inter', 'Geist', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
