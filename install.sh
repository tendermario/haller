#!/usr/bin/env zsh
. ./.venv/bin/activate


FOLDER=.venv

# Create venv if it doesnt exist
if [[ -d "$FOLDER" ]]; then
  echo "Welcome back :)"
else
  echo "Creating venv"
  virtualenv -p python3 $FOLDER
fi

# Enter venv
source .venv/bin/activate

# Install pyAudio dependency
brew install portaudio

# Install pyAudio with references to portaudio available... or something like that
pip install --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' pyaudio

# Or try requirements.lock for a deterministic flavour. Tested with python3.8.
pip install -r requirements.txt

echo "******************"
echo "Install complete"
