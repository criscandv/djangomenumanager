from .viewsets import *
from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'plates', PlatesViewSet, 'Plates')
router.register(r'sections', SectionsViewSet, 'Sections')
router.register(r'menus', MenuViewSet, 'Menu')
