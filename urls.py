from django.conf.urls.defaults import *
from django.conf import settings
from sparklez import views

#static
from django.views.static import serve

#admin
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    (r'^$', views.base),
    (r'^about/', views.about),

    #admin
    (r'^admin/password_reset/$', 'django.contrib.auth.views.password_reset'),
    (r'^admin/password_reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    (r'^admin/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm'),
    (r'^admin/reset/done/$', 'django.contrib.auth.views.password_reset_complete'),
    (r'^accounts/login/(.*)', admin.site.urls),
    (r'^admin/',include(admin.site.urls)),
)

if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        (r'^.*?media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
