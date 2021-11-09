from rest_framework import serializers
from apps.api.models import Plates
from apps.api.models import Sections
from apps.api.models import Menu


class PlatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plates
        fields = ['id', 'name', 'allergens']


class SectionsSerializer(serializers.ModelSerializer):
    plates = serializers.SerializerMethodField()

    def get_plates(self, model):
        plates = model.plates.all()
        serializer = PlatesSerializer(plates, many=True)

        return serializer.data

    class Meta:
        model = Sections
        fields = ['id', 'name', 'order', 'plates']


class MenuSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField()

    def get_sections(self, model):
        sections = model.sections.all().order_by('order')
        serializer = SectionsSerializer(sections, many=True)

        return serializer.data

    class Meta:
        model = Menu
        fields = ['id', 'name', 'price', 'sections']
