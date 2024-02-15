from country.serializers import CountrySerializer
from country.models import Country
from country.group_permission import GroupPermission

from rest_framework.renderers import JSONRenderer
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

class CountryViewSet(viewsets.ModelViewSet):

    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'code'

    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [GroupPermission]

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['code']
    ordering = ['name', 'code']

    @action(detail=False, methods=['get'])
    def count_country(self, request, pk=None):
        count = Country.objects.all().count()
        return Response(count)

    # def get_queryset(self):
        # return Country.objects.filter(code='FR')

    # def list(self, request):
    #     serializer = CountrySerializer(Country.objects.all(), many=True, context={'request': request})
    #     return Response(serializer.data)

# APIView
class ListCountryAPIView(APIView):

    def get(self, request, format=None):
        print(request.GET)
        serializer = CountrySerializer(Country.objects.all(), many=True)
        return Response(serializer.data)
    
# ViewSet
class ListCountryViewSet(viewsets.ViewSet):

    queryset = Country.objects.all()
    def list(self, request):
        serializer = CountrySerializer(self.queryset, many=True)
        return Response(serializer.data)

# GenericAPIViews
class ListCountryGenericAPIView(generics.ListCreateAPIView):

    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    # Surcharge possible 
    def list(self, request):
        codes = []
        for c in Country.objects.all():
            if c.code == 'FR':
                codes.append(c)
        serializer = CountrySerializer(codes, many=True)
        return Response(serializer.data)



