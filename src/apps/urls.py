from django.conf.urls import include, url
from django.contrib import admin

import theme.views
import vuln.urls


urlpatterns = [
    url(r'^$', theme.views.home, name='home'),
    url(r'^vuln/', include(vuln.urls, namespace='vuln')),
    url(r'^admin/', include(admin.site.urls)),
]
