from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from app.views.login import Login,Logout

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [

    path('login/',Login.as_view(),name='Login'),
    path('logout/',Logout.as_view(),name='Logout'),
    path('admin/', admin.site.urls),  
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    path('', include('app.urls')),


]
