import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props(self):
        node = HTMLNode("a", "click me", None, {"href": "https://boot.dev"})
        self.assertEqual(node.props_to_html(), ' href="https://boot.dev"')

    def test_props_not(self):
        node = HTMLNode("a", "clicker", None, {"href": "https://boot.dev"})
        self.assertNotEqual(node.props_to_html(), 'href="https://boot.dev"')

    def test_props_none(self):
        node = HTMLNode('a', "raha", None, None)
        self.assertEqual(node.props_to_html(), "")

if __name__ == "__main__":
    unittest.main()