import heapq



def ucs(graph, start, goal):
    """
    Route planning berbasis UCS pada matriks berbobot
    :param graph: Matriks bertetanggaan berbobot, dalam bentuk nested list
    :param start: Titik awal, dalam bentuk indeks baris dan kolom pada matriks
    :param goal: Titik tujuan, dalam bentuk indeks baris dan kolom pada matriks
    :return: Path dari titik awal ke titik tujuan
    """
    
    # Inisialisasi queue dan visited
    queue = []
    visited = set()
    
    # Masukkan titik awal ke queue
    heapq.heappush(queue, (0, start, [start]))
    
    while queue:
        
        # Pop titik dengan nilai f(n) terkecil dari queue
        cost, current, path = heapq.heappop(queue)
        
        print(current)
        print(cost)
        
        
        
        # Jika titik saat ini adalah titik tujuan, maka selesai
        if current == goal:
            return cost, path
        
        # Jika titik saat ini belum pernah dikunjungi, tambahkan ke visited
        if current not in visited:
            visited.add(current)
            
            # Cari semua tetangga dari titik saat ini
            for neighbor in get_neighbors(graph, current, visited):
                tmppath = path
                # Hitung nilai f(n) dari tetangga tersebut
                neighbor_cost = cost + graph[current][neighbor]
                tmppath = tmppath + [neighbor]
                 
                # Masukkan tetangga ke queue
                heapq.heappush(queue, (neighbor_cost, neighbor, tmppath))
        
        for i in queue:
            print(i)
        print("========================")
    
    # Jika tidak ditemukan path dari titik awal ke titik tujuan
    return -1,[]

def get_neighbors(graph, current,visited):
    """
    Mendapatkan semua tetangga dari suatu titik pada matriks
    :param graph: Matriks bertetanggaan berbobot, dalam bentuk nested list
    :param current: Titik saat ini, dalam bentuk indeks baris dan kolom pada matriks
    :return: List berisi tetangga-tetangga dari titik saat ini
    """
    
    neighbors = []
    
    # Cek tetangga-tetangga di atas, bawah, kiri, dan kanan
    for i in range(len(graph[0])):
        if (i!=current and graph[current][i] != 999999 and (i not in visited)):
            neighbors.append(i)
        
    return neighbors

# Contoh penggunaan
# A, Z, O, S, F, B, P, C, R, D, M, L, T
graph = [
    [0, 75, 999999, 140, 999999, 999999, 999999, 999999, 999999,999999,999999,999999, 118],
    [75, 0, 71, 999999, 999999, 999999 ,999999,999999,999999,999999,999999,999999,999999],
    [999999, 71, 0, 151, 999999, 999999, 999999, 999999,999999,999999,999999,999999,999999],
    [140, 999999, 151, 0, 99, 999999 ,999999,999999,80,999999,999999,999999,999999],
    [999999, 999999, 999999, 99, 0, 211 ,999999,999999,999999,999999,999999,999999,999999],
    [999999, 999999, 999999, 999999, 211, 0 ,101, 999999, 999999, 999999,999999 ,999999,999999],
    [999999, 999999, 999999, 999999, 999999, 101 ,0, 138, 97, 999999, 999999, 999999, 999999],
    [999999, 999999, 999999, 999999, 999999, 999999 , 138, 0, 146, 999999, 999999, 999999, 999999],
    [999999, 999999, 999999, 80, 999999, 999999 ,97,146, 0, 120,999999,999999,999999],
    [999999, 999999, 999999, 999999, 999999, 999999, 999999, 999999, 120, 0, 75, 999999, 999999],
    [999999, 999999, 999999, 999999, 999999, 999999, 999999, 999999, 999999, 75, 0, 70, 999999],
    [999999, 999999, 999999, 999999, 999999, 999999, 999999, 999999, 999999, 999999, 70, 0, 111],
    [118, 999999, 999999, 999999, 999999, 999999, 999999, 999999, 999999, 999999, 999999, 111, 0],
]
start = 0
goal = 5

path_cost, path = ucs(graph, start, goal)
if path_cost != -1:
    print("Path cost:", path_cost)
else:
    print("Path not found")

for i in path:
    print(i)