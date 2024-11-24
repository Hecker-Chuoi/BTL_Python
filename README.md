# BTL Python: ONE BILLION ROW CHALLENGE (1BRC)

## 1. Giới thiệu
One Billion Row Challenge (1BRC) là một cuộc thi công nghệ được tổ chức vào T1/2024, nhằm kiểm tra hiệu suất và khả năng tối ưu hóa sử dụng ngôn ngữ Java khi xử lý một tập dữ liệu khổng lồ.

Nhiệm vụ: phân tích và tổng hợp dữ liệu nhiệt độ từ một file văn bản chứa 1 tỷ dòng dữ liệu, tương đương 13.8 GB, bao gồm dữ liệu của 413 trạm thời tiết khác nhau.

**Thành viên nhóm:**
|STT|Họ tên|Mã Sinh viên|
|---|---|---|
|1|Nguyễn Hữu Tiến|B22DCCN722|
|2|Lê Hương Giang|B22DCCN248|
|3|Đỗ Lý Minh Anh|B22DCCN012|
|4|Trần Đức Chính|B22DCCN115|
|5|Thái Đoàn Trường|B22DCCN488|

## 2. Nội dung
Slide trình bày: [link](https://www.canva.com/design/DAGXOJcndbA/hmJ9pibEqPZkxi16XVDEmg/edit?utm_content=DAGXOJcndbA&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton).

|Phần|Nội dung|Phụ trách|Link|
|---|---|---|---|
|1|Giới thiệu đề tài|Giang|[Introduce](https://docs.google.com/document/d/1byyW0y2JiM_cmBuKfdakkTefFMRQGGc-xePNEp1soLk/edit?fbclid=IwZXh0bgNhZW0CMTEAAR3MdyGmkxiKTXUi2nq4YANsLmNNW9_rt_dY_jfyNqwqaqns-LhkL-Jyrzc_aem_W0tH850ptOlu-vzdfjo4tw&tab=t.0)|
|2.1|Cách tiếp cận cơ bản|Giang|[Basic approach](https://docs.google.com/document/d/1byyW0y2JiM_cmBuKfdakkTefFMRQGGc-xePNEp1soLk/edit?fbclid=IwZXh0bgNhZW0CMTEAAR3MdyGmkxiKTXUi2nq4YANsLmNNW9_rt_dY_jfyNqwqaqns-LhkL-Jyrzc_aem_W0tH850ptOlu-vzdfjo4tw&tab=t.0)|
|2.2|Sử dụng đa luồng|Trường|[Multiprocess](https://docs.google.com/document/d/15itUwXk6Wu21kn5Exbf-vWlZXGvgGRPtlX71cv8NJZs/edit?fbclid=IwZXh0bgNhZW0CMTEAAR3OKYUs9NWBc2pwzPvkzGNg6p_Ah21MgYZ9USLyWi3vnobu30Ud_P_HARg_aem_fyQo1di23I5EAJXl4gMElA&tab=t.0#heading=h.8350c5r69s8f)|
|2.3|Các bước tối ưu chương trình|Tiến|[Optimization](https://github.com/Hecker-Chuoi/BTL_Python/blob/main/doc/optimization.md)|
|2.4|Sử dụng external libraries|Chính|[External libraries](https://docs.google.com/document/d/1fDtjwv2iUcF5O6jBFLNuziNW98ejdb0dNir-Lngdi4s/edit?hl=vi&fbclid=IwZXh0bgNhZW0CMTEAAR0OGsz7sHU0MWY89ExOtUUUvEvRNqPz12eyQr0ZCb2IxbFQIxuxAomCm24_aem_z819w2sh61GrlC7tnLoY_A&tab=t.0#heading=h.sp7dwac2v0xv)|
|3|So sánh với ngôn ngữ khác|Minh Anh|[Compare with Java](https://docs.google.com/document/d/1DuAyR36lFnTOveXDlVqbo4V1YBjHtmGBKDTPDLbWxro/edit?fbclid=IwZXh0bgNhZW0CMTEAAR0hb9MFG6tFWUuFpcBdjfssB5oR9X0yKaNpyADcUnPNMmt3w_0mBuvta9o_aem_3N_QabSzVOq0SkvofigYzA&tab=t.0)|
|4|Hướng phát triển tiếp theo|Minh Anh|[Next step](https://docs.google.com/document/d/1DuAyR36lFnTOveXDlVqbo4V1YBjHtmGBKDTPDLbWxro/edit?fbclid=IwZXh0bgNhZW0CMTEAAR0hb9MFG6tFWUuFpcBdjfssB5oR9X0yKaNpyADcUnPNMmt3w_0mBuvta9o_aem_3N_QabSzVOq0SkvofigYzA&tab=t.0)|

## 3. Cấu trúc dự án
```plain text
│   README.md                           # Mô tả dự án
│
├───Java solution
│       Blog1.java                      # Basic approach sử dụng Java
│       Blog2.java                      # Multithread trên Java
│       Blog6.java                      # Multithread trên Java đã tối ưu
│
└───Python solution
        basicApproach.py                # Basic approach sử dụng Python
        calculateAverage_v0.py          # Multithread trên Python
        calculateAverage_v1.py          # Cải tiến 1
        calculateAverage_v2.py          # Cải tiến 2
        calculateAverage_v3.py          # Cải tiến 3
        calculateAverage_v4.py          # Cải tiến 4
        calculateAverage_v5.py          # Cải tiến 5: code Python tối ưu
        calculateAverageDuckDB.py       # Sử dụng DuckDB
        calculateAveragePolars.py       # Sử dụng Polars
```

## 4. Hướng dẫn cài đặt
Cài đặt CPython, Pypy, Java JDK.

**Cài đặt các thư viện hỗ trợ**
1. Mở thư mục `Python solution` trên cmd
2. Cài đặt các thư viện trong requirements.txt
    ```bash
    pip install -r .\requirements.txt #hoac
    pypy -m pip install -r .\requirements.txt
    ```

**Tạo file dữ liệu**
1. Mở thư mục `Python solution` trên cmd
2. Chạy file createMeasurements.py
    ```bash
    python createMeasurements.py
    ```
*Lưu ý: chọn phân vùng có dung lượng trống >= 15Gb.*

**Chạy chương trình**  
Chạy và kiểm nghiệm trên thực tế tốc độ các solution Java và Python.