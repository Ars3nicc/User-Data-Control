from django.urls import path
from . import views
from .views import detail_view
urlpatterns = [
    path('', views.main),
    path('aboutus/', views.aboutus),
    path('usertable/', views.usertable),
    path('stdtable/', views.student_table),
    path('tchtable/', views.teacher_table),
    path('create/', views.create_view),
    path('detail/<int:id>', views.detail_view),
    path('update/<int:id>', views.update_view),
    path('delete/<int:id>', views.delete_view),
    path('json/', views.json_view)  
]
