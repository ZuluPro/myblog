from random import choice
from django import template

register = template.Library()
SENTENCES = [
    'Brain archives',
    "Brain dump",
    "'Cause I need somewhere to write my thoughts",
    'Python, Django et pas de cul',
    '<code>mysql < /dev/brain</code>',
    "Welcome to Zulu's brain",
    "Maybe boring stuff for you",
    "Follow my train of thought",
]


@register.simple_tag
def random_sentence():
    return choice(SENTENCES)
