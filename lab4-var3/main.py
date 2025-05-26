from TASKS.find_card import FindCard
from TASKS.alg_luhn import AlgLuhn
from TASKS.io_operations import read_json, write_json
from TASKS.measuring_time import MeasuringTime


def find_card_action(settings: dict) -> None:
    """
    Find a card by its hash value using parallel processing.
    :param settings: settings
    :return: None
    """ ""
    try:
        bins = settings["bins"]
        last_digits = settings["last_four_digits"]
        target_hash = settings["hash"]
        filepath = settings["filepath"]
        cores = FindCard.number_of_cores()

        card = FindCard.find_card_parallel(bins, last_digits, target_hash, cores)

        if card:
            print(f"\nFound card: {card}")
            FindCard.serialization_res(bins, last_digits, target_hash, cores, filepath)
        else:
            print("\nCard not found")
    except Exception as e:
        print(f"\nError: {e}")


def measure_performance_action(settings: dict) -> None:
    """
    Measure search performance with different core counts.
    :param settings: settings
    :return: None
    """

    try:
        print("\nMeasuring performance...")

        bins = settings["bins"]
        last_digits = settings["last_four_digits"]
        target_hash = settings["hash"]

        times_result = MeasuringTime.meas_time(bins, last_digits, target_hash)
        MeasuringTime.plot_time(times_result)
    except Exception as e:
        print(f"\nError: {e}")


def validate_card_action() -> None:
    """Validate a card number using Luhn algorithm."""
    card = input("\nEnter card number to validate: ")
    if AlgLuhn.alg_luhn(card):
        print("Card is valid")
    else:
        print("Card is invalid")


def change_settings_action() -> dict:
    """
    Change application settings by loading a new configuration file.
    :param settings: file name
    :return:
    """
    new_file = input("\nEnter settings filename (or press Enter to cancel): ")
    if new_file:
        try:
            settings = read_json(new_file)
            print("Settings updated!")
            return settings

        except Exception as e:
            print(f"Error loading settings: {e}")


def show_menu() -> None:
    """Display the main menu options."""
    print("\n" + "=" * 40)
    print("  BANK CARD SEARCH SYSTEM  ".center(40, "="))
    print("=" * 40)
    print("1. Find card by hash")
    print("2. Measure performance")
    print("3. Validate card (Luhn algorithm)")
    print("4. Change settings")
    print("0. Exit")
    print("=" * 40)


def main() -> None:
    """Main application entry point."""
    settings = read_json("settings.json")

    while True:
        show_menu()
        choice = input("Select option: ")

        match choice:
            case "1":
                find_card_action(settings)
            case "2":
                measure_performance_action(settings)
            case "3":
                validate_card_action()
            case "4":
                new_settings = change_settings_action()
                settings = new_settings
            case "0":
                print("Exiting...")
                break
            case _:
                print("Invalid selection")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
