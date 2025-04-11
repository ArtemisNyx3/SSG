from enum import Enum

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html = ""
        for x in self.props.keys():
            html += f"{x}={self.props[x]} "
        return html
    
    def __repr__(self):
        return f"HTMLNode({self.tag.lower()}, {self.value}, {self.children}, {self.props})"

    def __eq__(self, other):
        return self.tag.lower() == other.tag.lower() and self.value == other.value and self.children == other.children and self.props == other.props