import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Multi_Variable:
    
    def __init__(self):
        pass

    def group_func(self,df_1,value_1,value_2,func_1):
        value = df_1.pivot_table(index = value_1, values = value_2, aggfunc = func_1)
        return value
    
    def graph_func(self,df_1,value_1,value_2):
        type_1 = df_1[value_1].dtype
        type_2 = df_1[value_2].dtype

        if((type_1 == 'int64'or type_1 == 'float64') and (type_2 == 'int64' or type_2 == 'float64')):
            plt.scatter(df_1[value_1],df_1[value_2])
            plt.show()
        elif((type_1 != 'int64'and type_1 != 'float64') and (type_2 != 'int64' and type_2 != 'float64')):
            a = df_1.pivot_table(index = value_2, values = value_1, aggfunc = 'count')
            print(a)
        else:
            plt.figure(figsize=(7,7))
            plt.title("Categorical and Quantitative Graphs")

            if(type_1 == 'int64' or type_1 == 'float64'):
                plt.bar(df_1[value_2],df_1[value_1])
                plt.xlabel(value_2)
                plt.ylabel(value_1)    
                plt.show()
            else:
                plt.bar(df_1[value_1],df_1[value_2])
                plt.xlabel(value_1)
                plt.ylabel(value_2)    
                plt.show()

class Uni_Variable:
    def __init__(self):
        pass

    def multi_func(self,df_1,value_1,func_1):
        if(func_1 == 'count'):
            return df_1[value_1].value_counts()
        elif(func_1 == 'mean'):
            return df_1[value_1].mean()
        elif(func_1 == 'median'):
            return df_1[value_1].median()
        else:
            return "Mention a valid function among count, mean, median"
        
    def bs_boxplot(self, bs_value):
        plt.boxplot(bs_value)
        plt.show()