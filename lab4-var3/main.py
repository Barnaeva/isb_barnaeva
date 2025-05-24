from TASKS.FindCard import FindCard
from TASKS.AlgLuhn import AlgLuhn
if __name__=='__main__':
    hash='bf67709b1216cb66038f3ae5ad2b4c066be03cbb'
    bins=["220220", "220100"]
    last="5688"
    card=FindCard.find_card_parallel(bins,last,hash)
    print(card)
    AlgLuhn.print_res(card)