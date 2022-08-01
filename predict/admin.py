from django.contrib import admin


from .models import Dataset
from .models import Attribute
from .models import Content

admin.site.register(Dataset)
admin.site.register(Attribute)
admin.site.register(Content)

