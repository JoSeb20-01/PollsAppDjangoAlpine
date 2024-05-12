from django import template
from django.template.base import Token, Parser

from core.templatetags.base import ModalNode, IdentifierNode

register = template.Library()

@register.tag(name="modal")
def do_modal(parser: Parser, token: Token = None):
    nodelist = parser.parse(('end_modal', ))
    parser.delete_first_token()
    return ModalNode(nodelist)

@register.tag(name="id")
def identifier(parser: Parser, token: Token):
    nodelist = parser.parse(('end_id', ))
    parser.delete_first_token()
    return IdentifierNode(nodelist, token.contents.split()[1])
