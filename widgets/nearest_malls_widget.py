
from utils import get_loc, parse_shoppingmall_data, distance
from textual.widget import Widget
from textual.widget import Widget
from textual.widgets import Button, Label, DataTable, Log
from textual.app import ComposeResult
from textual.containers import Container
from textual import events, on
import widgets.home_widget as hw
import pandas as pd

class NearestMalls(Widget):
    can_focus = True
   
    def __init__(self):
        super().__init__()
        self.df = parse_shoppingmall_data()
        self.opt_disabled = False
        self.malls = self.get_nearest_malls()
    
    def _on_mount(self, event):
        self.focus()
    def get_nearest_malls(self) -> pd.DataFrame:
        loc = get_loc()
        
        lat, long = loc
        shops = parse_shoppingmall_data()
        shops['Distance'] = shops.apply(lambda shop: distance(lat, long, float(shop['LATITUDE']), float(shop['LONGITUDE'])), axis=1)
        return shops.sort_values(by='Distance')

    def compose(self) -> ComposeResult:
        with Container(id="output-list", classes="display-out"):
            if self.malls is None:
                yield Label("Sorry an error occured")
            else:
                dt = DataTable()
                dt.add_columns(*["Mall", "Distance (KM)"])
                dt.add_rows(list(self.malls[['Mall', 'Distance']][1:6].itertuples(index=False, name=None)))
                yield dt

        with Container(id="opt-list", classes="menu"):
            yield Button(f"1. Home", id ="list-home", variant="primary")

           
    def on_key(self, event: events.Key) -> None:
        key = event.key
        if key.isdecimal() and int(key) == 1:
            tn =self.query_one(f"#list-home", Button)
            tn.press()
       
       

    @on(Button.Pressed, "#list-home")
    def home_press(self):
        b = self.app.query_one("#body", Container)
        b.remove_children()
        b.mount(hw.HomeWidget())



