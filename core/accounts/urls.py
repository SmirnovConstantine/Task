from django.urls import path, include
from knox import views as knox_views
from .views import RegisterAPI, UserAPI, EnterAPI


urlpatterns = [
    path('api/v1/auth/', include('knox.urls')),
    path('api/v1/auth/register/', RegisterAPI.as_view(), name="register"),
    path('api/v1/auth/enter/', EnterAPI.as_view(), name="login"),
    path('api/v1/auth/user/<int:pk>/', UserAPI.as_view(), name="user"),
    path('api/v1/auth/logout/', knox_views.LogoutView.as_view(), name="knox_logout"),

]
