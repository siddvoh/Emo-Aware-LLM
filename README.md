# Emo-Aware-LLM

An emotion-aware AI assistant that uses facial recognition to detect emotions and provide contextual responses using LLMs.

## Prerequisites

- Python 3.8+
- Webcam
- Microphone
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Emo-Aware-LLM.git
cd Emo-Aware-LLM
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Add your OpenAI API key to .env file
```

## Usage

Run the assistant:
```bash
python src/main.py
```

## License

MIT License