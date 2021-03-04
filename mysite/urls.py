"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include
# from myapp.views import first, index
#
# urlpatterns = [
#     path('my_url/', include('myapp.urls')),
#     path('', index, name='index')
# ]
from django.urls import include, path, re_path
from django.contrib import admin
from myapp.views import index, articles, users, archive, id_user, artcl_number
from myapp.views import cod, arch_nmb_name, tel_nmb, first

# urlpatterns = [
#     path('my_url/', include('myapp.urls')),
#     path('', index, name='index'),
#     path('article/', main_article, name='mail_article'),
#     path('article/33/', uniq_article, name='uniq_article'),
#     path('article/<int:article_id>/', article, name='article'),
#     path('article/<int:article_id>/<slug:name>', article, name='article_name'),
#     path('articles/', articles, name='articles'),
#     path('users/', users, name='users'),
#     path('articles/archive/', archive, name='archive'),
#
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my_url/', include('myapp.urls')),
    path('', index, name='index'),
    path('acricles/', articles, name='articles'),
    path('users/', users, name='users'),
    path('acrticles/archive/', archive, name='archive'),
    path('article/<int:article_number>/', artcl_number, name='numb'),
    # path('article/<int:article_number>/archive', arch_artcl_nmb),
    path('article/<int:article_number>/<slug:slug_name>', arch_nmb_name, name='arch_nmb_name'),
    path('users/<int:user_number>', id_user),
    re_path(r'(?P<tel>(\+380|0)(39|50|63|66|67|68|73|91|92|93|94|95|96|97|98|99)[0-9]{7})/?$', tel_nmb),
    re_path(r'(?P<code>([1-9a-f]){4}[--]([1-9a-f]){6})/$', cod),
    path('first/', first, name='first')
]
