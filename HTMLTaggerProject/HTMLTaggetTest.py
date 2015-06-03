__author__ = 'Luis'

import unittest

from HTMLTaggerProject.HTMLGen import HTMLGen

class HTMLTaggetTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.htmlGen = HTMLGen()

    def test_a(self):
        self.assertEqual(self.htmlGen.a(''), '<a></a>')
        self.assertEqual(self.htmlGen.a('test'), '<a>test</a>')

    #Python is asserting the text as encoded, so can't verify this
        #def test_a_special_keyword(self):
        #self.it("Testing a generation with a String with HTML keywords")
        #self.assert_equals(htmlGen.a('<test&>'), unicode('<a>&lttest&amp&gt</a>', ("utf_8")) )

    def test_comment(self):
        self.assertEqual(self.htmlGen.comment('test'), '<!--test-->')

    def test_b(self):
        self.assertEqual(self.htmlGen.b('test'), '<b>test</b>')

    def test_p(self):
        self.assertEqual(self.htmlGen.p('test'), '<p>test</p>')

    def test_body(self):
        self.assertEqual(self.htmlGen.body('test'), '<body>test</body>')

    def test_span(self):
        self.assertEqual(self.htmlGen.span('test'), '<span>test</span>')

    def test_div(self):
        self.assertEqual(self.htmlGen.div('test'), '<div>test</div>')

    def test_title(self):
        self.assertEqual(self.htmlGen.title('test'), '<title>test</title>')

    def test_complete(self):
        test_wrap_with_a = self.htmlGen.a('test')
        test_wrap_with_a_p = self.htmlGen.p(test_wrap_with_a)
        self.assertEqual(test_wrap_with_a_p, "<p><a>test</a></p>")
        test_comment_wrap_with_a_p = self.htmlGen.comment(test_wrap_with_a_p)
        self.assertEqual(test_comment_wrap_with_a_p, "<!--<p><a>test</a></p>-->")