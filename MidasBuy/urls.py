
from django.contrib import admin
from django.urls import path,include,re_path
# from core.views import call_back_view


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^auth/', include('drf_social_oauth2.urls'),name='drf'),
    # path('login/callback',call_back_view,name="call-back"),
    path('core/',include('core.urls')),
    # path('user/',include('django.contrib.auth.urls'))
]

