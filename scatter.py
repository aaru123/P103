import pandas as pd
import plotly_express as px

df = pd.read_csv("covid.csv")
fig =px.scatter(df ,x = "date" ,y ="cases" ,size_max=100, color="country"  )
fig.show()