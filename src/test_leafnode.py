import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode(tag="a", value="Boot.Dev", props={"href":"www.boot.dev", "target": "_blank",})
        node2 = LeafNode(tag="A",value= "Boot.Dev",props= {"href":"www.boot.dev", "target": "_blank",})
        self.assertEqual(node.to_html(), node2.to_html())
    
    def test_eq(self):
        node = LeafNode(tag="a", value="Boot.Dev", props={"href":"www.boot.dev", "target": "_blank",})
        node2 = LeafNode(tag="A",value= "Boot.Dev",props= {"href":"www.boot.dev", "target": "_blank",})
        self.assertEqual(node, node2)
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


if __name__ == "__main__":
    unittest.main()