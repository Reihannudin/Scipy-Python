'''
Apa itu Data Jarang?
Data jarang adalah data yang sebagian besar memiliki elemen yang tidak 
digunakan (elemen yang tidak membawa informasi apa pun).

Ini bisa berupa array seperti ini:
[1, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0]
'''

'''
Data Jarang: adalah kumpulan data di mana sebagian besar nilai item adalah nol.

Dense Array: kebalikan dari sparse array: sebagian besar nilainya bukan nol.
'''

'''
Dalam komputasi ilmiah, ketika kita berurusan dengan turunan parsial dalam 
aljabar linier, kita akan menemukan data yang jarang.
'''

'''
Cara Bekerja Dengan Data Jarang

SciPy memiliki modul, scipy.sparse yang menyediakan fungsi untuk menangani 
data yang jarang.

Ada dua jenis matriks jarang yang kami gunakan:

CSC - Kolom Jarang Terkompresi. Untuk aritmatika yang efisien, pengirisan kolom yang cepat.

CSR - Baris Jarang Terkompresi. Untuk pengirisan baris cepat, produk vektor matriks lebih cepat

Kami akan menggunakan matriks CSR dalam tutorial ini.
'''

'''
Matriks CSR
Kita dapat membuat matriks CSR dengan melewatkan sebuah array ke dalam function
scipy.sparse.csr_matrix()
'''

'Buat matriks CSR dari array:'
import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])
print(csr_matrix(arr))

'''
Contoh di atas mengembalikan:
  (0, 5) 1 
  (0, 6) 1 
  (0, 8) 2

Dari hasil kita dapat melihat bahwa ada 3 item dengan nilai.

Item 1. berada di 0posisi baris 5dan memiliki nilai 1.

Item 2. berada di 0posisi baris 6dan memiliki nilai 1.

Item 3. berada di 0posisi baris 8dan memiliki nilai 2.
'''

'''
Metode Matriks Jarang

Melihat data yang disimpan (bukan item nol) dengan dataproperti:
'''
met = np.array([[0,0,0], [0,0,1], [1,0,2]])
print(csr_matrix(met).data)

'Menghitung bukan nol dengan count_nonzero() metode:'
print(csr_matrix(met).count_nonzero())

'Menghapus entri nol dari matriks dengan eliminate_zeros()metode:'
mat = csr_matrix(met)
mat.eliminate_zeros()

print(mat)
print('-------------')

'Menghilangkan entri duplikat dengan sum_duplicates()metode:'
'Menghilangkan duplikat dengan menambahkannya:'
mat = csr_matrix(met)
mat.sum_duplicates()
print(mat)

'Konversi dari csr ke csc dengan tocsc() metode:'
newarr = csr_matrix(met).tocsc()
print(newarr)