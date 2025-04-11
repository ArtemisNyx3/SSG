import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq_props_to_html(self):
        node = HTMLNode("a", "Boot.Dev", None, {"href":"www.boot.dev", "target": "_blank",})
        node2 = HTMLNode("a", "Boot.Dev", None, {"href":"www.boot.dev", "target": "_blank",})
        self.assertEqual(node.props_to_html(), node2.props_to_html())
    
    def test_eq(self):
        node = HTMLNode("A", "Boot.Dev", None, {"href":"www.boot.dev", "target": "_blank",})
        node2 = HTMLNode("a", "Boot.Dev", None, {"href":"www.boot.dev", "target": "_blank",})
        self.assertEqual(node, node2)
    
    def test_neq(self):
        node = HTMLNode("a", "BOOT.Dev", None, {"href":"www.boot.dev", "target": "_blank",})
        node2 = HTMLNode("a", "Boot.Dev", None, {"href":"www.boot.dev", "target": "_blank",})
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
