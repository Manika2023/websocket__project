
from django.urls import path
from . import views
# urlpatterns = [
#     path('',views.index)
# ]

# dynamic url pattern
urlpatterns = [
    path('<str:group_name>/',views.index)
]
