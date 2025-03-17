from task1 import text_encryption

def main():
    key = "основыинформационнойбезопасности"
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя ,.:;-!"
    text = "Сегодня прекрасная погода. Проверяем работу шифра!"

    encrypted_text = text_encryption(text, key, alphabet)

    print("Исходный текст:")
    print(text)
    print("\nЗашифрованный текст:")
    print(encrypted_text)

if __name__ == "__main__":
    main()