import multiprocessing as mp
import hashlib


class FindCard:

    @staticmethod
    def number_of_cores() -> int:
        return mp.cpu_count()

    @staticmethod
    def hashing_num(num: str) -> str:
        return hashlib.sha1(num.encode()).hexdigest()

    @staticmethod
    def generate_valid_cards_hash(bin: str, last_digits: str, start: int, end: int, hash:str) -> tuple[str, str]:

        for middle in range(start, end):
            card = f"{bin}{middle:06}{last_digits}"
            rand_hash=FindCard.hashing_num(card)
            if rand_hash==hash:
                return  card, rand_hash
        return None

    @staticmethod
    def find_card_parallel(bins: list[str], last_digits: str, target_hash: str) -> str:
        cores = FindCard.number_of_cores()
        total_range = 10**6
        chunk_size = total_range // cores

        with mp.Pool(processes=cores) as pool:
            results = []
            for bin in bins:
                for i in range(cores):
                    start = i * chunk_size
                    end = start + chunk_size if i != cores - 1 else total_range
                    results.append(pool.apply_async(FindCard.generate_valid_cards_hash, (bin, last_digits, start, end,target_hash)))
            for result in results:
                found = result.get()
                if found:
                    pool.terminate()
                    return found[0]


        return None


