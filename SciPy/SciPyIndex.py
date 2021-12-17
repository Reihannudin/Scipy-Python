'Tutorial SciPy'
''''
Apa itu SciPy?
SciPy adalah perpustakaan komputasi ilmiah yang menggunakan NumPy di bawahnya.

SciPy adalah singkatan dari Python Ilmiah.

Ini menyediakan lebih banyak fungsi utilitas untuk pengoptimalan, statistik, dan pemrosesan sinyal.

Seperti NumPy, SciPy adalah open source sehingga kita dapat menggunakannya secara bebas.

SciPy dibuat oleh pencipta NumPy, Travis Olliphant.
'''

'''
Mengapa Menggunakan SciPy?
Jika SciPy menggunakan NumPy dibawahnya, mengapa kita tidak menggunakan NumPy saja?

SciPy telah mengoptimalkan dan menambahkan fungsi yang sering digunakan di NumPy dan Ilmu Data.
'''

'''
Instalasi SciPy
Jika Anda sudah menginstal Python dan PIP pada suatu sistem, maka instalasi SciPy sangat mudah.

Instal menggunakan perintah ini:
'pip install scipy'
'''

'''
Impor SciPy

Setelah SciPy diinstal, impor modul SciPy yang ingin Anda gunakan di aplikasi Anda dengan 
menambahkan pernyataan: from scipy import module
'''
from scipy import constants

'Sekarang kita telah mengimpor modul konstanta dari SciPy, dan aplikasi siap untuk menggunakannya:'

'Berapa meter kubik dalam satu liter:'
print(constants.liter)

'''
konstanta: SciPy menawarkan satu set konstanta matematika, salah satunya adalah liter yang 
mengembalikan 1 liter sebagai meter kubik.

Anda akan belajar lebih banyak tentang konstanta di bab berikutnya.
'''

'''
Memeriksa Versi SciPy
String versi disimpan di bawah __version__ atribut.
'''
import scipy as sc
print(sc.__version__)