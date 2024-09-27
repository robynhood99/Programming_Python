def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def print_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Input dari pengguna
start_range = int(input("Masukkan angka awal rentang: "))
end_range = int(input("Masukkan angka akhir rentang: "))

# Mencetak bilangan prima dalam rentang yang diberikan
prime_numbers = print_primes(start_range, end_range)
print(f"Bilangan prima antara {start_range} dan {end_range} adalah: {prime_numbers}")
