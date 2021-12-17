
'SciPy Optimizers'
''''
Pengoptimal di SciPy
Pengoptimal adalah seperangkat prosedur yang ditentukan dalam SciPy 
yang menemukan nilai minimum suatu fungsi, atau akar persamaan.
'''
'''
Mengoptimalkan Fungsi
Pada dasarnya, semua algoritma dalam Machine Learning tidak lebih 
dari persamaan kompleks yang perlu diminimalkan dengan bantuan data 
yang diberikan.
'''

'''
Akar Persamaan
NumPy mampu menemukan akar untuk polinomial dan persamaan linier, 
tetapi tidak dapat menemukan akar untuk persamaan non linier, seperti ini:

x + cos(x)

Untuk itu Anda dapat menggunakan optimze.rootfungsi SciPy .

Fungsi ini membutuhkan dua argumen yang diperlukan:

fun -  fungsi yang mewakili persamaan.

x0 - tebakan awal untuk root.

Fungsi mengembalikan objek dengan informasi mengenai solusi.

Solusi aktual diberikan di bawah atribut x objek yang dikembalikan:
'''
'Cari akar persamaan x + cos(x):'
from scipy.optimize import root
from math import cos

def eqn(x):
    return x + cos(x)

myRoot = root(eqn, 0)
print(myRoot.x)

'Catatan: Objek yang dikembalikan memiliki lebih banyak informasi tentang solusinya.'

'Cetak semua informasi tentang solusi (bukan hanya xyang merupakan root)'

print(myRoot)

'''

Meminimalkan Fungsi
Fungsi, dalam konteks ini, mewakili kurva, kurva memiliki titik tinggi dan titik rendah .

Titik tinggi disebut maxima .

Titik rendah disebut minima .

Titik tertinggi di seluruh kurva disebut maxima global , 
sedangkan sisanya disebut maxima lokal .

Titik terendah di seluruh kurva disebut minimum global , 
sedangkan sisanya disebut minimum lokal .
'''

'''
Menemukan Minima
Kita dapat menggunakan scipy.optimize.minimize()
fungsi untuk meminimalkan fungsi.

The minimize()Fungsi mengambil argumen berikut:

Fun - fungsi yang mewakili persamaan.
x0 - tebakan awal untuk root.

metode - nama metode yang akan digunakan. Nilai hukum:
    'CG'
    'BFGS'
    'Newton-CG'
    'L-BFGS-B'
    'TNC'
    'COBYLA'
    'SLSQP'

callback - fungsi dipanggil setelah setiap iterasi optimasi.

options - Dictonary yang mendefinisikan params tambahan:
  {
     "disp": boolean - print detailed description
     "gtol": number - the tolerance of the error
  }
'''

'Minimalkan fungsi x^2 + x + 2dengan BFGS:'
from scipy.optimize import minimize

def eqn(x):
    return x**2 + x + 2

mymin = minimize(eqn, 0, method='BFGS')
print(mymin)