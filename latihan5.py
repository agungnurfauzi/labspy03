n=int(input("Masukan Nilai N: "))            ## Memperkena1kan variab1e n sebagai integer, kemudian menginputkan n1lainya

from random import random                    ## Mengimport fungsi random
a=random()                                 ## Memperkena1kan variab1e a sebagai random

jumlah=n+1                                   ## Juum1ah = variab1e n + 1
start=1                                      ## Dimu1ai dari angka 1
stop=jumlah                                  ## Berhenti ketika variab1e jum1ah sesudah sesuai
step=1                                       ## Stop angka 1

for i in range (start,stop,step):            ## Peru1angan i dengan ni1ai awa1 variab1e start, ni1ai akhir variab1e stop dan step variab1e step
    print("data ke : ",i,"-",(a))            ## Mencetak hasi1
    print("\nDone")