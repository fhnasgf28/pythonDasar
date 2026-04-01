# Salary Manager API

Project FastAPI sederhana untuk mengelola data karyawan dan menghitung gaji bulanan.

## Fitur

- Melihat daftar karyawan
- Menambah data karyawan
- Melihat detail karyawan berdasarkan ID
- Menghitung gaji bulanan
- Menyimpan salary slip sementara di memory
- Melihat daftar salary slip dan slip terakhir per karyawan

## Endpoint

### 1. `GET /`
Menampilkan informasi dasar API.

### 2. `GET /employees`
Mengambil semua data karyawan.

### 3. `POST /employees`
Menambah data karyawan baru.

Contoh body:

```json
{
  "name": "Rina",
  "position": "Finance Staff",
  "base_salary": 6500000,
  "allowance": 1000000,
  "overtime_rate": 35000,
  "tax_percent": 5
}
```

### 4. `GET /employees/{employee_id}`
Mengambil detail satu karyawan.

### 5. `POST /salary/calculate`
Menghitung gaji bulanan.

Contoh body:

```json
{
  "employee_id": 1,
  "overtime_hours": 8,
  "bonus": 500000,
  "deduction": 100000
}
```

### 6. `GET /salary/slips`
Melihat semua salary slip yang sudah dihitung.

### 7. `GET /salary/slip/{employee_id}`
Melihat slip gaji terbaru untuk karyawan tertentu.

## Cara Menjalankan

### Opsi virtualenv biasa

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Opsi pyenv environment `django`

```bash
pyenv activate django
pip install -r requirements.txt
uvicorn main:app --reload
```

## Dokumentasi otomatis

Setelah dijalankan, buka:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Struktur project

```bash
salary_manager_api/
├── main.py
├── requirements.txt
└── README.md
```
