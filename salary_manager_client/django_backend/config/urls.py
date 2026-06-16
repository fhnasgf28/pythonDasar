from django.urls import include, path

urlpatterns = [
    path("api/", include("salary_app.urls")),
]
