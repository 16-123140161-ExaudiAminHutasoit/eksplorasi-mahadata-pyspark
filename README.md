# Eksplorasi Mahadata — Klasifikasi Penyakit Jantung dengan PySpark

Replikasi parsial alur klasifikasi berbasis Apache Spark yang terinspirasi oleh artikel Ed-daoudy dan Maalmi (2019), *A new Internet of Things architecture for real-time prediction of various diseases using machine learning on big data environment* ([DOI](https://doi.org/10.1186/s40537-019-0271-7)).

Eksperimen menggunakan dataset **Cleveland Heart Disease** dari [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/45/heart+disease) dan dijalankan di Google Colab dengan PySpark mode lokal. Eksperimen ini tidak membangun ulang komponen streaming, Kafka, atau Cassandra dari sistem pada artikel.

## Isi repositori

```text
eksplorasi-mahadata-pyspark/
├── README.md
├── requirements.txt
├── download_data.py
├── notebooks/
│   └── Eksplorasi_Mahadata.ipynb
└── hasil/
    ├── hasil_eksperimen.json
    └── prediksi_data_uji.csv
```

## Cara menjalankan

Buka `notebooks/Eksplorasi_Mahadata.ipynb` melalui Google Colab. Pilih runtime **CPU**, kemudian jalankan semua sel secara berurutan dari atas. Notebook sudah mencakup instalasi Java 17 dan PySpark 4.0.1, pengunduhan dataset, pembersihan, pelatihan, evaluasi, dan penyimpanan hasil. Tidak perlu mengunggah dataset secara manual.

Eksperimen yang dicatat berjalan di Colab dengan Python 3.13.16, Java 17, Spark 4.0.1, dan mode `local[2]`. Bila menggunakan lingkungan lain, pasang dependensi dari `requirements.txt` dan siapkan Java yang sesuai. Skrip `download_data.py` tersedia untuk mengunduh dataset secara terpisah: `python download_data.py`. Notebook tetap mengunduh data sendiri, jadi skrip ini tidak wajib dijalankan sebelum notebook.

## Metode yang dicoba

Data awal berisi 303 baris. Enam baris dengan nilai hilang pada atribut `ca` atau `thal` dihapus, sehingga tersisa 297 baris. Target `num` diubah menjadi dua label: `0` untuk nilai asli 0, dan `1` untuk nilai asli 1–4. Kolom `num` tidak digunakan sebagai fitur.

Data dibagi menggunakan `randomSplit([0.7, 0.3], seed=42)`; pembagian aktual menghasilkan 220 baris latih dan 77 baris uji. Pipeline terdiri atas `VectorAssembler`, `VectorIndexer` (`maxCategories=5`), dan `DecisionTreeClassifier` (`maxDepth=5`, `maxBins=32`, `seed=42`).

## Hasil satu kali eksekusi

| Ukuran | Hasil |
|---|---:|
| Accuracy | 83,12% |
| Precision kelas 1 | 78,57% |
| Recall kelas 1 | 75,86% |
| F1-score kelas 1 | 77,19% |
| TN / FP / FN / TP | 42 / 6 / 7 / 22 |
| Kedalaman / jumlah node pohon | 5 / 39 |
| Waktu pemanggilan `pipeline.fit()` | 3,9546 detik |

Angka di atas berasal dari eksekusi notebook yang tersimpan dalam `hasil/hasil_eksperimen.json` dan `hasil/prediksi_data_uji.csv`. Waktu eksekusi pada percobaan ulang bisa berubah. Pembagian acak tidak menggunakan stratifikasi kelas.

**Batasan:** ini adalah replikasi parsial, bukan implementasi identik metode C4.5 pada artikel. Dataset hanya 297 baris setelah pembersihan, sehingga percobaan ini tidak mengukur manfaat Spark pada data berukuran besar. Evaluasi dilakukan pada satu pembagian data, bukan validasi silang; hasilnya bukan dasar diagnosis medis.

## Catatan penggunaan AI

ChatGPT digunakan sebagai bantuan untuk memahami panduan, menyusun dan menjelaskan bagian kode, menelusuri error, serta membantu dokumentasi. Eksekusi eksperimen dan pemeriksaan output dilakukan melalui Google Colab; hasil yang disimpan tidak diubah untuk menyamakan angka dengan artikel. Penggunaan AI juga dijelaskan pada laporan tugas.

## Referensi

Ed-daoudy, A., & Maalmi, K. (2019). A new Internet of Things architecture for real-time prediction of various diseases using machine learning on big data environment. *Journal of Big Data, 6*, Article 104. https://doi.org/10.1186/s40537-019-0271-7

UCI Machine Learning Repository. Heart Disease dataset. https://archive.ics.uci.edu/dataset/45/heart+disease
