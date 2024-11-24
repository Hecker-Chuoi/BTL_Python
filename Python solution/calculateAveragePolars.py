import polars as pl
import timeit  
import psutil 
import os  

def df():
    process = psutil.Process(os.getpid())  # Tạo đối tượng psutil để giám sát process hiện tại

    # Giám sát bộ nhớ trước khi bắt đầu
    memory_before = process.memory_info().rss / (1024 * 1024)  
    print(f"Memory usage before: {memory_before:.2f} MB")  

    start_time = timeit.default_timer()  

    # Đọc tệp CSV sử dụng Polars
    df = pl.scan_csv(  # Dùng scan_csv để thực hiện lazy-loading (xử lý không tải toàn bộ dữ liệu vào bộ nhớ)
        "measurements.txt",  
        separator=";", 
        has_header=False,  
        with_column_names=lambda cols: ["station_name", "measurement"],  # Gán tên cột
    )

    # Thực hiện nhóm dữ liệu và tính toán các thống kê
    grouped = (
        df.group_by("station_name")  # Nhóm dữ liệu theo cột "station_name"
        .agg(
            pl.min("measurement").alias("min_measurement"),  
            pl.mean("measurement").alias("mean_measurement"), 
            pl.max("measurement").alias("max_measurement"),  
        )
        .sort("station_name")  # Sắp xếp theo tên trạm đo
        .collect(streaming=True)  # Thu thập dữ liệu theo dạng streaming để tiết kiệm bộ nhớ
    )
    
    # In kết quả cuối cùng
    print("{", end="")  
    for data in grouped.iter_rows():  
        print(
            f"{data[0]}= {data[1]:.1f} / {data[2]:.1f} / {data[3]:.1f}",  
            end="\n",
        )
    print("\b\b} ")  

    end_time = timeit.default_timer()  

    # Lấy bộ nhớ sau khi hoàn thành
    memory_after = process.memory_info().rss / (1024 * 1024) 
    print(f"Memory usage after: {memory_after:.2f} MB")  

    # Tính toán bộ nhớ đã sử dụng
    memory_used = memory_after - memory_before  
    elapsed_time = end_time - start_time  

    # In ra các thông số về thời gian và bộ nhớ
    print(f"Elapsed time: {elapsed_time:.2f} sec")  
    print(f"Memory used during process: {memory_used:.2f} MB")  

elapsed_time = timeit.timeit(df, number=1)
