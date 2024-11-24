import duckdb  
import timeit  
import psutil  
import os  

def process():
    # Lấy thông tin bộ nhớ trước khi chạy đoạn mã
    process = psutil.Process(os.getpid())  
    memory_before = process.memory_info().rss / (1024 * 1024)  
    print(f"Memory usage before: {memory_before:.2f} MB")  

    start_time = timeit.default_timer()  

    with duckdb.connect() as conn:  # Tạo kết nối tạm thời với DuckDB
        # Import CSV vào bộ nhớ và thực hiện truy vấn SQL
        data = conn.sql(
            """
            SELECT
                station_name,                                                       -- Tên của trạm đo
                MIN(measurement) AS min_measurement,                                -- Giá trị nhỏ nhất của đo lường
                CAST(AVG(measurement) AS DECIMAL(8,1)) AS mean_measurement,         -- Giá trị trung bình (CAST để định dạng số thập phân)
                MAX(measurement) AS max_measurement                                 -- Giá trị lớn nhất của đo lường
            FROM READ_CSV(                                                          -- Đọc tệp CSV trực tiếp
                'measurements.txt',                                                 -- Đường dẫn tới tệp CSV
                header=false,                                                       -- Không có header trong tệp CSV
                columns={'station_name':'VARCHAR','measurement':'DECIMAL(8,1)'},    -- Định nghĩa kiểu dữ liệu các cột
                delim=';',                                                          -- Dấu phân cách giữa các giá trị trong CSV
                parallel=true                                                       -- Bật chế độ xử lý song song để tăng tốc
            )
            GROUP BY
                station_name                                                        -- Nhóm dữ liệu theo từng trạm đo
            """
        )

        # In kết quả cuối cùng
        print("{", end="")  
        for row in sorted(data.fetchall()):  
            print(f"{row[0]} = {row[1]} / {row[2]} / {row[3]}", end="\n")
        print("\b\b} ")

    end_time = timeit.default_timer() 

    # Lấy thông tin bộ nhớ sau khi hoàn thành xử lý
    memory_after = process.memory_info().rss / (1024 * 1024) 
    print(f"Memory usage after: {memory_after:.2f} MB") 

    # Tính toán bộ nhớ đã sử dụng
    memory_used = memory_after - memory_before 
    elapsed_time = end_time - start_time  

    # In ra các thông số về thời gian và bộ nhớ
    print(f"Elapsed time: {elapsed_time:.2f} sec") 
    print(f"Memory used during process: {memory_used:.2f} MB")  

elapsed_time = timeit.timeit(process, number=1)
