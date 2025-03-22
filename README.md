# Luma - AI-Powered Meditation Generator

Create personalized 10-minute guided meditation sessions based on daily experiences using AI.

## ✨ Features

- **Personalized Meditation Scripts** - Generates custom guided meditations from daily journal input
- **AI-Powered Insights** - Uses Cohere's NLP to analyze mood and stress levels
- **Session Logging** - Automatically stores all generated sessions in `responses.txt`
- **API Ready** - CORS-enabled endpoint for easy frontend integration

## 🚀 Quick Start

1. **Setup Backend**
```bash
cd backend
echo "COHERE_API_KEY=your_cohere_key_here" > .env
pip install -r requirements.txt
python app.py
```

2. **Generate Meditation** (Example)
```bash
curl -X POST http://localhost:5000/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "I had a stressful day with 3 back-to-back meetings and missed lunch. Need to relax."
  }'
```

3. **Sample Response**
```json
{
  "response": "Begin by finding a quiet space... [10-minute meditation script]"
}
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


