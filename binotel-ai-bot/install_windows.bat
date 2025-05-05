@echo off
python -m pip install --upgrade pip
pip install flask requests python-dotenv
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install git+https://github.com/openai/whisper.git
echo ====================================
echo ✅ All dependencies installed
echo Run with: python run.py
echo ====================================
pause
