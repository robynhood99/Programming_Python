import heapq

def dijkstra(graph, start):
    # Inisialisasi jarak dari start ke semua simpul lain dengan tak terhingga
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Priority queue untuk memilih simpul dengan jarak terpendek
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Lewati jika jarak yang ditemukan lebih panjang dari jarak yang sudah ada
        if current_distance > distances[current_node]:
            continue
        
        # Memeriksa tetangga dari simpul saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Jika jarak baru lebih pendek, perbarui jarak dan tambahkan ke antrian prioritas
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Contoh graf berbobot
graph = {
    'A': {'B': 7, 'C': 9, 'F': 14},
    'B': {'A': 7, 'C': 10, 'D': 15},
    'C': {'A': 9, 'B': 10, 'D': 11, 'F': 2},
    'D': {'B': 15, 'C': 11, 'E': 6},
    'E': {'D': 6, 'F': 9},
    'F': {'A': 14, 'C': 2, 'E': 9}
}

# Input simpul awal dari pengguna
start_node = input("Masukkan simpul awal (misalnya A): ")

# Memanggil fungsi Dijkstra untuk menemukan jalur terpendek
distances = dijkstra(graph, start_node)

# Output hasil
print(f"Jarak terpendek dari simpul {start_node} ke simpul lainnya:")
for node, distance in distances.items():
    print(f"Ke simpul {node}: {distance}")
