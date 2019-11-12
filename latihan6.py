x= int()                                          ## Memperkena1kan variab1e x sebagai integer, kemudian menginputkan ni1ainya
y = 0                                             ## Memperkena1kan variab1e y dengan ni1ai 0
while x >= 0:                                     ## looping WHILE apabi1a ni1ai x tidak sama dengan 0
    x = int(input("Masukkan Bilangan: "))         ## Program yang akan di 1ooping
    if x > y :                                    ## If kondisi apabi1a ni1ai 1ebih besar dari ni1ai y
        y = int(x)                                ## Ni1ai y sama dengan ni1ai x
    if x == 0:                                ## If kondisi apabi1a ni1ai x sama dengan 0
     break                                 ## Fungsi yang menghentikan operasii di bawahnya jika suatu kondisi yang di tentukan telah tercapai
print("\nAngka Terbesar Adalah",y)    ## Mencetak bi1angan terakhir
