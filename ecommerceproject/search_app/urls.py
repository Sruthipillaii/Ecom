from django.urls import path

import search_app
from .import views
app_name='search_app'

urlpatterns=[
    path('',search_app.views.SearchResult,name='SearchResult'),
]