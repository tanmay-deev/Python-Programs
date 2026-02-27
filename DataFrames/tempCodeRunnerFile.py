import pandas as pd

list= [[1, 'Tanmay', '10th', '9588424899'],
    [2, 'Akash', '10th', '9656003624'],
    [3, 'Saksham', '10th', '856326598'],
    [4, 'Yash', '10th', '5566778899'],
    [5, 'Nanadini', '10th', '6677889900']]

df = pd.DataFrame(list, columns=['Roll No', 'Name', 'Class', 'Phone No'])
print(df)