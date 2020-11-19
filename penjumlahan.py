def penjumlahan (n) :
    hasil = 0 
    for x in n :
        hasil = hasil + x
    return hasil

list = [8, 2, 3, 0, 7]
print (list)
print ('Hasil penjumlahan', penjumlahan(list))