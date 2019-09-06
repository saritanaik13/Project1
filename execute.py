import pandas as pd
from new import Multi_Variable
from new import Uni_Variable

titanic = pd.read_csv("D:\\Sarita Naik\\Visual Studio Codes\\Statistical Analysis\\ExploratoryAnalysis\\train.csv")

bs = Multi_Variable()
vs = Uni_Variable()
#a = bs.group_func(titanic,'Sex','Fare','median')
#b = bs.multi_func(titanic,'Sex')
#bs.graph_func(titanic,'Sex','Embarked')
a = vs.multi_func(titanic,'Age', 'mean')
print(a)