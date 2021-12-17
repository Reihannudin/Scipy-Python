'''
Apa itu Uji Signifikansi Statistik?
Dalam statistik, signifikansi statistik berarti bahwa hasil yang dihasilkan memiliki 
alasan di baliknya, tidak dihasilkan secara acak, atau kebetulan.

SciPy memberi kita modul bernama scipy.stats, yang memiliki fungsi untuk melakukan 
uji signifikansi statistik.

Berikut adalah beberapa teknik dan kata kunci yang penting saat melakukan tes tersebut:
'''
'''
Hipotesis dalam Statistik
Hipotesis adalah asumsi tentang suatu parameter dalam populasi.
'''
'''
Hipotesis nol
Diasumsikan bahwa observasi tidak signifikan secara statistik.
'''

'''
Hipotesis Alternatif
Diasumsikan bahwa pengamatan disebabkan oleh beberapa alasan.

Ini alternatif untuk Hipotesis Null.

Contoh:

Untuk penilaian siswa kami akan mengambil:

"siswa lebih buruk dari rata-rata" - sebagai hipotesis nol, dan:

"siswa lebih baik dari rata-rata" - sebagai hipotesis alternatif.
'''
'''
Tes satu sisi
Ketika hipotesis kami menguji satu sisi nilai saja, itu disebut "uji satu sisi".

Contoh:

Untuk hipotesis nol:

"rata-ratanya sama dengan k", kita dapat memiliki hipotesis alternatif:

"rata-ratanya kurang dari k", atau:

rata-rata lebih besar dari k
'''
'''
Tes dua sisi
Ketika hipotesis kami menguji kedua sisi nilai.

Contoh:

Untuk hipotesis nol:

"rata-ratanya sama dengan k", kita dapat memiliki hipotesis alternatif:

"rata-rata tidak sama dengan k"

Dalam hal ini mean kurang dari, atau lebih besar dari k, dan kedua sisi harus diperiksa.
'''
'''
nilai alfa
Nilai alpha adalah tingkat signifikansi.

Contoh:

Seberapa dekat dengan ekstrem data harus agar hipotesis nol ditolak.

Biasanya diambil sebagai 0,01, 0,05, atau 0,1.
'''
'''
nilai P
Nilai P menunjukkan seberapa dekat dengan ekstrim data sebenarnya.

Nilai P dan nilai alpha dibandingkan untuk menetapkan signifikansi statistik.

Jika nilai p <= alpha kami menolak hipotesis nol dan mengatakan bahwa data signifikan secara statistik. 
jika tidak, kami menerima hipotesis nol.
'''
'''
T-Test
Uji-t digunakan untuk menentukan apakah ada perbedaan yang signifikan antara rata-rata dua variabel. 
dan memberi tahu kami jika mereka termasuk dalam distribusi yang sama.

Ini adalah tes dua sisi.

Fungsi tersebut ttest_ind()mengambil dua sampel dengan ukuran yang sama dan menghasilkan tupel t-statistik 
dan nilai-p.
'''
'Temukan apakah nilai yang diberikan v1 dan v2 berasal dari distribusi yang sama:'
import numpy as np
from scipy.stats import ttest_ind

v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)

res = ttest_ind(v1, v2)

print(res)

'Jika Anda hanya ingin mengembalikan nilai-p, gunakan pvalueproperti:'
res = ttest_ind(v1, v2).pvalue

print(res)

'''
KS-Tes
Uji KS digunakan untuk memeriksa apakah nilai yang diberikan mengikuti distribusi.

Fungsi mengambil nilai yang akan diuji, dan CDF sebagai dua parameter.

Sebuah CDF dapat berupa string atau fungsi callable bahwa pengembalian probabilitas.

Ini dapat digunakan sebagai tes satu sisi atau dua sisi.

Secara default adalah dua ekor. Kita dapat melewatkan alternatif parameter sebagai 
string dari salah satu sisi dua, kurang, atau lebih besar.
'''
'Temukan apakah nilai yang diberikan mengikuti distribusi normal:'
import numpy as np
from scipy.stats import kstest

v = np.random.normal(size=100)

res = kstest(v, 'norm')

print(res)

'''
Deskripsi Statistik Data
Untuk melihat ringkasan nilai dalam array, kita dapat menggunakan describe()fungsi.

Ini mengembalikan deskripsi berikut:

jumlah pengamatan (nobs)
nilai minimum dan maksimum = minmax
berarti
perbedaan
kecondongan
kurtosis
'''
import numpy as np
from scipy.stats import describe

v = np.random.normal(size=100)
res = describe(v)

print(res)

'''
Uji Normalitas (Skewness dan Kurtosis)
Tes normalitas didasarkan pada skewness dan kurtosis.

The normaltest()kembali fungsi p nilai hipotesis nol:

"x berasal dari distribusi normal" .
'''

'''
Kecondongan:
Ukuran simetri dalam data.

Untuk distribusi normal adalah 0.

Jika negatif berarti data miring ke kiri.

Jika positif berarti datanya miring ke kanan.
'''

'''
Kurtosis:
Sebuah ukuran apakah data yang berat atau ringan ekor ke distribusi normal.

Kurtosis positif berarti ekor berat.

Kurtosis negatif berarti ekor ringan.
'''
'Temukan kemiringan dan kurtosis nilai dalam array:'
import numpy as np
from scipy.stats import skew, kurtosis

v = np.random.normal(size=100)

print(skew(v))
print(kurtosis(v))

'Cari tahu apakah data berasal dari distribusi normal:'

import numpy as np
from scipy.stats import normaltest

v = np.random.normal(size=100)

print(normaltest(v))