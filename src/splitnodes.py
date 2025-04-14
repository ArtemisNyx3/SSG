from textnode import TextType,TextNode
from extractmarkdown import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        flg = False
        start=0
        for i in range(len(node.text)):
            if node.text[i] == delimiter:
                # print(f"found deliitter at {i}")
                if flg == False:
                    # print(f"flg false subNode is from {start} to {i} indicies --- {node.text[start:i]}")
                    end = i
                    # start - end = texttype of node
                    if end-start!= start:
                        new_nodes.append(TextNode(node.text[start: end], node.text_type))
                    start = end
                    flg = True 
                else:
                    # print(f"flg true subNode is from {start} to {i} indicies --- {node.text[start:i+1]}")

                    end = i
                    # start - end = texttype from arg
                    nstr = node.text[start + 1: end]
                    if len(nstr) != 0:
                        new_nodes.append(TextNode(nstr, text_type))
                    start = end+1
                    flg = False
        if (start != len(node.text) -1):
            new_nodes.append(TextNode(node.text[start:],node.text_type))
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
            sections = text.split(f"![{img_info[0]}]({img_info[1]})", 1)
            new_nodes.append(TextNode(sections[0],node.text_type)) # Left is the text before the img/link
            # The link/image
            new_nodes.append(TextNode(img_info[0],TextType.IMAGE,img_info[1])) if split_type == TextType.IMAGE else  new_nodes.append(TextNode(img_info[0],TextType.LINK,img_info[1])) 
            markdown.append(sections[1]) # The string that left contains rest of the info
    # print(f"New Nodes are - {new_nodes}")
    return new_nodes

def split_nodes_image(old_nodes):
       return helper(old_nodes, TextType.IMAGE)

    

def split_nodes_link(old_nodes):
       return helper(old_nodes, TextType.LINK)

