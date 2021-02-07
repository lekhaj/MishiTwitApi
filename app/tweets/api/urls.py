from django.urls import path
from django.conf.urls import url
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

# existing serializer, viewset, router registrations code
...

# Create our schema's view w/ the get_schema_view() helper method. Pass in the proper Renderers for swagger
# schema_view = get_schema_view(title='Tweets API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

from .views import (
    tweet_action_view,
    tweet_delete_view,
    tweet_detail_view,
    tweet_feed_view,
    tweet_list_view,
    tweet_create_view,
)
'''
CLIENT
Base ENDPOINT /api/tweets/
'''
urlpatterns = [
    # url(r'^', schema_view, name="docs"),
    path('', tweet_list_view),
    path('feed/', tweet_feed_view),
    path('action/', tweet_action_view),
    path('create/', tweet_create_view),
    path('<int:tweet_id>/', tweet_detail_view),
    path('<int:tweet_id>/delete/', tweet_delete_view),
]

# urlpatterns += router.urls
