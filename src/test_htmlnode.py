import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


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

    def test_leafnode_a(self):
        node = LeafNode("a", "Buna seara!")
        self.assertEqual(node.to_html(), "<a>Buna seara!</a>")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leafnode_b(self):
        node = LeafNode("b", "Buna seara!")
        self.assertEqual(node.to_html(), "<b>Buna seara!</b>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(),
                         "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()
