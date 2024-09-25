from django.urls import path
from .import views
from .views import TodoCreate


# urlpatterns = [
    # path('', views.index, name='index'),

    # path('/save', views.saveAction, name='save'),

    # path('/edittodo/<int:pk>', views.editTodo, name='edittodo'),

    # path('/delete/<int:pk>', views.deleteAction, name='delete')

    # path('/save', views.saveAction, name='save'),
# ]

urlpatterns = [
    # path('create', views.create, name='create'),
    path('create', TodoCreate.as_view(), name='create'),
    # path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    # path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('register/', RegisterView.as_view(), name='auth_register'),
    # path('users-list/', ListUsers.as_view(), name='list_users'),
]