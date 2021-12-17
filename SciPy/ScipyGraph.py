'''
Bekerja dengan Grafik
Grafik adalah struktur data yang penting.

SciPy memberi kita modul scipy.sparse.csgraph
untuk bekerja dengan struktur data seperti itu.

Matriks Kedekatan
Matriks ketetanggaan adalah nxn matriks n yang 
menyatakan banyaknya elemen dalam suatu graf.

Dan nilai-nilai mewakili hubungan antar elemen.
'''
'''
Contoh
       A
    1 / \ 2
     /   \
    B     C

Untuk graf seperti ini, dengan elemen A, B dan C, koneksinya adalah:

A & B dihubungkan dengan bobot 1.

A & C dihubungkan dengan beban 2.

C & B tidak terhubung.

Matriks Adjency akan terlihat seperti ini:
   ABC
   J:[0 1 2]  
   B:[1 0 0]
   C:[2 0 0]

Berikut ini beberapa metode yang paling sering digunakan untuk bekerja dengan matriks ketetanggaan.
'''

'''
Connected Components
Temukan semua komponen yang terhubung dengan connected_components() metode.
'''
import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

arr = np.array([
    [0, 1, 2],
    [1, 0, 0],
    [2, 0, 0]
])

newarr = csr_matrix(arr)

print(connected_components(newarr))


'''
Dijkstra
Gunakan dijkstra metode untuk menemukan jalur terpendek dalam grafik dari 
satu elemen ke elemen lainnya.

Dibutuhkan argumen berikut:

return_predecessors: boolean (Benar untuk mengembalikan seluruh jalur traversal jika tidak Salah).
indeks: indeks elemen untuk mengembalikan semua jalur dari elemen itu saja.
limit: berat maksimum jalur.
'''

'Temukan jalur terpendek dari elemen 1 ke 2:'
from scipy.sparse.csgraph import dijkstra

print(dijkstra(newarr, return_predecessors=True, indices=0))

'''
Floyd Warshall
Gunakan floyd_warshall() metode untuk menemukan jalur terpendek 
antara semua pasangan elemen.
'''
'Temukan jalur terpendek antara semua pasangan elemen'
import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(floyd_warshall(newarr, return_predecessors=True))


'''
Bellman Ford
The bellman_ford() Metode juga dapat menemukan jalan terpendek 
antara semua pasangan elemen, tetapi metode ini dapat menangani beban negatif juga.
'''
import numpy as np
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse import csr_matrix

arr = np.array([
  [0, -1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(bellman_ford(newarr, return_predecessors=True, indices=0))


'''
Orde Pertama Kedalaman
The depth_first_order()method mengembalikan kedalaman pertama traversal dari node.

Fungsi ini membutuhkan argumen berikut:

grafik.
elemen awal untuk melintasi grafik dari.
'''

'Lintasi kedalaman grafik terlebih dahulu untuk matriks ketetanggaan yang diberikan:'
import numpy as np
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

newarr = csr_matrix(arr)

print(depth_first_order(newarr, 1))

'''
Orde Pertama Luas
The breadth_first_order()Metode mengembalikan luasnya pertama traversal dari node.

Fungsi ini membutuhkan argumen berikut:

grafik.
elemen awal untuk melintasi grafik dari.
'''
'Lintasi lebar grafik terlebih dahulu untuk matriks ketetanggaan yang diberikan:'

import numpy as np
from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

newarr = csr_matrix(arr)

print(breadth_first_order(newarr, 1))