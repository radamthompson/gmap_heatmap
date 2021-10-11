import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np

def parser(data, tags):
    tree = ET.iterparse(data)
    
    for event, node in tree:
        if node.tag in tags:
            yield node.tag, node.text




