


window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        script_js_fun: function (button) {
            console.log('Script Client Side Callback!')
            return "Script Client Side Callback!";
        }
    }
});

