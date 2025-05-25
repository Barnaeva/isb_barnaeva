class AlgLuhn:

    @staticmethod
    def alg_luhn(num_card: str) -> bool:
        """
        Implements the luhn algorithm
        :param num_card: num card
        :return: true or false
        """
        total = 0
        for i, digit in enumerate(reversed(num_card)):
            num = int(digit)
            if i % 2 == 1:
                num *= 2
                if num > 9:
                    num -= 9
            total += num
        return total % 10 == 0

    @staticmethod
    def print_res(num_card: str) -> None:
        """
        Print res alg Luhn
        :param num_card:num card
        :return: None
        """
        if AlgLuhn.alg_luhn(num_card):
            print("This card number is valid")
        else:
            print("This card number is not valid")
