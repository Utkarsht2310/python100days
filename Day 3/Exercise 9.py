# Write a program to pronounce list names using win32 API.

import win32com.client


def pronounce_names(names):
    """
    Pronounce each name in the given list using the Windows SAPI Text-to-Speech engine.
    """
    # Create a voice object using the Speech API
    speaker = win32com.client.Dispatch("SAPI.SpVoice")

    for name in names:
        print(f"Pronouncing: {name}")
        speaker.Speak(name)


if __name__ == "__main__":
    # List of names to pronounce
    names_to_pronounce = [
        "Alice",
        "Bob",
        "Charlotte",
        "David",
        "Emily"
    ]

    print("Starting to pronounce names...\n")
    pronounce_names(names_to_pronounce)
    print("\nFinished pronouncing names!")
