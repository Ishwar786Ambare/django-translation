from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns 
from django.utils.translation import gettext_lazy as _
from pages.views import change_language

urlpatterns = [
    path('change_language/', 
         change_language, 
         name='change_language')
]

urlpatterns += i18n_patterns(
        path('', include('pages.urls')),
        path(_('admin/'), admin.site.urls),
        prefix_default_language=False
    )