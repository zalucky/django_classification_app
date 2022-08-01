
from django.urls import path
from . import views

from django.contrib import admin

app_name = 'predict'


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),

    path('import_dataset/', views.import_dataset, name="import_dataset"),
    path('import_csv/', views.import_csv, name="import_csv"),

    path('datasets/', views.datasets, name="datasets"),
    path('approval/', views.approval, name="approval"),

    path('args2/', views.args2, name='args2'),
    path('args2_chances/', views.args2_chances, name='args2_chances'),
    path('args3/', views.args3, name='args3'),
    path('args3_chances/', views.args3_chances, name='args3_chances'),
    path('args4/', views.args4, name='args4'),
    path('args4_chances/', views.args4_chances, name='args4_chances'),
    path('args5/', views.args5, name='args5'),
    path('args5_chances/', views.args5_chances, name='args5_chances'),
    path('args6/', views.args6, name='args6'),
    path('args6_chances/', views.args6_chances, name='args6_chances'),
    path('args7/', views.args7, name='args7'),
    path('args7_chances/', views.args7_chances, name='args7_chances'),
    path('args8/', views.args8, name='args8'),
    path('args8_chances/', views.args8_chances, name='args8_chances'),
    path('args9/', views.args9, name='args9'),
    path('args9_chances/', views.args9_chances, name='args9_chances'),

    path('database_list/', views.database_list, name="database_list"),
    
]