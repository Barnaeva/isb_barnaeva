from .find_card import FindCard
import numpy as np
import time



class MeasuringTime:

    @staticmethod
    def meas_time(bins: list[str], last_digits: str, target_hash: str)->list[tuple[int,int]]:
        num_cor = FindCard.number_of_cores()
        num_cor*=1.5
        time_res=[]
        for i in range (1,int (num_cor+1)):
            time_start=time.time()
            FindCard.find_card_parallel(bins, last_digits, target_hash, i)
            time_end=time.time()
            all_time=time_end-time_start
            time_res.append((i, all_time))

        return time_res

