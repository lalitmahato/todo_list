from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def testing_rest(rquest):
    data = {
        "name":"Lalit",
        "age":21,
        "city":"Lucknow"
    }
    return JsonResponse(data)