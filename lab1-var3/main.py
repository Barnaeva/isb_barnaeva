from TASK1.task1 import text_encryption
from TASK2.task2 import calculate_symbol_frequency, make_key, decryption_cod3
from io_operations import read_json, read_file, write_file, write_json


def task1() -> None:
    task1_files = read_json("settings.json")["TASK1"]

    key = read_json(task1_files["key"])
    alphabet = read_json(task1_files["alphabets"])["alphabet"]
    text1 = read_file(task1_files["plain_text"])

    encrypted_text = text_encryption(text1, key, alphabet)
    write_file(task1_files["encrypted_text"], encrypted_text)


def task2() -> None:
    task2_files = read_json("settings.json")["TASK2"]

    text2 = read_file(task2_files["plain_text"])

    freq = calculate_symbol_frequency(text2)
    write_json(task2_files["frequency"], freq)

    freq_alp = read_json(task2_files["alp_freq"])
    key = make_key(freq_alp, freq)
    write_json(task2_files["key"], key)

    key = read_json(task2_files["key"])
    decrypted_cod3_text = decryption_cod3(text2, key)
    write_file(task2_files["decrypted_text"], decrypted_cod3_text)


def main():
    try:
        task1()
        task2()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
