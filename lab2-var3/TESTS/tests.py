import math


def frequency_bitwise_test(sequence: str) -> float:
    """
    The function performs a frequency bitwise test for a given sequence

    :param sequence: Binary string
    :return: P-value
    """
    s_n = 0
    n=len(sequence)
    for val in sequence:
        s_n += 1 / math.sqrt(n) if val == "1" else -1 / math.sqrt(n)

    p_value = math.erfc(abs(s_n) / math.sqrt(2))
    return p_value

def identical_consecutive_bits(sequence: str) -> float:
    """
    The function performs a test for the same consecutive bits for a given string
    :param sequence: Binary string
    :return: P-value
    """
    n = len(sequence)
    s_n = sum(1 for val in sequence if val == '1') / n

    if abs(s_n - 0.5) >= 2 / math.sqrt(n):
        return 0.0

    v_n = sum(1 for i in range(n-1) if sequence[i] != sequence[i+1])
    p_value=math.erfc((abs(v_n - 2*n*s_n*(1-s_n)))/(2*math.sqrt(2*n)*s_n*(1-s_n)))

    return p_value