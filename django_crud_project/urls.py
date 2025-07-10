from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='base.html'), name='home'),
    path('accounts/', include('accounts.urls')),
    path('oficinas/', include('oficinas.urls')),
    path('personas/', include('personas.urls')),
    path('captcha/', include('captcha.urls')),
]