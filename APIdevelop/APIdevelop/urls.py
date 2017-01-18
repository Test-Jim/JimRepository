
"""APIdevelop URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from views import helloworld,current_datatime
from inventory.views import  search_form,get_tester_info

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^helloworld/$',helloworld),
    url(r'^current_datatime/$',current_datatime),
    url(r'^search_form/$',search_form),
    url(r'^get_tester_info/$',get_tester_info),


]
