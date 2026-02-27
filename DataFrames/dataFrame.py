import pandas as pd

datal = [['AAA', 25, 'Pune'],
       ['BBB', 30, 'Mumbai'],
       ['CCC', 35, 'Nasik']]


df = pd.DataFrame(datal,columns=['Name', 'Age', 'City'])
print(df)

