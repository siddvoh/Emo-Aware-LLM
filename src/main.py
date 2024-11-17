from dotenv import load_dotenv
from vision import capture_image, analyze_expression
from audio import speak, listen
from ai import get_response
from utils import setup_environment

def main():
    # Load environment variables and setup platform-specific configs
    load_dotenv()
    setup_environment()
    
    # Main flow
    frame = capture_image()
    if frame is not None:
        emotion = analyze_expression(frame)
        if emotion:
            speak(f"Wow, you look {emotion}!")
            user_prompt = listen()
            if user_prompt:
                combined_prompt = f"I am {emotion}. {user_prompt}"
                response = get_response(combined_prompt)
                if response:
                    print(f"Assistant: {response}")
                    speak(response)
        else:
            print("Could not determine facial expression.")
            speak("Could not determine facial expression.")

if __name__ == "__main__":
    main()