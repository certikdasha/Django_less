from datetime import datetime

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render



def first(request):
    return HttpResponse("Hey! It's your first view!!")

#
# def index(request):
#     return HttpResponse("It's index page!!")


def main_article(request):
    return HttpResponse('There will be a list with articles')


def uniq_article(request):
    return HttpResponse('This is uniq answer for uniq value')


def article(request, article_id, name=''):
    return HttpResponse(
        "This is an article #{}. {}".format(article_id, "Name of this article is {}".format(
            name) if name else "This is unnamed article"))


# def articles(request):
#     return HttpResponse("It's articles!")
#
#
# def users(request):
#     return HttpResponse("It's users!!")
#
#
# def archive(request):
#     return HttpResponse('archive')


def id_user(request, user_number):
    return HttpResponse(
        f"User's number {user_number}"
    )
#
#
# def artcl_number(request, article_number):
#     return HttpResponse(
#         f"This is {article_number} article."
#     )


# def arch_artcl_nmb(request, article_number):
#     return HttpResponse(
#         f"This is {article_number} article archive."
#     )

#
# def arch_nmb_name(request, article_number, slug_name):
#     return HttpResponse(
#         f"this is article #{article_number}. Name of this article is {slug_name}"
#     )


def tel_nmb(request, tel):
    return HttpResponse(
        "This telephone number is {}".format(tel)
    )


def cod(request, code):
    return HttpResponse(
        f"This code: {code}"
    )


class MyClass:
    string = ''

    def __init__(self, s):
        self.string = s


def index(request):
    my_num = 33
    my_str = 'some string'
    my_dict = {"some_key": "some_value"}
    my_list = ['list_first_item', 'list_second_item', 'list_third_item']
    my_set = {'set_first_item', 'set_second_item', 'set_third_item'}
    my_tuple = ('tuple_first_item', 'tuple_second_item', 'tuple_third_item')
    my_class = MyClass('class string')
    return render(request, 'index.html', {
        'my_num': my_num,
        'my_str': my_str,
        'my_dict': my_dict,
        'my_list': my_list,
        'my_set': my_set,
        'my_tuple': my_tuple,
        'my_class': my_class,
        'display_num': True,
        'now': datetime.now(),
    })


def first(request):
    return render(request, 'first.html')


def articles(request):
    return render(request, "acricles.html")


def users(request):
    return render(request, "users.html")


def archive(request):
    return render(request, 'archive.html')


def artcl_number(request, article_number):
    return render(request, 'number.html', {
        'number': article_number,
    })


def arch_nmb_name(request, article_number, slug_name):
    return render(request, 'arch_nmb_name.html', {
        'number': article_number,
        'text': slug_name
    })
