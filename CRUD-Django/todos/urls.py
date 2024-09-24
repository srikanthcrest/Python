from django.urls import path
from admin_user_api.views import MyObtainTokenPairView, RegisterView
from rest_framework_simplejwt.views import TokenRefreshView
from .import views


urlpatterns = [
    path('', views.index, name='index'),

    path('/save', views.saveAction, name='save'),

    path('/edittodo/<int:pk>', views.editTodo, name='edittodo'),

    path('/delete/<int:pk>', views.deleteAction, name='delete')

    # path('/save', views.saveAction, name='save'),
]