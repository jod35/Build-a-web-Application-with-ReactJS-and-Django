from django.contrib import admin
from django.urls import path,include
from notes.views import NotesViewset
from rest_framework.routers import DefaultRouter

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="Guest Book API",
      default_version='v1',
      description="This is a guest book API",   
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



router=DefaultRouter()

router.register('posts',NotesViewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
