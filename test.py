import time
from datetime import timedelta


def line_iterate(s: bytes,
) -> tuple[bytes, int]:
    location = []
    i = 0
    while i < len(s):
        if s[i] == ord(';'): break
        location.append(s[i])
        i += 1
    location = bytes(location)
    
    sign = -1 if s[-6] == ord('-') or s[-5] == ord('-') else 1
    idx = -5 if s[-5] >= ord('0') and s[-5] <= ord('9') else -4

    if idx == -4:
        measurement = sign * (s[idx]-ord('0'))*10 + (s[-2]-ord('0'))
    else:
        measurement = sign * (s[idx]-ord('0'))*100 + (s[idx+1]-ord('0'))*10 + (s[-2]-ord('0'))

    return (location, measurement)


def calculate_stats(filepath: str):
    stats = {}

    with open(filepath, "rb") as f:
        cnt = 0
        for row in f:
            cnt += 1
            if cnt == 10: break

            location, measurement = line_iterate(row)
            print(location, measurement, sep = " ")




if __name__ == "__main__":
    measurements_path = "measurements.txt"
    calculate_stats(measurements_path)