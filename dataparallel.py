from multiprocessing import Pool
import os

# fungsi yang akan dijalankan paralel
def process_data(data):
    pid = os.getpid()
    result = data * data
    print(f"Process {pid} memproses data {data} -> hasil {result}")
    return result

if __name__ == "__main__":
    # data berbeda untuk tiap proses
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]

    # membuat 4 proses paralel
    with Pool(4) as p:
        results = p.map(process_data, numbers)

    print("Hasil akhir:", results)