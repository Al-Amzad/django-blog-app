from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
	path ('admin/', admin.site.urls),
	path ('account/', include ('app_login.urls')),
	path ('blog/', include ('app_blog.urls')),
	path ('', views.Index, name = 'index'),
]

urlpatterns += staticfiles_urlpatterns ()
urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
