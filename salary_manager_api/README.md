# Salary Manager API

Project FastAPI yang sudah di-upgrade agar lebih siap dipakai project lain.

## Upgrade yang sudah ditambahkan

- **SQLite database** untuk penyimpanan permanen
- **CORS enabled** agar bisa diakses frontend/project lain
- **Update employee**
- **Delete employee**
- **Filter salary slip berdasarkan bulan**
- **Export salary slip ke PDF**

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

### Employee
- `GET /employees`
- `POST /employees`
- `GET /employees/{employee_id}`
- `PUT /employees/{employee_id}`
- `DELETE /employees/{employee_id}`

### Salary
- `POST /salary/calculate`
- `GET /salary/slips`
- `GET /salary/slips?month=2026-04`
- `GET /salary/slip/{employee_id}`
- `GET /salary/slip/{employee_id}/pdf`

## Contoh body update employee

```json
{
  "position": "Senior Backend Developer",
  "base_salary": 10000000,
  "allowance": 2000000
}
```

## Contoh body salary calculate

```json
{
  "employee_id": 1,
  "overtime_hours": 8,
  "bonus": 500000,
  "deduction": 100000,
  "period_month": "2026-04"
}
```

## Cara menjalankan

```bash
cd /home/fhnasgf/.openclaw/workspace/salary_manager_api
pyenv activate django
pip install -r requirements.txt
uvicorn main:app --reload --port 8001
```

## Dokumentasi API

- Swagger UI: `http://127.0.0.1:8001/docs`
- ReDoc: `http://127.0.0.1:8001/redoc`

## Cara export PDF

Setelah salary slip dibuat, buka endpoint berikut di browser atau dari frontend:

```bash
http://127.0.0.1:8001/salary/slip/1/pdf
```

## Copy ke project lain

```bash
cp -r /home/fhnasgf/.openclaw/workspace/salary_manager_api /media/fhnasgf/Data1/NGODING/pythonDasar/
```

## Commit di project tujuan

```bash
cd /media/fhnasgf/Data1/NGODING/pythonDasar/salary_manager_api
git add .
git commit -m "Upgrade salary manager API with employee management, monthly filtering, and PDF export"
git push
```
