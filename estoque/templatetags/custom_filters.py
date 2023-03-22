from django import template

register = template.Library()


def isinstance_filter(value, class_name):
    return isinstance(value, type(class_name))

register.filter('isinstance', isinstance_filter)