from dash import Dash, html, dcc, Input, Output, State, ALL
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.SKETCHY])

most_used = (8, 10, 16)
name_matches = [
    {"label": "Двоичная (2)", "field": 2},
    {"label": "Восьмеричная (8)", "field": 8},
    {"label": "Десятичная (10)", "field": 10},
    {"label": "Шестнадцатеричная (16)", "field": 16},
] + [{"label": f"{value}-ная", "field": value} for value in range(3, 37) if value not in most_used]


def get_dropdown(is_from):
    def pick_id(flag):
        return "from-input" if flag else "out-input"
    return [
        dbc.DropdownMenuItem("Основные", header=True), 
        dbc.DropdownMenuItem("Двоичная (2)", id={"type": pick_id(is_from), "id": "input 2"}),
        dbc.DropdownMenuItem("Восьмеричная (8)", id={"type": pick_id(is_from), "id": "input 8"}),
        dbc.DropdownMenuItem("Десятичная (10)", id={"type": pick_id(is_from), "id": "input 10"}),
        dbc.DropdownMenuItem("Шестнадцатеричная (16)", id={"type": pick_id(is_from), "id": "input 16"}),
        dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem("Другие", header=True),
            ] + [dbc.DropdownMenuItem(f"{value}-ная", id={"type": pick_id(is_from), "id": f"input {value}"}) 
                 for value in range(3, 37) if value not in most_used]

app.layout = dbc.Container([
    dcc.Store(id="store"),
    html.H1(children="Онлайн калькулятор систем счисления", className='my-4 text-center'),
    dbc.Row([
        dbc.Col([
            html.H3("Из системы счисления:"),
            dbc.DropdownMenu(get_dropdown(True), label="Выберите систему счисления", id="input-from")
        ], class_name='py-4 col-lg-4 col-12'),
        dbc.Col([
            html.H3("Перевести указанное число:"),
            dbc.Input(id="input", type="text", placeholder="Значение для перевода"),
        ], class_name='py-4 col-lg-4 col-12'),
        dbc.Col([
            html.H3("В систему счисления:"),
            dbc.DropdownMenu(get_dropdown(False), label="Выберите систему счисления", id="input-to")
        ], class_name='py-4 col-lg-4 col-12')
    ]),
    dbc.Row(
        dbc.Col(dbc.Button(children="Рассчитать", id="calculate", class_name='d-block w-100'), class_name='col-lg-3 col-12'),
        justify="center"
    ),
    dbc.Row([
        dbc.Col(id="result")
    ], class_name='my-4 text-center border')
])

def set_new_data(id, n_clicks, data):
    if data is None:
        data = {
            "picked_from": {
                "data": None,
                "n_clicks": [None] * len(name_matches)
            },
            "picked_to": {
                "data": None,
                "n_clicks": [None] * len(name_matches)
            }
        }
    for index, item in enumerate(n_clicks):
        if data[id]["n_clicks"][index] != item:
            data[id]["n_clicks"] = n_clicks
            data[id]["data"] = name_matches[index]["field"] 
            return data, name_matches[index]["label"]


# It seems that better use dcc.Dropdown, but i want better visual!
@app.callback(
    Output("store", "data", allow_duplicate=True),
    Output("input-from", "label"),
    Input({"type": "from-input", "id": ALL}, "n_clicks"),
    State("store", "data"),
    prevent_initial_call=True
)
def set_from(n_clicks, data):
    return set_new_data("picked_from", n_clicks, data)

@app.callback(
    Output("store", "data", allow_duplicate=True),
    Output("input-to", "label"),
    Input({"type": "out-input", "id": ALL}, "n_clicks"),
    State("store", "data"),
    prevent_initial_call=True
)
def set_to(n_clicks, data):
    return set_new_data("picked_to", n_clicks, data)

@app.callback(
    Output("result", "children"),
    Input("calculate", "n_clicks"),
    State("store", "data"),
    State("input", "value"),
    prevent_initial_call=True
)
def show_result(n_clicks, data, value):
    if n_clicks:
        if data is None:
            return html.H3("Не указана никакая информация!", className="my-3")
        _from = data["picked_from"].get("data")
        _to = data["picked_to"].get("data")
        if not is_value_in_x(value, _from):
            return html.H3(f"Указано число \"{value}\", которое не относится к выбранной системе счисления.", className="my-3")
        if "-" in value:
            return html.H3("Нельзя указывать отрицательные числа!", className="my-3")
        if is_equal_zero(value):
            return get_correct_layout(_from, _to, value, 0)
        if _from and _to and int(value) > 0:
            return get_correct_layout(_from, _to, value, translate(_from, _to, value))
        return html.H3("Не указаны системы счисления!", className="my-3")

def from_x_to_10(value: str, x: int):
    """
    Преобразует число из x системы счисления в 10-ричную
    """
    result = 0
    for i, char in enumerate(str(value)[::-1]):
        if char.isdigit():
            result += int(char) * (x ** i)
        else:
            result += (ord(char) - ord('A') + 10) * (x ** i)
    return result

def from_10_to_x(value: int, x: int):
    """
    Преобразует число из 10-ричной системы счисления в x систему счисления
    """
    result = ""
    while value > 0:
        digit = value % x
        if digit > 9:
            result = chr(ord('A') + digit - 10) + result
        else:
            result = str(digit) + result
        value //= x
    return result

def translate(_from: int, to: int, value: str):
    to_10 = from_x_to_10(value, _from)
    return from_10_to_x(int(to_10), to)

def is_value_in_x(value: str, x: int) -> bool:
    """
    Проверяет, относится ли число к x-системе счисления
    """
    try:
        int(str(value), x)
        return True
    except ValueError:
        return False

def is_equal_zero(x: str):
    return int(x) == 0

def get_correct_layout(_from: int, _to: int, value: str, calc_value: int):
    return html.Div([
        html.H3("Результат:", className="fs-2"),
        html.Div([
            html.B(remove_zeros(value)),
            html.Sub(_from),
            html.Span(" = "),
            html.B(calc_value),
            html.Sub(_to)
        ]),             
    ], className="my-3")

def remove_zeros(value: str):
    value = value.lstrip('0')
    if not value:
        return '0'
    return value

if __name__ == '__main__':
    app.run(port=8055, debug=True)