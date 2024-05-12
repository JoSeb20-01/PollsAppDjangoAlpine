from typing import List

from django import template
from django.template.base import NodeList

class IdentifierNode(template.Node):

    def __init__(self, nodelist, id_block):
        self.nodelist: NodeList = nodelist
        self.id_block = id_block

    def render(self, context: template.Context):
        return self.nodelist.render(context)

class ModalNode(template.Node):

    def __init__(self, nodelist):
        self.nodelist: NodeList = nodelist

    def _render_list(self, context: template.Context):
        nodes: List[IdentifierNode] = self.nodelist.get_nodes_by_type(IdentifierNode)
        new_context = {}
        for node in nodes:
            new_context[node.id_block] = node.render(context)
        return new_context

    def render(self, context: template.Context):
        new_context = self._render_list(context)
        t = context.template.engine.get_template("modal.html")
        return t.render(template.Context(new_context, autoescape=context.autoescape))
