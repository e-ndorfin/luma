# Luma - AI-Powered Meditation Generator

Create personalized 10-minute guided meditation sessions based on daily experiences using AI.

## ✨ Features

- **Personalized Meditation Scripts** - Generates custom guided meditations from daily journal input
- **AI-Powered Insights** - Uses Cohere's NLP to analyze mood and stress levels
- **Clean, Modern UI** - Beautiful purple gradient interface with loading animations
- **Responsive Design** - Works across all devices

## 📁 Project Structure

```
luma/
├── frontend/              # React frontend application
│   ├── public/            # Static assets
│   ├── src/               # Source code
│   │   ├── components/    # React components
│   │   │   ├── Loading.jsx       # Loading animation component
│   │   │   ├── Loading.css       # Styling for loading animation
│   │   │   ├── MeditationInput.jsx # Input form component
│   │   ├── App.jsx        # Main application component
│   │   ├── App.css        # Application styling
│   │   ├── main.jsx       # Entry point
│   │   ├── index.css      # Global styling
│   ├── index.html         # HTML template
│   ├── package.json       # Frontend dependencies
│   └── vite.config.js     # Vite configuration
├── backend/               # Flask backend (planned)
└── README.md             # Documentation
```

## 🚀 Quick Start

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### Backend (Coming Soon)
```bash
cd backend
pip install -r requirements.txt
python app.py
```

## 🔜 Roadmap

- **MP3 Generation** (Coming Soon): Convert scripts to audio with text-to-speech
- **Voice Customization**: Choose guide voice tone (calm/soothing/energetic)
- **Web Interface**: React frontend with meditation player
- **Session History**: Browse previous meditations

## ⚙️ Requirements

- Cohere API Key (free tier available)
- Python 3.10+
- Flask backend (current)
- React frontend (planned)

🔒 **Environment**: Create `.env` with `COHERE_API_KEY` in backend folder

> **Note**: Current version outputs text scripts - audio MP3 generation coming in next version!

# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react/README.md) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## Expanding the ESLint configuration

If you are developing a production application, we recommend using TypeScript and enable type-aware lint rules. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) to integrate TypeScript and [`typescript-eslint`](https://typescript-eslint.io) in your project.


