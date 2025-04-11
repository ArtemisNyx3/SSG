from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value = None, props=None):
        if value == None:
             raise ValueError("'Value' is a requred argument" )
        self.tag = tag
        self.value = value
        self.props = props
    
    def props_to_html(self):
        html = ""
        if self.props == None: 
             return
        for x in self.props.keys():
            html += f"{x}={self.props[x]} "
        return html
        
    def to_html(self):
        if self.tag == None:
            return f"{self.value}"
        self.tag = self.tag.lower()

        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>" if self.props != None else f"<{self.tag}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"HTMLNode({self.tag.lower()}, {self.value}, {self.props})"

    def __eq__(self, other):
                return self.tag.lower() == other.tag.lower() and self.value == other.value and self.props == other.props
