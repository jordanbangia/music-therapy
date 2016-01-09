import re
from django import template

numeric_test = re.compile("^\d+$")
register = template.Library()


def getattrib(value, arg):
    if hasattr(value, str(arg)):
        return getattr(value, arg)
    elif hasattr(value, 'has_key') and value.has_key(arg):
        return value[arg]
    elif numeric_test.match(str(arg)) and len(value) > int(arg):
        return value[int(arg)]
    else:
        return None

register.filter('getattrib', getattrib)
