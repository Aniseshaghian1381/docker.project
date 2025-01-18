
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings  # good idea
from django.views.generic import TemplateView
# from FirstProj import settings # bad idea

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('catalogue/', include('catalogue.urls')),
    path('basket/', include('basket.urls')),
    path('shipping/', include('shipping.urls')),
    # path('about/', about, name='about-us'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about-us'),
    # path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
