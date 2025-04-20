from TESTS.tests import frequency_bitwise_test, identical_consecutive_bits,longest_tes_sequence

def main():
    d="111100101001010001110101010101010"
    print(frequency_bitwise_test(d))
    print(identical_consecutive_bits(d))
    print(longest_tes_sequence(d))


if __name__ == "__main__":
    main()