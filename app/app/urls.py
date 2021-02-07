"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, re_path, include # url()
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
from rest_framework_simplejwt import views as jwt_views

# existing serializer, viewset, router registrations code
...

# Create our schema's view w/ the get_schema_view() helper method. Pass in the proper Renderers for swagger
# schema_view = get_schema_view(title='Tweets API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

urlpatterns = [
    # url(r'^', schema_view, name="docs"),
    path('admin/', admin.site.urls),
    # re_path(r'profiles?/', include('profiles.urls')),
    path('api/tweets/', include('tweets.api.urls')),
    path('api/profiles?/', include('profiles.api.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
