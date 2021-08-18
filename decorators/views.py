from django.http.response import HttpResponse
from django.views.decorators.http import require_http_methods
# Create your views here.


@require_http_methods(["GET"])
def print_query(request, pk):
    if not pk:
        return HttpResponse("Pleae give a query")

    else:
        return HttpResponse(pk)