#import lib
import pandas as pd



# converion of xml data into other form

path = "dict/1.xml"

data = pd.read_xml(path)

data.head()



