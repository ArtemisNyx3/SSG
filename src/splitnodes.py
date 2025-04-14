from textnode import TextType,TextNode
from extractmarkdown import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(sections[i], node.text_type))
            else:
                new_nodes.append(TextNode(sections[i], text_type))
    # print(f"New nodes are --- {new_nodes}")
    return new_nodes

# TODO: Logic to handle duplicate image markdown
def helper(old_nodes,split_type):
    new_nodes = []
    for node in old_nodes:
        link_mds = extract_markdown_images(node.text) if split_type == TextType.IMAGE else extract_markdown_links(node.text)
        link_mds = list(link_mds)[::-1]
        markdown = [node.text]
        # print(f"Markdown extracted image stack --- {link_mds}")
        # print(f"Markdown Text Stack            --- {markdown}")
        while link_mds!= None and len(link_mds) > 0:
            img_info = link_mds.pop()
            text = markdown.pop()
            if text == '':
                pass
            sections = text.split(f"![{img_info[0]}]({img_info[1]})", 1) if split_type == TextType.IMAGE else text.split(f"[{img_info[0]}]({img_info[1]})", 1)
            new_nodes.append(TextNode(sections[0],node.text_type)) # Left is the text before the img/link
            # The link/image
            new_nodes.append(TextNode(img_info[0],TextType.IMAGE,img_info[1])) if split_type == TextType.IMAGE else  new_nodes.append(TextNode(img_info[0],TextType.LINK,img_info[1])) 
            markdown.append(sections[1]) # The string that left contains rest of the info
    # print(f"New Nodes are - {new_nodes}")
    for x in markdown:
        if x != '':
            new_nodes.append(TextNode(x,node.text_type))
    return new_nodes

def split_nodes_image(old_nodes):
       return helper(old_nodes, TextType.IMAGE)

    

def split_nodes_link(old_nodes):
       return helper(old_nodes, TextType.LINK)

def text_to_textnodes(text):
    nodes = [TextNode(text,TextType.TEXT)]
    
    nodes = split_nodes_image(nodes)
    print("******** Split images  ***********")
    print(f"Nodes ---- {nodes}")
    print("*******************")
    nodes = split_nodes_link(nodes)
    print("******** Split links  ***********")
    print(f"Nodes ---- {nodes}")
    print("*******************")

    nodes = split_nodes_delimiter(nodes, '_', TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, '**', TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, '`', TextType.CODE)

    
    print("*******************")
    print(f"Nodes ---- {nodes}")
    print("*******************")

    return nodes
