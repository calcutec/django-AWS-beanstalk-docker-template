"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import url, include                                                                                                                                      
from django.contrib import admin                                                                                                                                               
from django.views.generic import TemplateView                                                                                                                                  
from web.views import *

                                                                                                                                                                               
urlpatterns = [                                                                                                                                                                
#    url(r'^admin/', admin.site.urls),                                                                                                                                          
#    url(r'^about/', AboutView.as_view(), name='about'),                                                                                                                        
#    url(r'^contact/$', ContactView.as_view(), name='contact'),                                                                                                                 
    url(r'^$', IndexView.as_view(), name='home'),                                                                                                                              
]                                                                                                                                                                              
                                                                                                                                                                               
# Return a robots.txt that disallows all spiders when DEBUG is True.                                                                                                           
'''
if getattr(settings, "DEBUG", True):                                                                                                                                           
    urlpatterns += [                                                                                                                                                           
        url(r'^robots.txt$',                                                                                                                                                   
            lambda r: HttpResponse("User-agent: *\nDisallow: /", content_type="text/plain")),                                                                                  
    ]                                                                                                                                                                          
else:                                                                                                                                                                          
    urlpatterns += [                                                                                                                                                           
        url(r'^robots.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots_file")                                                  
    ]                                                                                                                                                                          
'''
                                                                                                                                                                               
# Add in the Django toolbar if we're in debug mode                                                                                                                             
if settings.DEBUG:                                                                                                                                                             
    import debug_toolbar                                                                                                                                                       
    urlpatterns.append(url(r'^__debug__/', include(debug_toolbar.urls)))                                                                                                       
                                                                           
