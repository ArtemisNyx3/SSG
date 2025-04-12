from textnode import TextType,TextNode

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
