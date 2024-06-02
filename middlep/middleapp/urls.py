from django.urls import path
from . import views
urlpatterns = [
    path("manual/",views.manual_view,name="manual"),
    path("restrict/",views.restrict_view,name="restrict")
]
