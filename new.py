import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Multi_Variable:
    
    def __init__(self):
        pass

    def group_func(self,df_1,value_1,value_2,func_1):
        value = df_1.pivot_table(index = value_1, values = value_2, aggfunc = func_1)
        return value
    
    def multi_func(self,df_1,value_1):
        value = df_1[value_1].value_counts()
        return value

    def graph_func(self,df_1,value_1,value_2):
        type_1 = df_1[value_1].dtype
        type_2 = df_1[value_2].dtype

        if(type_1 == 'int64' and type_2 == 'int64'):