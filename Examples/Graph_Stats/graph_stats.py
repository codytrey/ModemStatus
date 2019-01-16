import plotly
import plotly.graph_objs as go
import sqlite3
import sys
import os
import datetime

if sys.argv[1] is not None:
    conn = sqlite3.connect(sys.argv[1])
else:
    conn = sqlite3.connect(str(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "modem.db")))
c = conn.cursor()
ds1p = []
ds1s = []
ds2p = []
ds2s = []
ds3p = []
ds3s = []
ds4p = []
ds4s = []
ds5p = []
ds5s = []
ds6p = []
ds6s = []
ds7p = []
ds7s = []
ds8p = []
ds8s = []
time = []
for x in c.execute("select * from downstream"):
        try:
            ds1p.append(float(x[0]))
        except ValueError:
            ds1p.append(0.0)
        try:
            ds1s.append(float(x[1]))
        except ValueError:
            ds1s.append(0.0)
        try:
            ds2p.append(float(x[2]))
        except ValueError:
            ds2p.append(0.0)
        try:
            ds2s.append(float(x[3]))
        except ValueError:
            ds2s.append(0.0)
        try:
            ds3p.append(float(x[4]))
        except ValueError:
            ds3p.append(0.0)
        try:
            ds3s.append(float(x[5]))
        except ValueError:
            ds3s.append(0.0)
        try:
            ds4p.append(float(x[6]))
        except ValueError:
            ds4p.append(0.0)
        try:
            ds4s.append(float(x[7]))
        except ValueError:
            ds4s.append(0.0)
        try:
            ds5p.append(float(x[8]))
        except ValueError:
            ds5p.append(0.0)
        try:
            ds5s.append(float(x[9]))
        except ValueError:
            ds5s.append(0.0)
        try:
            ds6p.append(float(x[10]))
        except ValueError:
            ds6p.append(0.0)
        try:
            ds6s.append(float(x[11]))
        except ValueError:
            ds6s.append(0.0)
        try:
            ds7p.append(float(x[12]))
        except ValueError:
            ds7p.append(0.0)
        try:
            ds7s.append(float(x[13]))
        except ValueError:
            ds7s.append(0.0)
        try:
            ds8p.append(float(x[14]))
        except ValueError:
            ds8p.append(0.0)
        try:
            ds8s.append(float(x[15]))
        except ValueError:
            ds8s.append(0.0)
        # time.append(x[16])
        # datetime.datetime.strptime(x[16],'%Y-%m-%d %H:%M:%S')
        # time.append(datetime.datetime.strptime(x[16], '%Y-%m-%d %H:%M:%S'))
        time.append(datetime.datetime.fromtimestamp(x[16]))

ds1p_plot = go.Scatter(
    x=time,
    y=ds1p,
    name='Down Stream 1 Power'
)
ds1s_plot = go.Scatter(
    x=time,
    y=ds1s,
    name='Down Stream 1 Signal to Noise'
)
ds2p_plot = go.Scatter(
    x=time,
    y=ds2p,
    name='Down Stream 2 Power'
)
ds2s_plot = go.Scatter(
    x=time,
    y=ds2s,
    name='Down Stream 2 Signal to Noise'
)
ds3p_plot = go.Scatter(
    x=time,
    y=ds3p,
    name='Down Stream 3 Power'
)
ds3s_plot = go.Scatter(
    x=time,
    y=ds3s,
    name='Down Stream 3 Signal to Noise'
)
ds4p_plot = go.Scatter(
    x=time,
    y=ds4p,
    name='Down Stream 4 Power'
)
ds4s_plot = go.Scatter(
    x=time,
    y=ds4s,
    name='Down Stream 4 Signal to Noise'
)
ds5p_plot = go.Scatter(
    x=time,
    y=ds5p,
    name='Down Stream 5 Power'
)
ds5s_plot = go.Scatter(
    x=time,
    y=ds5s,
    name='Down Stream 5 Signal to Noise'
)
ds6p_plot = go.Scatter(
    x=time,
    y=ds6p,
    name='Down Stream 6 Power'
)
ds6s_plot = go.Scatter(
    x=time,
    y=ds6s,
    name='Down Stream 6 Signal to Noise'
)
ds7p_plot = go.Scatter(
    x=time,
    y=ds7p,
    name='Down Stream 7 Power'
)
ds7s_plot = go.Scatter(
    x=time,
    y=ds7s,
    name='Down Stream 7 Signal to Noise'
)
ds8p_plot = go.Scatter(
    x=time,
    y=ds8p,
    name='Down Stream 8 Power'
)
ds8s_plot = go.Scatter(
    x=time,
    y=ds8s,
    name='Down Stream 8 Signal to Noise'
)

data = [ds1p_plot, ds2p_plot, ds3p_plot, ds4p_plot, ds5p_plot, ds6p_plot, ds7p_plot, ds8p_plot]

plotly.offline.plot({"data": data, "layout": go.Layout(title="Downstream Power Graph")},
                    auto_open=True, filename="Downstream_Power_Graph.html")
data = [ds1s_plot, ds2s_plot, ds3s_plot, ds4s_plot, ds5s_plot, ds6s_plot, ds7s_plot, ds8s_plot]

plotly.offline.plot({"data": data, "layout": go.Layout(title="Downstream Signal to Noise Graph")},
                    auto_open=True, filename="Downstream_SnR_Graph.html")

us1p = []
us2p = []
us3p = []
time = []
for x in c.execute("select * from upstream"):
    try:
        us1p.append(float(x[0]))
    except ValueError:
        us1p.append(0.0)
    try:
        us2p.append(float(x[1]))
    except ValueError:
        us2p.append(0.0)
    try:
        us3p.append(float(x[2]))
    except ValueError:
        us3p.append(0.0)
    time.append(datetime.datetime.fromtimestamp(x[3]))
    # time.append(datetime.datetime.strptime(x[3], '%Y-%m-%d %H:%M:%S'))

us1p_plot = go.Scatter(
    x=time,
    y=us1p,
    name='Upstream Power 1'
)
us2p_plot = go.Scatter(
    x=time,
    y=us2p,
    name='Upstream Power 1'
)
us3p_plot = go.Scatter(
    x=time,
    y=us3p,
    name='Upstream Power 1'
)

data = [us1p_plot, us2p_plot, us3p_plot]

plotly.offline.plot({"data": data, "layout": go.Layout(title="Upstream Graph")},
                    auto_open=True, filename="UpstreamGraph.html")
