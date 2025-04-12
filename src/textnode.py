from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold text"
    ITALIC = "italic text"
    CODE = "code text"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
       return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})" 






def text_node_to_html_node(node: TextNode):
    if node.text_type == TextType.BOLD:
        return LeafNode("b",node.text)   
    elif node.text_type == TextType.ITALIC:
        return LeafNode("i",node.text)
    elif node.text_type == TextType.CODE:
        return LeafNode("code",node.text)  
    elif node.text_type == TextType.TEXT:
        return LeafNode(value=node.text)
    
    elif node.text_type == TextType.LINK:
        return LeafNode("a",node.text, {"href":node.url})    
    elif node.text_type == TextType.IMAGE:
        return LeafNode("img",node.text,{"src":node.url})
    else:
        raise ValueError("Invalid 'TextType'")
    
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []        
    
    for node in old_nodes:
        if delimiter == '`': # code
            pass
        elif delimiter == '**': # Bold
            pass
        elif delimiter == "_": #Italic
            pass
