from TASK1.task1 import text_encryption
from TASK2.task2 import calculate_symbol_frequency, make_key, decryption_cod3
from io_operations import read_json, read_file, write_file, write_json


def task1() -> None:
    key = read_json("TASK1/key.json").get("key")
    alphabet = read_json("TASK1/alphabet.json").get("alphabet")
    text1 = read_file("TASK1/text.txt")

    encrypted_text = text_encryption(text1, key, alphabet)
    write_file("TASK1/encryption_text.txt", encrypted_text)


def task2() -> None:
    text2 = read_file("TASK2/cod3.txt")

    freq = calculate_symbol_frequency(text2)
    write_json("TASK2/frequency.json", freq)

    freq_alp = read_json("TASK2/alphabet_frequency.json")
    key = make_key(freq_alp, freq)
    write_json("TASK2/key.json", key)

    key = read_json("TASK2/key.json")
    decrypted_cod3_text = decryption_cod3(text2, key)
    write_file("TASK2/decryption_text.txt", decrypted_cod3_text)


def main():
    try:
        task1()
        task2()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
