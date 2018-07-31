from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^user-info/', views.show_user_info, name= 'user-info')
]
