# BTL Python: ONE BILLION ROW CHALLENGE (1BRC)

## 1. Giới thiệu
One Billion Row Challenge (1BRC) là một cuộc thi công nghệ được tổ chức vào T1/2024, nhằm kiểm tra hiệu suất và khả năng tối ưu hóa sử dụng ngôn ngữ Java khi xử lý một tập dữ liệu khổng lồ.

Nhiệm vụ: phân tích và tổng hợp dữ liệu nhiệt độ từ một file văn bản chứa 1 tỷ dòng dữ liệu, tương đương 13.8 GB, bao gồm dữ liệu của 413 trạm thời tiết khác nhau.

## 2. Nội dung
|Nội dung|Phụ trách|Link|
|---|---|---|
|Giới thiệu đề tài|Giang|[Introduce](https://docs.google.com/document/d/1byyW0y2JiM_cmBuKfdakkTefFMRQGGc-xePNEp1soLk/edit?fbclid=IwZXh0bgNhZW0CMTEAAR3MdyGmkxiKTXUi2nq4YANsLmNNW9_rt_dY_jfyNqwqaqns-LhkL-Jyrzc_aem_W0tH850ptOlu-vzdfjo4tw&tab=t.0)|
|Cách tiếp cận cơ bản|Giang|[Basic approach](https://docs.google.com/document/d/1byyW0y2JiM_cmBuKfdakkTefFMRQGGc-xePNEp1soLk/edit?fbclid=IwZXh0bgNhZW0CMTEAAR3MdyGmkxiKTXUi2nq4YANsLmNNW9_rt_dY_jfyNqwqaqns-LhkL-Jyrzc_aem_W0tH850ptOlu-vzdfjo4tw&tab=t.0)|
|Sử dụng đa luồng|Trường|[Multiprocess](https://docs.google.com/document/d/15itUwXk6Wu21kn5Exbf-vWlZXGvgGRPtlX71cv8NJZs/edit?fbclid=IwZXh0bgNhZW0CMTEAAR3OKYUs9NWBc2pwzPvkzGNg6p_Ah21MgYZ9USLyWi3vnobu30Ud_P_HARg_aem_fyQo1di23I5EAJXl4gMElA&tab=t.0#heading=h.8350c5r69s8f)|
|Các bước tối ưu chương trình|Tiến|[Optimization]()|
|Sử dụng external libraries|Chính|[External libraries](https://docs.google.com/document/d/1fDtjwv2iUcF5O6jBFLNuziNW98ejdb0dNir-Lngdi4s/edit?hl=vi&fbclid=IwZXh0bgNhZW0CMTEAAR0OGsz7sHU0MWY89ExOtUUUvEvRNqPz12eyQr0ZCb2IxbFQIxuxAomCm24_aem_z819w2sh61GrlC7tnLoY_A&tab=t.0#heading=h.sp7dwac2v0xv)|
|So sánh với ngôn ngữ khác|Minh Anh|[Compare with Java](https://docs.google.com/document/d/1DuAyR36lFnTOveXDlVqbo4V1YBjHtmGBKDTPDLbWxro/edit?fbclid=IwZXh0bgNhZW0CMTEAAR0hb9MFG6tFWUuFpcBdjfssB5oR9X0yKaNpyADcUnPNMmt3w_0mBuvta9o_aem_3N_QabSzVOq0SkvofigYzA&tab=t.0)|
|Hướng phát triển tiếp theo|Minh Anh|[Next step](https://docs.google.com/document/d/1DuAyR36lFnTOveXDlVqbo4V1YBjHtmGBKDTPDLbWxro/edit?fbclid=IwZXh0bgNhZW0CMTEAAR0hb9MFG6tFWUuFpcBdjfssB5oR9X0yKaNpyADcUnPNMmt3w_0mBuvta9o_aem_3N_QabSzVOq0SkvofigYzA&tab=t.0)|

## 3. Cấu trúc
```plain text
├── Python solution/                   # Mã nguồn chính của dự án
│   ├── basicApproach.py            # File chạy chính
│   ├── utils.py           # Các hàm hỗ trợ
├── docs/                  # Tài liệu hoặc báo cáo
├── tests/                 # Bộ kiểm thử
└── README.md              # File mô tả dự án
```

## 4. 