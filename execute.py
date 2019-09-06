import pandas as pd
from new import Multi_Variable

titanic = pd.read_csv("D:\\Sarita Naik\\Visual Studio Codes\\Statistical Analysis\\ExploratoryAnalysis\\train.csv")

bs = Multi_Variable()
a = bs.group_func(titanic,['Sex'],['Age'],'count')
b = bs.multi_func(titanic,'Sex')
c = bs.graph_func(titanic,'Survived','PassengerId')
print(c)