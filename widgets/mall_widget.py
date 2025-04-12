
from textual.widget import Widget
from textual.widget import Widget
from textual.widgets import Button, Label
from textual.app import ComposeResult
from textual.containers import Container
from textual import events, on
import widgets.home_widget as hw
import pandas
import widgets.detailed_mall_widget as dwm
class Mall(Widget):
    can_focus = True
   
    def __init__(self, data:pandas.DataFrame):
        super().__init__()
        self.df = data

    def on_mount(self):
        self.focus()
    
    def compose(self) -> ComposeResult:
        with Container(id="detailed-mall", classes="display-out"):
            yield Label(f"{self.df["Mall"]}")
            yield Label(f"{self.df["Region"]} Region")
            yield Label(f"Expenditure: {self.df["Expenditure"]}")
            yield Label(f"Nearest MRT: {self.df["MRT"]}")
            yield Label(f"Traffic: {self.df["Traffic"]}")
            yield Label("")
            yield Label(f"Things to do:")
            yield Label(f"1. {self.df["ThingsToDo1"]}")
            yield Label(f"2. {self.df["ThingsToDo2"]}")
            yield Label(f"3. {self.df["ThingsToDo3"]}")
            yield Label("")
            yield Label("Authors review")
            yield Label(f"{self.df["Review"]}", shrink=True)
            yield Label(f"Rating {self.df["Rating"]}")
        with Container(id = "buttons", classes="menu"):
            yield Button(f"1. Back", id = "list_back", variant="primary")
            yield Button(f"2. Home", id ="list_home", variant="primary")

    def on_key(self, event: events.Key) -> None:
        key = event.key
        
        if key.isdecimal() and int(key) == 1:
            tn =self.query_one(f"#list_back", Button)
            tn.press()
        elif key.isdecimal() and int(key) == 2:
            tn =self.query_one(f"#list_home", Button)
            tn.press()
    
    @on(Button.Pressed, "#list_back")
    def back_press(self):
        b = self.app.query_one("#body", Container)
        b.remove_children()
        b.mount(dwm.DetailedMall())
        
    
    @on(Button.Pressed, "#list_home")
    def home_press(self):
        b = self.app.query_one("#body", Container)
        b.remove_children()
        b.mount(hw.HomeWidget())
      
       


    

