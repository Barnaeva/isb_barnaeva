class AlgLuhn:

    @staticmethod
    def alg_luhn(num_card: str)->bool:
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
    def print_res(num_card: str):
        if AlgLuhn.alg_luhn(num_card):
            print("This card number is valid")
        else:
            print("This card number is not valid")