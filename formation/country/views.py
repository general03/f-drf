from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from country.serializers import CountrySerializer
from country.models import Country



# def test(request):
#     """Serialization simple, slide 40"""
#     c = Country()
#     c.code = 'IT'
#     c.name = 'Italie'
#     cs = CountrySerializer(c)
#     return JsonResponse(cs.data)

def test(request):
    """Serialization avec vérification, slide 42, 44 et 46"""
    cs = CountrySerializer(data={'code': 'fr', 'name': 'France'}, context={'request': request})
    print(cs.is_valid())
    # cs.save()
    return JsonResponse(cs.data)


# def test(request):
#     """Serialization avec vérification d'un champ spécifique, slide 48"""
#     c = Country()
#     c.code = 'fr'
#     c.name = 'France'
#     serializer = CountrySerializer(c, data={"code": "FR"}, partial=True)
#     print(serializer.is_valid())
#     print(serializer.save())
#     return JsonResponse(serializer.data)


def front(request):
    return render(request, 'index.html')