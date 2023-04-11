import heapq

def astar(strdist, graph, start, goal):
    
    # Inisialisasi queue dan visited
    queue = []
    visited = set()
    
    # Masukkan titik awal ke queue
    heapq.heappush(queue, (0, 0, start, [start]))
    
    while queue:
        
        # Pop titik dengan nilai f(n) terkecil dari queue
        totalcost, cost, current, path = heapq.heappop(queue)
        
        
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
                neighbor_cost = cost + graph[current][neighbor] * strdist[current][neighbor]
                tmppath = tmppath + [neighbor]
                heuriscost = neighbor_cost + strdist[goal][neighbor]
                 
                # Masukkan tetangga ke queue
                heapq.heappush(queue, (heuriscost, neighbor_cost, neighbor, tmppath))
        
    
    # Jika tidak ditemukan path dari titik awal ke titik tujuan
    return -1,[]

def get_neighbors(graph, current,visited):
    
    neighbors = []
    
    # Cek tetangga-tetangga di atas, bawah, kiri, dan kanan
    for i in range(len(graph[0])):
        if (i!=current and graph[current][i] != 0 and (i not in visited)):
            neighbors.append(i)
        
    return neighbors
