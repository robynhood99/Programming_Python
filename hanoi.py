def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Pindahkan cakram 1 dari tiang {source} ke tiang {target}")
        return
    hanoi(n-1, source, auxiliary, target)
    print(f"Pindahkan cakram {n} dari tiang {source} ke tiang {target}")
    hanoi(n-1, auxiliary, target, source)

# Input dari pengguna
num_disks = int(input("Masukkan jumlah cakram: "))

# Memanggil fungsi hanoi untuk memulai proses pemindahan
print("\nLangkah-langkah untuk memindahkan cakram:")
hanoi(num_disks, 'A', 'C', 'B')
