from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist

from .base import BaseViewSet

from rest_framework import status
from rest_framework.response import Response

from apps.api.models import Plates
from apps.api.models import Sections
from apps.api.models import Menu

from apps.api.serializers import PlatesSerializer
from apps.api.serializers import SectionsSerializer
from apps.api.serializers import MenuSerializer


class PlatesViewSet(BaseViewSet):
    model_class = Plates
    serializer_class = PlatesSerializer


class SectionsViewSet(BaseViewSet):
    model_class = Sections
    serializer_class = SectionsSerializer


class MenuViewSet(BaseViewSet):
    model_class = Menu
    serializer_class = MenuSerializer

    def get_queryset(self, **kwargs):
        queryset = super(MenuViewSet, self).get_queryset(**kwargs)

        name = kwargs.get('name', None)
        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset

    def create(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                data = request.data.copy()
                sections = data.get('sections', [])

                menu = Menu()
                menu.name = data.get('name')
                menu.price = data.get('price')
                menu.save()

                # Save sections
                if len(sections):
                    self.save_sections(menu, sections)

                return Response({
                    'message': 'Menú has been created'
                }, status=status.HTTP_201_CREATED)
        except Exception as e:
            transaction.rollback()
            return Response({
                'message': 'An error has ocurred',
                'err': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('pk', None)
            if not pk:
                # Response error if id doesn't be provided
                return Response({
                    'message': 'Id is required'
                }, status=status.HTTP_400_BAD_REQUEST)

            with transaction.atomic():
                data = request.data.copy()
                sections = data.get('sections', [])

                try:
                    # Find item in db
                    menu = Menu.objects.get(id=pk)
                except ObjectDoesNotExist:
                    # Raise Error if item doesn't exists
                    return Response({
                        'message': 'Item not found'
                    }, status=status.HTTP_404_NOT_FOUND)

                menu.name = data.get('name')
                menu.price = data.get('price')
                menu.save()

                # Save sections
                menu.sections.all().delete()
                if len(sections):
                    self.save_sections(menu, sections, is_updated=True)

                return Response({
                    'message': 'Menú has been updated'
                }, status=status.HTTP_200_OK)

        except Exception as e:
            transaction.rollback()
            return Response({
                'message': 'An error has ocurred',
                'err': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def save_sections(self, model, sections, is_updated=False):
        """
        Create sections into db, find data and if exists update the instance else create new instance
        """
        for s in sections:
            try:
                section = Sections.objects.get(name__iexact=s['name'])
            except ObjectDoesNotExist:
                section = Sections()

            plates = s.get('plates', [])
            section.name = s['name']
            section.order = s['order']
            section.save()

            if is_updated:
                section.plates.all().delete()

            if len(plates):
                self.save_plates(section, plates)

            model.sections.add(section)

    @staticmethod
    def save_plates(model, plates):
        """
        Create plates into db, find data and if exists update the instance else create new instance
        """
        for p in plates:
            try:
                plate = Plates.objects.get(name__iexact=p['name'], allergens__iexact=p['allergens'])
            except ObjectDoesNotExist:
                plate = Plates()
                plate.name = p['name']
                plate.allergens = p['allergens']
                plate.save()

            model.plates.add(plate)

