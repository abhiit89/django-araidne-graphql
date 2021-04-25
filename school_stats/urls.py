from django.urls import path, include
from ariadne.contrib.django.views import GraphQLView
from .resolver import schema
urlpatterns = [
    path('graphql/', GraphQLView.as_view(schema=schema), name='graphql'),
    path('', GraphQLView.as_view(schema=schema), name='graphql'),
]
