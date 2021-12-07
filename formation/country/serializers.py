from rest_framework import serializers
from country.models import Country

class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = [
            'code',
            'name',
        ]
    
    def validate_code(self, value):
        if value != value.upper():
            raise serializers.ValidationError("Code is not upper case")
        return value

    def validate(self, data):
        if data['code'].lower() in data['name'].lower():
            return data
        raise serializers.ValidationError("The Code is not in Name")

# class CountrySerializer(serializers.HyperlinkedModelSerializer):

#     class Meta:
#         model = Country
#         fields = '__all__'
        