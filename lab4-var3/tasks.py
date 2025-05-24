import multiprocessing as mp
import hashlib


class CardProcessor:

    @staticmethod
    def number_of_cores() -> int:
        return mp.cpu_count()

    @staticmethod
    def alg_luhn(num_card: str) -> bool:
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
    def hashing_num(num: str) -> str:
        return hashlib.sha1(num.encode()).hexdigest()

    @staticmethod
    def generate_valid_cards_hash(bin: str, last_digits: str) -> list[tuple[str, str]]:
        hash_valid_cards = []
        for middle in range(0, 10 ** 6):
            card = f"{bin}{middle:06}{last_digits}"
            if CardProcessor.alg_luhn(card):
                hash_valid_cards.append((card, CardProcessor.hashing_num(card)))
        return hash_valid_cards

    @staticmethod
    def find_card_parallel(bin: str, last_digits: str, target_hash: str) -> str:
        cores = CardProcessor.number_of_cores()

        with mp.Pool(processes=cores) as pool:
            result = pool.apply_async(CardProcessor.generate_valid_cards_hash, (bin, last_digits))

            cards_and_hashes = result.get()

            for card, card_hash in cards_and_hashes:
                if card_hash == target_hash:
                    pool.terminate()
                    return card

        return None