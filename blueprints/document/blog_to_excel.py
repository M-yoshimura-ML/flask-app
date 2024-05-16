import pandas as pd
import openpyxl

url = 'https://info.finance.yahoo.co.jp/ranking/?kd=45'

# read_html により、<table>要素が対象となる
df = pd.read_html(url)
print(df)
# df[0].to_excel('salary_ranking.xlsx')
