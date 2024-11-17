import os
import platform

def setup_environment():
    # Suppress warnings for all platforms
    os.environ['PYTHONWARNINGS'] = 'ignore'
    
    # Set ALSA configuration only on Raspberry Pi
    if platform.machine().startswith('arm'):
        os.environ['ALSA_PCM_CARD'] = os.getenv('ALSA_PCM_CARD', '1')
        os.environ['ALSA_PCM_DEVICE'] = os.getenv('ALSA_PCM_DEVICE', '3')