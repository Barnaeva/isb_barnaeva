def calculate_symbol_frequency(data: str) -> dict[str, float]:
    """
    Calculates the frequency of each symbol in the given text.

    :param data: The input text.
    :return: A dictionary where keys are symbols and values are their frequencies.
    """
    if not data:
        return {}

    result = {}

    for symbol in data:
        if symbol in result:
            result[symbol] += 1
        else:
            result[symbol] = 1

    for symbol, count in result.items():
        result[symbol] = count / len(data)


    return dict(sorted(result.items(), key=lambda item: item[1], reverse=True))

def make_key(freq_alp:dict[str,float],freq_task: dict[str,float])->dict[str,str]:
    """

    :param freq_alp:
    :param freq_task:
    :return:
    """
    result={}

    for alp_symb,task_symb in zip(freq_alp.keys(),freq_task.keys()):
        result[task_symb]=alp_symb

    return result

def swap(data: str, key: dict[str,str]) -> str:
    """
    Replaces symbols in the data using the provided key.

    :param data: The input text.
    :param key: A dictionary mapping symbols to their replacements.
    :return: The modified text.
    """
    result = ""
    for symbol in data:
        result += key.get(symbol,symbol)
    return result
