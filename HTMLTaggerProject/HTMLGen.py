__author__ = 'Luis'

A_TAG = "a"
B_TAG = "b"
P_TAG = "p"
BODY_TAG = "body"
DIV_TAG = "div"
SPAN_TAG = "span"
TITLE_TAG = "title"
GENERIC_TAG_WRAPPER_FORMAT = "<{1}>{0}</{1}>"
COMMENT_FORMAT = "<!--{0}-->"

class HTMLGen:

    def a(self, content):
        #content = self.escape_HTML_keywords(content)
        return self.wrap_content_with_tag(content, A_TAG)

    def comment(self, content):
        return COMMENT_FORMAT.format(content)

    def b(self, content):
        return self.wrap_content_with_tag(content, B_TAG)

    def p(self, content):
        return self.wrap_content_with_tag(content, P_TAG)

    def body(self, content):
        return self.wrap_content_with_tag(content, BODY_TAG)

    def span(self, content):
        return self.wrap_content_with_tag(content, SPAN_TAG)

    def title(self, content):
        return self.wrap_content_with_tag(content, TITLE_TAG)

    def div(self, content):
        return self.wrap_content_with_tag(content, DIV_TAG)

    def wrap_content_with_tag(self, content, tag):
        return GENERIC_TAG_WRAPPER_FORMAT.format(content, tag)

    #Python is asserting the text as encoded, so can't verify this
    def escape_HTML_keywords(self, content):
        content = content.replace("<", "&lt")
        content = content.replace(">", "&gt")
        content = content.replace("&", "&amp")
        return content