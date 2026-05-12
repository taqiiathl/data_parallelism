from multiprocessing import Pool
import os
import time

def process_data(data):
    pid = os.getpid()

    # simulasi proses berat
    time.sleep(1)

    result = data * data
    print(f"Process {pid} memproses data {data} -> hasil {result}")

    return result

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]

    with Pool(4) as p:
        results = p.map(process_data, numbers)

    print("Hasil akhir:", results)