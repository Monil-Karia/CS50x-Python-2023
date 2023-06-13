def total(galleons , sickel , knuts):
    return(galleons * 17 + sickel) * 29 + knuts

coins_list = [100, 50 ,25]

coins_dict= {"galleons": 100 , "sickel": 50  , "knuts": 25}

print(total(*coins_list),"knuts")  #here we can see that * can make unpacking of the total here 

print(total(**coins_dict),"knuts")  #here we can see that ** can make unpacking of the total here 