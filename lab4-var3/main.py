from TASKS.find_card import FindCard
from TASKS.alg_luhn import AlgLuhn
from TASKS.measuring_time import MeasuringTime
if __name__=='__main__':
    hash='bf67709b1216cb66038f3ae5ad2b4c066be03cbb'
    bins=["220220", "220100"]
    last="5688"
    cores = FindCard.number_of_cores()
    card=FindCard.find_card_parallel(bins,last,hash,cores)
    print(card)
    AlgLuhn.print_res(card)
    time_res=MeasuringTime.meas_time(bins,last,hash)
    print(time_res)