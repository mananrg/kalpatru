import plotly
import plotly.graph_objs as go
from flask import Flask, request, redirect, url_for, flash, render_template
import pandas as pd
import numpy as np
import json

def create_plot():


  N = 40
  x = np.linspace(0, 1, N)
  y = np.random.randn(N)
  df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe


  data = [
   go.Bar(
     x=df['x'], # assign x as the dataframe column 'x'
     y=df['y']
  )
          ]

  graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

  return graphJSON

app = Flask(__name__)


@app.route('/')
def index():

        bar = create_plot()
        return render_template('plot_readability.html', plot=bar)


if __name__ == "__main__":
        app.run(host='0.0.0.0',port=6006)

