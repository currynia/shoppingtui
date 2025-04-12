from utils import parse_shoppingmall_data
from textual.widget import Widget
from textual.widgets import Button, TextArea, DataTable, Log
from textual.app import ComposeResult
from textual.containers import Container
from textual import events, on
import widgets.list_shopping_mall_widget as lsm
import widgets.detailed_mall_widget as dm

class HomeWidget(Widget):
    can_focus = True
    def __init__(self):
        super().__init__()
        option1 = f'List all malls in Singapore.'
        option2 = f'View detailed info about mall.'

        option3 = f'List nearest malls.'

       

        option4 = f'Open Map.'

        option5 = f'Exit.'
        self.opt_disabled = False
        self.options = [option1, option2, option3, option4, option5]

    def on_mount(self):
        self.focus()
    
    def compose(self) -> ComposeResult:
        with Container(id="options"):
            yield TextArea("Select an option", read_only=True)
            for num, opt in enumerate(self.options, 1):
                yield Button(f"{num}. {opt}", id ="opt"+str(num) ,classes="home-opt",variant="primary")
    
    def on_key(self, event: events.Key) -> None:
        if not self.opt_disabled:
            key = event.key
            if key.isdecimal():
                button = int(key)
                if (button in range(1, len(self.options) + 1)):
                    btn =self.query_one(f"#opt{button}", Button)
                    btn.press()
       
   
    def disable_all_option(self) -> None:
        for btn in self.query(".home-opt").results():
            btn.disabled = True
        self.opt_disabled = True

    @on(Button.Pressed, "#opt1")
    def option_pressed(self):
        b = self.app.query_one("#body", Container)
        
        self.disable_all_option()
        b.remove_children()

        b.mount(lsm.ListShoppingMall())

    @on(Button.Pressed, "#opt2")
    def option_pressed_2(self):
        b = self.app.query_one("#body", Container)
        
        self.disable_all_option()
        b.remove_children()

        b.mount(dm.DetailedMall())
       
        
        
        