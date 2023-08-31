from dash import Dash, html, dcc, Input, Output, callback, ctx


app = Dash(__name__)

app.layout = html.Div(
    [
        dcc.Slider(
            id="slider-circular", min=0, max=20,
            marks={i: str(i) for i in range(21)},
            value=3
        ),
        dcc.Input(
            id="input-circular", type="number", min=0, max=20, value=3
        ),
    ]
)
@callback(
    Output("input-circular", "value"),
    Output("slider-circular", "value"),
    Input("input-circular", "value"),
    Input("slider-circular", "value"),
)
def callback(input_value, slider_value):
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
    value = input_value if trigger_id == "input-circular" else slider_value
    return value, value

if __name__ == '__main__':
    app.run(debug=True)
