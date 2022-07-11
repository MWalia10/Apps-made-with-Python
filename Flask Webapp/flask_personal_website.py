from flask import Flask, render_template

app = Flask(__name__)

@app.route('/plot/')
def plot():
    from pandas_datareader import data
    import datetime
    from bokeh.plotting import figure, show, output_file
    from bokeh.embed import components
    from bokeh.resources import CDN
    df = data.DataReader(name = "AAPL", data_source = "yahoo", start = datetime.datetime(2021, 10, 10), end = datetime.datetime(2022, 3, 10))
    df.head()
    p = figure(x_axis_type = "datetime", width = 1000, height = 300, sizing_mode = "scale_width")
    p.title = "Candlestick_Chart"
    p.grid.grid_line_alpha = 0.3

    hours_12 = 12*60*60*1000
    mask_inc = df.Close >= df.Open
    mask_dec = df.Close < df.Open
    df["Middle"] = (df.Open + df.Close)/2
    df["Height"] = abs(df.Open - df.Close)

    p.segment(df.index, df.High, df.index, df.Low, color = "black")
    p.rect(df.index[mask_inc], df.Middle[mask_inc], 
           hours_12, df.Height[mask_inc], fill_color = "green", 
           line_color = "black")
    p.rect(df.index[mask_dec], df.Middle[mask_dec], 
           hours_12, df.Height[mask_dec], fill_color = "red", 
           line_color = "black")
    script1, div1 = components(p)
    cdn_js = CDN.js_files[0]
    return render_template('plot.html', script1=script1, div1=div1, cdn_js = cdn_js)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug = True)
