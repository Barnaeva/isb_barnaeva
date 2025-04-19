from TESTS.tests import frequency_bitwise_test, identical_consecutive_bits

def main():
    d="111100101001010001110101010101010"
    print(frequency_bitwise_test(d))
    print(identical_consecutive_bits(d))


if __name__ == "__main__":
    main()