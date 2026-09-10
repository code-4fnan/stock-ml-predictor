from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This connects the empty root URL to your predictor app
    path('', include('predictor.urls')), 
]