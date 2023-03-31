from django.http import JsonResponse
from django.middleware.csrf import get_token

class LoginHelper():
    def get_csrf_token(request):
        response = JsonResponse({"message": "CSRF Cookie successfully stored as HTTP Only"})
        response["X-CSRFToken"] = get_token(request)
        return response