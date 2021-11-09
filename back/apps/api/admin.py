from django.contrib import admin
from apps.api.models import Plates
from apps.api.models import Sections
from apps.api.models import Menu


admin.site.register([Plates, Sections, Menu])
