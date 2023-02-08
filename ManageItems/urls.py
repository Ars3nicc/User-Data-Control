from django.urls import path
from . import views
from .views import detail_view
urlpatterns = [
    path('<id>', detail_view ),
    path('', views.main),
    path('aboutus/', views.aboutus),
    path('usertable/', views.usertable),
    path('create/', views.create_view),
    path('detail/', views.detail_view),
    path('update/', views.update_view)
]
