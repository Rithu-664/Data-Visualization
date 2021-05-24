import pandas as panda
import plotly.express as px

df = panda.read_csv('.\covidData.csv')

figure = px.scatter(df,x="date",y="cases",color="country",title="Covid cases per day")
figure.show()

