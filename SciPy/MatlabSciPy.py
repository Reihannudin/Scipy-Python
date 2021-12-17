'''
Bekerja Dengan Array Matlab
Kami tahu bahwa NumPy memberi kami metode untuk mempertahankan data dalam 
format yang dapat dibaca untuk Python. Tetapi SciPy juga memberi kami 
interoperabilitas dengan Matlab.

SciPy memberi kita modul scipy.io, yang memiliki fungsi untuk bekerja dengan array Matlab.
'''
'''
Mengekspor Data dalam Format Matlab
The savemat() Fungsi memungkinkan kita untuk ekspor data dalam format Matlab.

Metode ini mengambil parameter berikut:
   filename - nama file untuk menyimpan data.
   mdict - kamus yang berisi data.
   do_compression - nilai boolean yang menentukan apakah akan mengompresi hasil atau tidak. Standar Salah.
'''
from scipy import io
import numpy as np

arr = np.arange(10)

io.savemat('arr.mat', {"vec": arr})

'''
Catatan: Contoh di atas menyimpan nama file "arr.mat" di komputer Anda.

Untuk membuka file, lihat contoh "Impor Data dari Format Matlab" di bawah ini:
'''
'''
Impor Data dari Format Matlab
The loadmat() Fungsi memungkinkan kita untuk mengimpor data dari file Matlab.

Fungsi mengambil satu parameter yang diperlukan:

filename - nama file dari data yang disimpan.

Ini akan mengembalikan array terstruktur yang kuncinya adalah nama variabel, 
dan nilai yang sesuai adalah nilai variabel.
'''
'Impor array dari file mat berikut.:'
from scipy import io
import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,])

# Export:
io.savemat('arr.mat', {"vec": arr})

# Import:
mydata = io.loadmat('arr.mat')

print(mydata)

'Gunakan nama variabel "vec" untuk hanya menampilkan larik dari data matlab:'

print(mydata['vec'])

'''
Catatan: Kita dapat melihat bahwa array awalnya adalah 1D, 
tetapi pada ekstraksi telah meningkat satu dimensi.

Untuk mengatasi ini, kami dapat memberikan argumen tambahan squeeze_me=True:
'''
# Import:
mydata = io.loadmat('arr.mat', squeeze_me=True)

print(mydata['vec'])
