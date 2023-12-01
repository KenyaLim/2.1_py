def tarif_tol(jarak, golongan=2):
  total = 0
  jarakAwal = 50
  jarakSekarang = 0
  if golongan == 1:
    if jarak >= 50:
      total += 10000
      jarakSekarang = jarak - jarakAwal
      while jarakSekarang > 0:
        total += 1000
        jarakSekarang -= 1
    return total
  elif golongan == 2:
    if jarak >= 50:
      total += 15000
      jarakSekarang = jarak - jarakAwal
      while jarakSekarang > 0:
        total += 1500
        jarakSekarang -= 1
    return total
  elif golongan == 3:
    if jarak >= 50:
      total += 20000
      jarakSekarang = jarak - jarakAwal
      while jarakSekarang > 0:
        total += 2000
        jarakSekarang -= 1
    return total
  elif golongan == 4:
    if jarak >= 50:
      total += 25000
      jarakSekarang = jarak - jarakAwal
      while jarakSekarang > 0:
        total += 2500
        jarakSekarang -= 1
    return total
        
    
      

#call function
print(tarif_tol(100))
print(tarif_tol(150, 1))
#print(tarif_tol(golongan = 4, jarak = 200))