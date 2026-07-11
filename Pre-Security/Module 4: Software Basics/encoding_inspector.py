"""
Data Encoding Inspector

This script supports my Data Encoding notes by showing how text characters
are represented as numbers and bytes using ASCII, Unicode, UTF-8, UTF-16,
and UTF-32.
"""


def show_character_details(text):
    print(f"Original text: {text}")
    print("-" * 50)

    for character in text:
        print(f"Character: {character}")
        print(f"Unicode code point: U+{ord(character):04X}")

        try:
            print(f"ASCII: {character.encode('ascii')}")
        except UnicodeEncodeError:
            print("ASCII: Not supported")

        print(f"UTF-8: {character.encode('utf-8')}")
        print(f"UTF-16: {character.encode('utf-16')}")
        print(f"UTF-32: {character.encode('utf-32')}")
        print("-" * 50)


def show_gibberish_example():
    print("\nGibberish Example")
    print("-" * 50)

    original_text = "Cybersecurity café"
    encoded_text = original_text.encode("utf-8")

    print(f"Original text: {original_text}")
    print(f"UTF-8 bytes: {encoded_text}")

    try:
        decoded_incorrectly = encoded_text.decode("ascii")
        print(f"Decoded as ASCII: {decoded_incorrectly}")
    except UnicodeDecodeError:
        print("Decoded as ASCII: Error - ASCII cannot read all UTF-8 characters.")


if __name__ == "__main__":
    sample_text = input("Enter text to inspect, such as Hello or 🔐: ").strip()

    if sample_text:
        show_character_details(sample_text)
    else:
        show_character_details("Hello 🔐")

    show_gibberish_example()
