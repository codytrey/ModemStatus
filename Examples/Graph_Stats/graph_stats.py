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
        if x[0] == "":
            ds1p.append(0.0)
        else:
            ds1p.append(float(x[0]))
        if x[1] == "":
            ds1s.append(0.0)
        else:
            ds1s.append(float(x[1]))
        if x[2] == "":
            ds2p.append(0.0)
        else:
            ds2p.append(float(x[2]))
        if x[3] == "":
            ds2s.append(0.0)
        else:
            ds2s.append(float(x[3]))
        if x[4] == "":
            ds3p.append(0.0)
        else:
            ds3p.append(float(x[4]))
        if x[5] == "":
            ds3s.append(0.0)
        else:
            ds3s.append(float(x[5]))
        if x[6] == "":
            ds4p.append(0.0)
        else:
            ds4p.append(float(x[6]))
        if x[7] == "":
            ds4s.append(0.0)
        else:
            ds4s.append(float(x[7]))
        if x[8] == "":
            ds5p.append(0.0)
        else:
            ds5p.append(float(x[8]))
        if x[9] == "":
            ds5s.append(0.0)
        else:
            ds5s.append(float(x[9]))
        if x[10] == "":
            ds6p.append(0.0)
        else:
            ds6p.append(float(x[10]))
        if x[11] == "":
            ds6s.append(0.0)
        else:
            ds6s.append(float(x[11]))
        if x[12] == "":
            ds7p.append(0.0)
        else:
            ds7p.append(float(x[12]))
        if x[13] == "":
            ds7s.append(0.0)
        else:
            ds7s.append(float(x[13]))
        if x[14] == "":
            ds8p.append(0.0)
        else:
            ds8p.append(float(x[14]))
        if x[15] == "":
            ds8s.append(0.0)
        else:
            ds8s.append(float(x[15]))
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
    if x[0] == "":
        us1p.append(0.0)
    else:
        us1p.append(float(x[0]))
    if x[1] == "":
        us2p.append(0.0)
    else:
        us2p.append(float(x[1]))
    if x[2] == "":
        us3p.append(0.0)
    else:
        us3p.append(float(x[2]))
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
