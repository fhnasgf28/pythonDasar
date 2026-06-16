import json

import requests
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

BASE = settings.FASTAPI_BASE_URL
TIMEOUT = 10


@csrf_exempt
def employee_list(request):
    if request.method == "GET":
        resp = requests.get(f"{BASE}/employees", timeout=TIMEOUT)
        return JsonResponse(resp.json(), safe=False, status=resp.status_code)

    if request.method == "POST":
        data = json.loads(request.body)
        resp = requests.post(f"{BASE}/employees", json=data, timeout=TIMEOUT)
        return JsonResponse(resp.json(), safe=False, status=resp.status_code)

    return JsonResponse({"detail": "Method not allowed"}, status=405)


@csrf_exempt
def employee_detail(request, employee_id):
    if request.method == "GET":
        resp = requests.get(f"{BASE}/employees/{employee_id}", timeout=TIMEOUT)
        return JsonResponse(resp.json(), safe=False, status=resp.status_code)

    if request.method == "PUT":
        data = json.loads(request.body)
        resp = requests.put(f"{BASE}/employees/{employee_id}", json=data, timeout=TIMEOUT)
        return JsonResponse(resp.json(), safe=False, status=resp.status_code)

    if request.method == "DELETE":
        resp = requests.delete(f"{BASE}/employees/{employee_id}", timeout=TIMEOUT)
        return JsonResponse(resp.json(), safe=False, status=resp.status_code)

    return JsonResponse({"detail": "Method not allowed"}, status=405)


@csrf_exempt
def calculate_salary(request):
    if request.method == "POST":
        data = json.loads(request.body)
        resp = requests.post(f"{BASE}/salary/calculate", json=data, timeout=TIMEOUT)
        return JsonResponse(resp.json(), safe=False, status=resp.status_code)

    return JsonResponse({"detail": "Method not allowed"}, status=405)


def salary_slips(request):
    month = request.GET.get("month")
    params = {"month": month} if month else {}
    resp = requests.get(f"{BASE}/salary/slips", params=params, timeout=TIMEOUT)
    return JsonResponse(resp.json(), safe=False, status=resp.status_code)
