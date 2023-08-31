from dash import Dash, html, Input, Output, clientside_callback, ClientsideFunction

app = Dash(__name__)

app.layout = html.Div([
    html.Button(
        id='inline-button', children='Inline Callback', n_clicks=0
    ),
    html.Button(
        id='script-button', children='Script Callback', n_clicks=0
    ),
    html.Div(
        id = 'text',
        children='...'
    )    
])


clientside_callback(
    """
    function(button) {
        console.log('Inline Client Side Callback!')
        return 'Inline Client Side Callback.'
    }
    """,
    Output('text', 'children', allow_duplicate=True),
    Input('inline-button', 'n_clicks'),
    prevent_initial_call = True
)


clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='script_js_fun'
    ),
    Output('text', 'children', allow_duplicate=True),
    Input('script-button', 'n_clicks'),
    prevent_initial_call = True
)


if __name__ == '__main__':
    app.run(debug=True)

