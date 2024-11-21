# time python3 calculateAverage.py
import mmap
import os
from gc import disable as gc_disable, enable as gc_enable
import multiprocessing as mp


def get_file_chunks(
    file_name: str,
    max_cpu: int = 8,
) -> tuple[int, list[tuple[str, int, int]]]:
    """Split file into chunks"""
    cpu_count = min(max_cpu, mp.cpu_count())

    file_size = os.path.getsize(file_name)
    chunk_size = file_size // cpu_count

    start_end = list()
    with open(file_name, mode="rb") as f:

        def is_new_line(position):
            if position == 0:
                return True
            else:
                f.seek(position - 1)
                return f.read(1) == b"\n"

        def next_line(position):
            f.seek(position)
            f.readline()
            return f.tell()

        chunk_start = 0
        while chunk_start < file_size:
            chunk_end = min(file_size, chunk_start + chunk_size)

            while not is_new_line(chunk_end):
                chunk_end -= 1

            if chunk_start == chunk_end:
                chunk_end = next_line(chunk_end)

            start_end.append(
                (
                    file_name,
                    chunk_start,
                    chunk_end,
                )
            )

            chunk_start = chunk_end

    return (
        cpu_count,
        start_end,
    )


def process_file_chunk(
    file_name: str,
    chunk_start: int,
    chunk_end: int,
) -> dict:
    """Process each file chunk in a different process"""
    result = dict()
    with open(file_name, mode="rb") as f:
        with mmap.mmap(f.fileno(), length=0, access=mmap.ACCESS_READ) as mm:
            mm.seek(chunk_start)
            gc_disable()
            while mm.tell() < chunk_end:
                line = mm.readline()
                if not line:
                    break
                chunk_start += len(line)
                if chunk_start > chunk_end:
                    break
                location, s = line.split(b";")
                measurement = int(s[:-3] + s[-2:])
                _result = result.get(location)
                if _result:
                    if measurement < _result[0]: # update min value
                        _result[0] = measurement
                    if measurement > _result[1]: # update max value
                        _result[1] = measurement
                    _result[2] += measurement # update sum
                    _result[3] += 1           # update count
                else:
                    result[location] = [
                        measurement,
                        measurement,
                        measurement,
                        1,
                    ]  # min, max, sum, count

            gc_enable()
    return result


def process_file(
    cpu_count: int,
    start_end: list,
):
    """Process data file"""
    with mp.Pool(cpu_count) as p:
        # Run chunks in parallel
        chunk_results = p.starmap(
            process_file_chunk,
            start_end,
        )

    # Combine all results from all chunks
    result = dict()
    for chunk_result in chunk_results:
        for location, measurements in chunk_result.items():
            _result = result.get(location)
            if _result:
                if measurements[0] < _result[0]:
                    _result[0] = measurements[0]
                if measurements[1] > _result[1]:
                    _result[1] = measurements[1]
                _result[2] += measurements[2]
                _result[3] += measurements[3]
            else:
                result[location] = measurements
    
    # Print final results
    print("{", end="")
    for location, measurements in sorted(result.items()):
        print(
            f"{location.decode('utf-8')}={0.1*measurements[0]:.1f}/{(0.1*measurements[2] / 0.1*measurements[3]) if 0.1*measurements[3] != 0 else 0:.1f}/{0.1*measurements[1]:.1f}",
            end=", ",
        )
    print("\b\b}", end = "")


if __name__ == "__main__":
    cpu_count, *start_end = get_file_chunks("measurements.txt")
    process_file(cpu_count, start_end[0])
