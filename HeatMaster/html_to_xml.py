
import html.parser
import xml.etree.ElementTree as ET
import sys
import re

class HTMLtoXMLParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.root = ET.Element("root")
        self.element_stack = [self.root]

    def handle_starttag(self, tag, attrs):
        # Clean attributes
        cleaned_attrs = {}
        for k, v in attrs:
            if v is None:
                v = ''
            # Replace Django template tags in attributes
            v = re.sub(r'{%.*?%}', '', v)
            v = re.sub(r'{{.*?}}', '', v)
            cleaned_attrs[k] = v
        
        element = ET.SubElement(self.element_stack[-1], tag, cleaned_attrs)
        self.element_stack.append(element)

    def handle_endtag(self, tag):
        if self.element_stack and self.element_stack[-1].tag == tag:
            self.element_stack.pop()

    def handle_data(self, data):
        data = data.strip()
        if data:
            # Ignore Django template tags in data
            data = re.sub(r'{%.*?%}', '', data)
            data = re.sub(r'{{.*?}}', '', data)
            if data.strip():
                self.element_stack[-1].text = data.strip()

    def get_xml(self):
        return self.root

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python html_to_xml.py <input_html_file> <output_xml_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    parser = HTMLtoXMLParser()
    parser.feed(html_content)
    xml_tree = parser.get_xml()

    # tostring in Python 3.8+ defaults to 'unicode', which is what we want.
    # For older versions, encoding might be needed.
    xml_string = ET.tostring(xml_tree, encoding='unicode', method='xml')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(xml_string)

    print(f"Successfully converted {input_file} to {output_file}")
