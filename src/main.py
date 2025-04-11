from textnode import TextNode,TextType

def main():
    tnode = TextNode("This is some ancor text", TextType.LINK, "https://www.boot.dev")
    print(tnode.__repr__())

if __name__ == "__main__":
    main()