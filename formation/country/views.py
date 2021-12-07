from curses import meta
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from country.serializers import CountrySerializer
from country.models import Country



# def test(request):
#     c = Country()
#     c.code = 'IT'
#     c.name = 'Italie'
#     cs = CountrySerializer(c)
#     return JsonResponse(cs.data)

def test(request):
    cs = CountrySerializer(data={'code': 'fr', 'name': 'France'})
    print(cs.is_valid())
    return JsonResponse(cs.errors)


# def test(request):
#     c = Country()
#     c.code = 'FR'
#     c.name = 'France'
#     serializer = CountrySerializer(c, data={'name': 'FRANCE'}, partial=True)
#     print(serializer.is_valid())
#     print(serializer.save())
#     return JsonResponse(serializer.data)


def front(request):
    return render(request, 'index.html')