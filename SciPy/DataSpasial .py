'''
Bekerja dengan Data Spasial
Data spasial mengacu pada data yang direpresentasikan dalam ruang geometris.

Misalnya titik pada sistem koordinat.

Kami menangani masalah data spasial pada banyak tugas.

Misalnya menemukan apakah suatu titik berada di dalam batas atau tidak.

SciPy memberi kita modul scipy.spatial, yang memiliki fungsi untuk bekerja dengan data spasial.
'''

'''
Triangulasi
Triangulasi poligon adalah membagi poligon menjadi beberapa segitiga yang dengannya kita dapat 
menghitung luas poligon.

Triangulasi dengan titik berarti membuat segitiga yang tersusun atas permukaan di mana semua 
titik yang diberikan berada pada setidaknya satu titik sudut dari sembarang segitiga di permukaan.

Salah satu metode untuk menghasilkan triangulasi ini melalui titik adalah Delaunay() Triangulasi.
'''

'Buatlah triangulasi dari poin-poin berikut:'
import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1]
])

simplices = Delaunay(points).simplices

plt.triplot(points[:, 0], points[:, 1], simplices)
plt.scatter(points[:, 0], points[:, 1], color='r')

plt.show()

'Catatan: The simplices properti menciptakan generalisasi dari notasi segitiga'

'Convex Hull'
'''
Convex hull adalah poligon terkecil yang mencakup semua titik yang diberikan.

Gunakan ConvexHull() metode untuk membuat Convex Hull.
'''
import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1],
  [1, 2],
  [5, 0],
  [3, 1],
  [1, 2],
  [0, 2]
])

hull = ConvexHull(points)
hull_points = hull.simplices

plt.scatter(points[:,0], points[:,1])
for simplex in hull_points:
  plt.plot(points[simplex,0], points[simplex,1], 'k-')

plt.show()

'''
KDtrees
KDtrees adalah struktur data yang dioptimalkan untuk kueri tetangga 
terdekat.

Misalnya dalam sekumpulan titik dengan menggunakan KDTrees, 
kita dapat menanyakan titik mana yang terdekat dengan titik tertentu secara efisien.

The KDTree() Metode mengembalikan sebuah objek KDTree.

The query() Metode mengembalikan jarak ke tetangga terdekat dan lokasi tetangga.
'''

from scipy.spatial import KDTree

points = [(1, -1), (2, 3), (-2, 3), (2, -3)]

kdtree = KDTree(points)

res = kdtree.query((1, 1))

print(res)


'''
Matriks Jarak
Ada banyak Metrik Jarak yang digunakan untuk menemukan berbagai jenis jarak 
antara dua titik dalam ilmu data, jarak Euclidean, jarak kosinus, dll.

Jarak antara dua vektor mungkin tidak hanya panjang garis lurus di antara 
mereka, tetapi juga sudut antara mereka dari asal, atau jumlah langkah unit yang diperlukan, dll.

Banyak kinerja algoritme Pembelajaran Mesin sangat bergantung pada metrik jarak. 
Misalnya "K Tetangga Terdekat", atau "K Berarti" dll.

Mari kita lihat beberapa Metrik Jarak:
'''

''''
Jarak Euclidean
Temukan jarak euclidean antara titik-titik yang diberikan.
'''
from scipy.spatial.distance import euclidean

p1 = (1, 0)
p2 = (10, 2)

res = euclidean(p1, p2)

print(res)

'''
Jarak Cityblock (Jarak Manhattan)
Apakah jarak dihitung menggunakan 4 derajat gerakan.

Misal kita hanya bisa bergerak: atas, bawah, kanan, atau kiri, 
tidak diagonal.
'''
from scipy.spatial.distance import cityblock

p1 = (1, 0)
p2 = (10, 2)

res = cityblock(p1, p2)

print(res)

'''
Jarak kosinus
Adalah nilai sudut cosinus antara dua titik A dan B.
'''
'Cari jarak cosinus antara titik-titik yang diberikan:'
from scipy.spatial.distance import cosine

p1 = (1, 0)
p2 = (10, 2)

res = cosine(p1, p2)

print(res)


'''
Jarak Hamming
Adalah proporsi bit di mana dua bit berbeda.

Ini adalah cara untuk mengukur jarak untuk urutan biner.
'''
'Temukan jarak hamming antara titik-titik yang diberikan:'
from scipy.spatial.distance import hamming

p1 = (True, False, True)
p2 = (False, True, True)

res = hamming(p1, p2)

print(res)