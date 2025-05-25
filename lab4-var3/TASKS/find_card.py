import multiprocessing as mp
import hashlib
from .io_operations import write_json
from tqdm import tqdm


class FindCard:

    @staticmethod
    def number_of_cores() -> int:
        """
        Defines the available number of processes
        :return: number of processes
        """
        return mp.cpu_count()

    @staticmethod
    def hashing_num(num: str) -> str:
        """
        Hashes the specified string
        :param num: num card
        :return:hash
        """
        return hashlib.sha1(num.encode()).hexdigest()

    @staticmethod
    def generate_cards_hash(
        bin: str, last_digits: str, start: int, end: int, hash: str
    ) -> tuple[str, str]:
        """
        Generate card numbers in the specified range.
        :param bin:bin
        :param last_digits:last 4 digits
        :param start:start
        :param end:end
        :param hash: hash
        :return: card, rand hash
        """
        for middle in range(start, end):
            card = f"{bin}{middle:06}{last_digits}"
            rand_hash = FindCard.hashing_num(card)
            if rand_hash == hash:
                return card, rand_hash
        return None

    @staticmethod
    def find_card_parallel(bins: list[str], last_digits: str, target_hash: str, cores: int) -> str:
        """
        Searches for the appropriate card number using multiprocessing.
        :param bins: bins
        :param last_digits:last 4 digits
        :param target_hash: target hash
        :param cores:cores
        :return: the number of the found card
        """
        total_range = 10**6
        chunk_size = total_range // cores

        with mp.Pool(processes=cores) as pool:
            results = []
            for bin in bins:
                for i in range(cores):
                    start = i * chunk_size
                    end = start + chunk_size if i != cores - 1 else total_range
                    results.append(
                        pool.apply_async(
                            FindCard.generate_cards_hash,
                            (bin, last_digits, start, end, target_hash),
                        )
                    )
            for result in results:
                found = result.get()
                if found:
                    pool.terminate()
                    return found[0]

        return None

    @staticmethod
    def serialization_res(bins: list[str], last_digits: str, target_hash: str, cores: int, filepath:str)->None:
        """
        Serialize the number of the found card
        :param bins: bins
        :param last_digits:last 4 digits
        :param target_hash: target hash
        :param cores:cores
        :param filepath: filepath
        :return: None
        """
        try:
            res =FindCard.find_card_parallel(bins,last_digits,target_hash,cores)
            write_json(filepath,{"card_number": res})
        except Exception as exc:
            raise Exception(f"Error serializing private key: {exc}")