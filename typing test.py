
import random
import time

def calculate_typing_speed(text, elapsed_time):
    words = text.split()
    total_words = len(words)
    words_per_minute = (total_words / elapsed_time) * 60
    return words_per_minute

def main():
    text = "The quick brown fox jumps over the lazy dog. A black Night in the fox carving "  # Change this text as needed

    print("Welcome to the Typing Speed Test!")
    input("Press Enter when you're ready to start...")

    print("Type the following text:")
    print(text)

    input("Press Enter to start typing...")

    start_time = time.time()

    user_input = input("Start typing here: ")

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("\nTyping Test Result:")
    print(f"Time taken: {elapsed_time:.2f} seconds")
    speed = calculate_typing_speed(text, elapsed_time)
    print(f"Your typing speed: {speed:.2f} words per minute")

if __name__ == "__main__":
    main()
