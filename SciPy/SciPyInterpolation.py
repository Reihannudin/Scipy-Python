'''
Apa itu Interpolasi?
Interpolasi adalah metode untuk menghasilkan titik-titik 
antara titik-titik yang diberikan.

Sebagai contoh: untuk titik 1 dan 2, kita dapat melakukan 
interpolasi dan menemukan titik 1,33 dan 1,66.

Interpolasi memiliki banyak kegunaan, dalam Machine Learning 
kita sering berurusan dengan data yang hilang dalam sebuah dataset, 
interpolasi sering digunakan untuk menggantikan nilai-nilai tersebut.

Metode pengisian nilai ini disebut imputasi .

Selain imputasi, interpolasi sering digunakan di mana kita perlu 
menghaluskan titik-titik diskrit dalam kumpulan data.
'''

'''
Bagaimana Menerapkannya di SciPy?

SciPy memberi kita sebuah modul bernama scipy.interpolate yang memiliki 
banyak fungsi untuk menangani interpolasi:
'''
'''
Interpolasi 1D
Fungsi interp1d() ini digunakan untuk menginterpolasi suatu distribusi dengan 1 variabel.

Dibutuhkan x dan y menunjuk dan mengembalikan fungsi yang dapat dipanggil yang dapat dipanggil 
dengan new x dan mengembalikan yang sesuai y.
'''

'Untuk nilai interpolasi xs dan ys yang diberikan dari 2.1, 2.2... hingga 2.9'

from scipy.interpolate import interp1d
import numpy as np

xs = np.arange(10)
ys = 2*xs + 1

interp_func = interp1d(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))

print(newarr)

'''
Catatan: xs baru harus berada dalam rentang yang sama dengan xs lama, 
artinya kita tidak dapat memanggil interp_func() dengan nilai yang lebih tinggi dari 10, 
atau kurang dari 0.
'''

'''
Interpolasi Spline
Dalam interpolasi 1D titik-titik dipasang untuk kurva tunggal sedangkan dalam interpolasi 
Spline titik-titik dipasang terhadap fungsi sepotong - sepotong yang didefinisikan dengan 
polinomial yang disebut splines.

The UnivariateSpline() Fungsi mengambil xs dan ys dan menghasilkan funciton callable yang 
bisa disebut dengan yang baru xs.
'''
'Fungsi sepotong-sepotong: Fungsi yang memiliki definisi berbeda untuk rentang yang berbeda.'

'Temukan interpolasi spline univariat untuk 2.1, 2.2... 2.9 untuk titik non linier berikut:'
from scipy.interpolate import UnivariateSpline
import numpy as np

xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1

interp_func = UnivariateSpline(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))

print(newarr)

'''
Interpolasi dengan Fungsi Basis Radial
Fungsi basis radial adalah fungsi yang didefinisikan sesuai dengan titik referensi tetap.

The Rbf()Fungsi juga mengambil xsdan ys sebagai argumen dan menghasilkan fungsi callable 
yang bisa disebut dengan yang baru xs.
'''

'Interpolasi xs dan ys berikut menggunakan rbf dan temukan nilai untuk 2.1, 2.2 ... 2.9:'
from scipy.interpolate import Rbf
import numpy as np

xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1

interp_func = Rbf(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))

print(newarr)