def calculate_symbol_frequency(data: str) -> dict[str, float]:
    """
    Calculate symbol frequency in the given text.

    :param data: Input text.
    :return: Dictionary of symbols and their frequencies.
    """
    try:

        result = {}

        for symbol in data:
            if symbol == "\n":
                continue
            result[symbol] = result.get(symbol, 0) + 1

        for symbol, count in result.items():
            result[symbol] = count / len(data)

        return dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
    except Exception as e:
        print(f"An error occurred while calculating symbol frequency: {e}")
        return {}


def make_key(freq_alp: dict[str, float], freq_task: dict[str, float]) -> dict[str, str]:
    """
    Create a mapping of symbols based on their frequencies.

    :param freq_alp: Frequencies of alphabet symbols.
    :param freq_task: Frequencies of task symbols.
    :return: Mapping of task symbols to alphabet symbols.
    """
    result = {}

    for alp_symb, task_symb in zip(freq_alp.keys(), freq_task.keys()):
        result[task_symb] = alp_symb

    return result


def decryption_cod3(data: str, key: dict[str, str]) -> str:
    """
    Replace symbols in the data using the provided key.

    :param data: Input text.
    :param key: Dictionary mapping symbols to replacements.
    :return: Modified text.
    """
    result = ""
    for symbol in data:
        result += key.get(symbol, symbol)
    return result
