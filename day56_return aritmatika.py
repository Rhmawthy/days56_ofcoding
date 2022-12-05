a = int (input("masukkan angka 1 :"))
b = int (input("masukkan angka 2 :"))

def aritmatika (angka_1, angka_2):
	tambah = angka_1 + angka_2
	kurang = angka_1 - angka_2
	bagi = angka_1 / angka_2
	kali= angka_1 * angka_2
	
	return tambah,kurang,bagi,kali

t,k,b,l = aritmatika (a,b)
print("hasil tambah", t)
print("hasil kurang", k)
print("hasil bagi ", b)
print("hasil kali ", l)





