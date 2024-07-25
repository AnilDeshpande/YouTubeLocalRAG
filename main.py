#Run this if it is main file
import os
from talk_via_ollama import talk_via_ollama


def main():
    os.system('clear')
    print("Start Interacting with Ollama")
    talk_via_ollama("preprocessed_videos_meta_data.txt")


if __name__ == "__main__":
    main()
