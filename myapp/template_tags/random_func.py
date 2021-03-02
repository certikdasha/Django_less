from django import template
import random
import string


register = template.Library()


@register.filter(name='random_numb')
def random_numb(value):
    value = random.randint(1, 1000)
    return value


@register.filter(name='rand_str')
def rand_str(value):
    s = string.ascii_lowercase
    result_str = ''.join(random.choice(s) for i in range(random.randint(5, 10)))
    return result_str


# register.filter('random_numb', random_numb)
# register.filter('rand_str', rand_str)
