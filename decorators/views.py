from django.http.response import HttpResponse
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view, authentication_classes
from .models import Result
from rest_framework.response import Response 
from .token_authentication import FaculatyAuthentication
from rest_framework import status

# Create your views here.


@require_http_methods(["GET"])
def print_query(request, pk):
    if not pk:
        return HttpResponse("Pleae give a query")

    else:
        return HttpResponse(pk)

@api_view(["GET"])
@authentication_classes([FaculatyAuthentication])
def get_result(request):
    result = Result.objects.all().values()
    print(result)
    return Response(list(result), status=status.HTTP_200_OK)