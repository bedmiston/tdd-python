# from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'lists.views.home_page', name='home'),
    url(r'^lists/', include('lists.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += patterns('',
#                             url(r'^__debug__/', include(debug_toolbar.urls)),
#                             )
