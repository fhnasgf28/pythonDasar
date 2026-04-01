# Salary Manager API

Project FastAPI yang sudah di-upgrade agar lebih siap dipakai project lain.

## Upgrade yang sudah ditambahkan

- **SQLite database** untuk penyimpanan permanen
- **CORS enabled** agar bisa diakses frontend/project lain
- **Data karyawan dan slip gaji persisten**
- Struktur project lebih rapi dengan file terpisah

## Struktur project

```bash
salary_manager_api/
├── main.py
├── models.py
├── database.py
├── requirements.txt
├── salary_manager.db   # otomatis dibuat saat dijalankan
└── README.md
```

## Endpoint

### `GET /`
Info dasar API.

### `GET /employees`
Ambil semua data karyawan.

### `POST /employees`
Tambah karyawan baru.

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

### `GET /employees/{employee_id}`
Ambil detail satu karyawan.

### `POST /salary/calculate`
Hitung gaji bulanan dan simpan salary slip ke database.

Contoh body:

```json
{
  "employee_id": 1,
  "overtime_hours": 8,
  "bonus": 500000,
  "deduction": 100000
}
```

### `GET /salary/slips`
Ambil semua slip gaji.

### `GET /salary/slip/{employee_id}`
Ambil slip gaji terbaru berdasarkan employee id.

## Cara menjalankan

### Pakai pyenv `django`

```bash
cd /home/fhnasgf/.openclaw/workspace/salary_manager_api
pyenv activate django
pip install -r requirements.txt
uvicorn main:app --reload --port 8001
```

## Dokumentasi API

- Swagger UI: `http://127.0.0.1:8001/docs`
- ReDoc: `http://127.0.0.1:8001/redoc`

## Cara pakai dari project lain

### JavaScript / Frontend

```javascript
fetch("http://127.0.0.1:8001/employees")
  .then((res) => res.json())
  .then((data) => console.log(data));
```

### Hitung gaji dari project lain

```javascript
fetch("http://127.0.0.1:8001/salary/calculate", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    employee_id: 1,
    overtime_hours: 8,
    bonus: 500000,
    deduction: 100000
  })
})
  .then((res) => res.json())
  .then((data) => console.log(data));
```

## Catatan

Untuk production, sebaiknya lanjut upgrade dengan:
- auth/login
- environment file (`.env`)
- PostgreSQL
- folder `routers/`, `services/`, `schemas/`
