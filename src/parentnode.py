from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        if tag == None:
            raise ValueError("'Tag' is not optional")
        if children == None:
            raise ValueError("'Children' is not optional")
        self.tag = tag
        self.children = children
        self.props = props
    
    def to_html(self):
        html = f"<{self.tag}>"
        for node in self.children:
            html += node.to_html()
        html += f"</{self.tag}>"
        return html
