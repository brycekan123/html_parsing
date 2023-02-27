"""This program will return a combined list of unordered and ordered lists when given a html file.
Time Complexity: O(1). Space Complexity: O(N).
"""
from html.parser import HTMLParser
from bs4 import BeautifulSoup


class MyHTMLParser(HTMLParser):
    """creates an environment for parsing text files formatted in HTML and XHTML"""

    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

    class ListCollector:
        """creates environment a list for unordered or ordered list when fed an HTML file"""
        def __init__(self, html_file):
            self.html_file = html_file
            self.ul_list = []
            self.ol_list = []
            self.combine_list = []

        def set_lists(self):
            """creates a combined list of the unordered and ordered lists """
            with open(self.html_file, "r") as f:
                data = f.read()
                soup = BeautifulSoup(data, features="html.parser")
                self.list_maker(soup, "ul")
                self.list_maker(soup, "ol")
            self.combine_list.append(self.ul_list)
            self.combine_list.append(self.ol_list)

        def list_maker(self, soup_data, arg):
            """creates both unordered and ordered lists"""
            parent = soup_data.find("body").find(arg)
            text = list(parent.descendants)
            if arg == "ul":
                for i in range(2, len(text), 3):
                    self.ul_list.append(text[i])
            if arg == "ol":
                for i in range(2, len(text), 3):
                    self.ol_list.append(text[i])

        def get_lists(self):
            """returns combined list"""
            self.set_lists()
            return self.combine_list


