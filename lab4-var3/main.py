from TASKS.find_card import FindCard
from TASKS.alg_luhn import AlgLuhn
from TASKS.measuring_time import MeasuringTime

if __name__ == "__main__":
    hash = "bf67709b1216cb66038f3ae5ad2b4c066be03cbb"
    bins = ["220220", "220100"]
    last = "5688"
    filepath="res.json"
    cores = FindCard.number_of_cores()
    card=FindCard.find_card_parallel(bins,last,hash,cores)
    AlgLuhn.print_res(card)
    FindCard.serialization_res(bins,last,hash,cores,filepath)

    time_res = MeasuringTime.meas_time(bins, last, hash)
    print(time_res)
    MeasuringTime.plot_time(time_res)
