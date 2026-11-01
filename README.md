# Dashboard Meteorit dengan Flask

Aplikasi web sederhana menggunakan Flask untuk menampilkan visualisasi data meteorit.
Dibuat untuk Praktikum Aplikasi Web Modul 6.

**Nama:** Benedikta Anyarita Pratiwi
**NIM:** 24051130019

## Dataset

`meteorites.csv` berisi 19.282 data meteorit dari tahun 1900 hingga 2013, dengan kolom
nama, tipe, kelas, grup, massa, status (Fell/Found), tahun, dan lokasi.

## Isi Dashboard

- Ringkasan: total meteorit, rata-rata massa, jumlah Fell dan Found
- Peta persebaran meteorit
- Grafik jumlah meteorit per tahun
- Grafik distribusi tipe meteorit
- Grafik jumlah meteorit per kelas

## Struktur Folder

```
meteor-flask/
├── data/
│   └── meteorites.csv
├── templates/
│   └── dashboard.html
├── app.py
└── requirements.txt
```

## Cara Menjalankan

```
pip install -r requirements.txt
python app.py
```

Buka http://127.0.0.1:5000 di browser.
