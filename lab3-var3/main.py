from hybrid_cryptosystem.HybridSyst import generate_keys, encrypt_file, decrypt_file
from hybrid_cryptosystem.io_operations import read_json


def case_generate_keys(settings):
    generate_keys(
        settings["encrypted_key"], settings["public_key"], settings["private_key"]
    )
    print("Keys generated")


def case_encrypt(settings):
    encrypt_file(
        settings["input_dir"],
        settings["private_key"],
        settings["encrypted_key"],
        settings["encrypted_dir"],
    )
    print(f"Encrypted text")


def case_decrypt(settings):
    decrypt_file(
        settings["encrypted_dir"],
        settings["private_key"],
        settings["encrypted_key"],
        settings["decrypted_dir"],
    )
    print(f"Decrypted text")


def case_change_settings(settings):
    new_file = input(
        "\nEnter new settings file name (or press Enter to keep current): "
    )
    if new_file:
        try:
            new_settings = read_json(new_file)
            settings.update(new_settings)
            print("Settings updated!")
        except:
            print("Error loading settings file")


def show_menu():
    print("\n" + "=" * 30)
    print("  HYBRID CRYPTO SYSTEM  ".center(30, "="))
    print("=" * 30)
    print("1. Generate keys")
    print("2. Encrypt default file")
    print("3. Decrypt default file")
    print("4. Change settings file")
    print("0. Exit")
    print("=" * 30)


def main():
    settings = read_json("settings.json")

    while True:
        show_menu()
        choice = input("Select operation: ")

        if choice == "1":
            case_generate_keys(settings)
        elif choice == "2":
            case_encrypt(settings)
        elif choice == "3":
            case_decrypt(settings)
        elif choice == "4":
            case_change_settings(settings)
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
