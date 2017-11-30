import pandas as pd
import xlrd
import json

#excel_file = pd.read_excel("fisher_current_panda.xlsx")
#excel_to_json =  pd.DataFrame(excel_file)

pd.read_excel("fischer_current_panda.xlsx").to_json("output.json")



