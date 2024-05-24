"""
This script is used to generate the dataset for the SP project.
The dataset contains a list of n entrys with the following format:
timestamp:latitude;longitude

timestamp is the time in epoch format and coordinates are latitude and longitude 

for simplicity purposes:
    the latitude values range from 42.000 and 36.686 
    and the longitude values from -9.788 and -6.251 
these values are approximatelly the range of Portugal and are randomly generated

nº packets ver no wireshark / tamanho do dataset
nº de bytes / tamanho do dataset

10% de interseçao
"""

import random
import sys


# Portugal coordinates
min_longitude = -9.788
max_longitude = -6.251
min_latitude = 36.686
max_latitude = 42.000

starting_time = 1715036400  # 07/05/2024 00:00:00


def gen_dataset(filename1, filename2, n):
    common_entries = int(n * 0.1)  # 10% of n
    unique_entries = n - common_entries

    # Generate common data for both files
    common_data = [
        f"{starting_time + i}:{random.uniform(min_latitude, max_latitude):.4f};{random.uniform(min_longitude, max_longitude):.4f}\n"
        for i in range(common_entries)
    ]

    # Write to the first file with unique data
    with open(filename1, "w") as f1:
        with open(filename2, "w") as f2:

            f1.writelines(common_data)
            f2.writelines(common_data)

            for i in range(common_entries, n):
                timestamp = starting_time + i + unique_entries
                latitude = random.uniform(min_latitude, max_latitude)
                longitude = random.uniform(min_longitude, max_longitude)
                f1.write(f"{timestamp}:{latitude:.4f};{longitude:.4f}\n")
                f2.write(
                    f"{timestamp}:{latitude+1:.4f};{longitude+1:.4f}\n"
                )  # 1 to make sure they are different


def number_of_intersections(filename1, filename2):
    with open(filename1, "r") as f1:
        with open(filename2, "r") as f2:
            data1 = set(f1.readlines())
            data2 = set(f2.readlines())
            return len(data1.intersection(data2))


def main():
    gen_dataset("dataset1.txt", "dataset2.txt", 10000)

    print(number_of_intersections("dataset1.txt", "dataset2.txt"))


if __name__ == "__main__":
    main()
