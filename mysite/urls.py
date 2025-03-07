from django.urls import include,path
from django.contrib import admin

urlpatterns = [
    path("", include("blog.urls")),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]
