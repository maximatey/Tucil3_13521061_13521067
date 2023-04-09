import heapq



def astar(strdist, graph, start, goal):
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
    heapq.heappush(queue, (0, 0, start, [start]))
    
    while queue:
        
        # Pop titik dengan nilai f(n) terkecil dari queue
        totalcost, cost, current, path = heapq.heappop(queue)
        
        print(current)
        print(cost)
        print(totalcost)
        
        
        
        # Jika titik saat ini adalah titik tujuan, maka selesai
        if current == goal:
            return totalcost, cost, path
        
        # Jika titik saat ini belum pernah dikunjungi, tambahkan ke visited
        if current not in visited:
            visited.add(current)
            
            # Cari semua tetangga dari titik saat ini
            for neighbor in get_neighbors(graph, current, visited):
                tmppath = path
                # Hitung nilai f(n) dari tetangga tersebut
                neighbor_cost = cost + graph[current][neighbor]
                tmppath = tmppath + [neighbor]
                heuriscost = neighbor_cost + strdist[goal][neighbor]
                 
                # Masukkan tetangga ke queue
                heapq.heappush(queue, (heuriscost, neighbor_cost, neighbor, tmppath))
        
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
        if (i!=current and graph[current][i] != 0 and (i not in visited)):
            neighbors.append(i)
        
    return neighbors

# Contoh penggunaan
# A, Z, O, S, F, B, P, C, R, D, M, L, T
graph = [
    [0, 75, 0, 140, 0, 0, 0, 0, 0,0,0,0, 118],
    [75, 0, 71, 0, 0, 0 ,0,0,0,0,0,0,0],
    [0, 71, 0, 151, 0, 0, 0, 0,0,0,0,0,0],
    [140, 0, 151, 0, 99, 0 ,0,0,80,0,0,0,0],
    [0, 0, 0, 99, 0, 211 ,0,0,0,0,0,0,0],
    [0, 0, 0, 0, 211, 0 ,101, 0, 0, 0,0 ,0,0],
    [0, 0, 0, 0, 0, 101 ,0, 138, 97, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0 , 138, 0, 146, 0, 0, 0, 0],
    [0, 0, 0, 80, 0, 0 ,97,146, 0, 120,0,0,0],
    [0, 0, 0, 0, 0, 0, 0, 0, 120, 0, 75, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 75, 0, 70, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 70, 0, 111],
    [118, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 111, 0],
]

strdist=[
    [100,200,300,400,100,200,300,400,100,200,300,400,100],
    [200,300,400,100,200,300,400,100,200,300,400,100,200],
    [300,400,100,200,300,400,100,200,300,400,100,200,300],
    [400,100,200,300,400,100,200,300,400,100,200,300,400],
    [100,200,300,400,100,200,300,400,100,200,300,400,100],
    [200,300,400,100,200,300,400,100,200,300,400,100,200],
    [300,400,100,200,300,400,100,200,300,400,100,200,300],
    [400,100,200,300,400,100,200,300,400,100,200,300,400],
    [100,200,300,400,100,200,300,400,100,200,300,400,100],
    [200,300,400,100,200,300,400,100,200,300,400,100,200],
    [300,400,100,200,300,400,100,200,300,400,100,200,300],
    [400,100,200,300,400,100,200,300,400,100,200,300,400],
    [100,200,300,400,100,200,300,400,100,200,300,400,100]
]
start = 0
goal = 5

totalcost, path_cost, path = astar(strdist, graph, start, goal)
if path_cost != -1:
    print("Path cost:", path_cost)
else:
    print("Path not found")

for i in path:
    print(i)