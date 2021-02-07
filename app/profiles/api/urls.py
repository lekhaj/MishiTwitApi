from django.urls import path
from django.conf.urls import url
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

# existing serializer, viewset, router registrations code
...

# Create our schema's view w/ the get_schema_view() helper method. Pass in the proper Renderers for swagger
# schema_view = get_schema_view(title='Tweets API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

from .views import (
    profile_detail_api_view,
)
'''
CLIENT
Base ENDPOINT /api/profiles/
'''
urlpatterns = [
    # url(r'^', schema_view, name="docs"),
    path('<str:username>/', profile_detail_api_view),
    path('<str:username>/follow', profile_detail_api_view),
]
