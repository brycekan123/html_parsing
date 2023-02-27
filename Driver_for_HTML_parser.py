"""Driver code for Lab 3, an HTML parsing assignment of getting ordered and unordered lists"""
import BryceKanLab3

if __name__ == "__main__":
    parser = BryceKanLab3.MyHTMLParser()
    print(parser.ListCollector("/Users/brycekan/Downloads/lists.html").get_lists())

"""
---Run Output--
[['An item', 'Another', 'And another one'], ['Item one', 'Item two', 'Item three', 'Item four']]
"""