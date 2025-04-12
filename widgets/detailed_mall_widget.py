from options.num import OptionsNum
from utils import parse_shoppingmall_data
import textwrap


from utils import parse_shoppingmall_data
from textual.widget import Widget
from textual.widgets import Button, TextArea, DataTable, Log, Input
from textual.app import ComposeResult
from textual.containers import Container
from textual import events, on
import widgets.home_widget as hw


class DetailedMall(Widget):
    can_focus = True
   
    def __init__(self):
        super().__init__()
        self.df = parse_shoppingmall_data()
        self.opt_disabled = False
        self.regions = ["North", "South", "East", "West", "Central"]

    def on_mount(self):
        self.focus()
    
    def compose(self) -> ComposeResult:
        with Container(id="output-list"):
            yield TextArea("Select the region of the mall you want to view", id="list-text", read_only=True)

        with Container(id="opt-list"):
            for o, region in enumerate(self.regions,1):
                btn = Button(f"{o}. {region}", id=f"region-{o}", classes="region-opt", variant="primary")
                yield btn

    def on_key(self, event: events.Key) -> None:
        key = event.key
        if not self.opt_disabled:
          
            if key.isdecimal():
                button = int(key)
                if (button in range(1, len(self.regions) + 1)):
                    btn =self.query_one(f"#region-{button}", Button)
                    btn.press()
        else:
            if key.isdecimal() and int(key) == 1:
                tn =self.query_one(f"#list-back", Button)
                tn.press()
            elif key.isdecimal() and int(key) == 2:
                tn =self.query_one(f"#list-home", Button)
                tn.press()
        event.stop()
       
   
    def disable_all_option(self) -> None:
        for btn in self.query(".region-opt").results():
            btn.disabled = True
        self.opt_disabled = True

    def mount_malls(self, loc:str):
        m = self.df[self.df["Region"] == loc].reset_index()
        container = self.query_one("#output-list")
        container.remove_children()
        dt = DataTable()
        dt.add_columns(*["Index", f"{loc} Malls"])
        dt.add_rows(list(m[["Mall"]][1:].itertuples(index=True, name=None)))
        self.disable_all_option()
        container.mount(dt)

        opt = self.query_one("#opt-list")
        opt.remove_children()
        opt.mount(Input(id="mall_id", placeholder="Enter index of mall to view", type="integer"))
        # opt.mount(Button("1. Back", id="list-back", variant="primary"))
        # opt.mount(Button("2. Home", id="list-home", variant="primary"))

    @on(Button.Pressed, "#list-back")
    def back_press(self):
        b = self.app.query_one("#body", Container)
        b.remove_children()
        b.mount(DetailedMall())
        
    
    @on(Button.Pressed, "#list-home")
    def home_press(self):
        b = self.app.query_one("#body", Container)
        b.remove_children()
        b.mount(hw.HomeWidget())


    @on(Button.Pressed, "#region-1")
    def option_pressed(self):
        loc = 'North'
        self.mount_malls(loc)

    @on(Button.Pressed, "#region-2")
    def option_pressed_2(self):
        loc = 'South'
        self.mount_malls(loc)

    @on(Button.Pressed, "#region-3")
    def option_pressed_3(self):
        loc = 'East'
        self.mount_malls(loc)

    @on(Button.Pressed, "#region-4")
    def option_pressed_4(self):
        loc = 'West'
        self.mount_malls(loc)

    @on(Button.Pressed, "#region-5")
    def option_pressed_5(self):
        loc = 'Central'
        self.mount_malls(loc)


            
        # if loc is not None:
        #     s = f"{loc} Malls"
        #     print(s)
        #     print("-"*len(s))
        #     g = df[df["Region"] == loc].reset_index()
        #     for idx, row in g.iterrows():
        #         print(f"{idx+1:<20} {row['Mall']}")
        #     inp = input("Enter mall to choose: ")
        #     try:
        #         inp = int(inp) - 1
        #         print("\n")
        #         m = g.loc[inp]
        #         s = f"Things to do in {m['Mall']}"
        #         print(s)
        #         print("-"*len(s))
        #         print(f"Nearest MRT {m['MRT']}\n")
        #         print(f"Expenditure:{m['Expenditure']}\n")
        #         print(f"Traffic {m['Traffic']}")
        #         print("-"*len(s))
        #         print(f'1. {m['ThingsToDo1']}\n')
        #         print(f'2. {m['ThingsToDo2']}\n')
        #         print(f'3. {m['ThingsToDo3']}')
        #         print("-"*len(s))
        #         print("Author's review\n")
        #         review = textwrap.fill(m["Review"], width=100)
        #         print(f"{review}\n")
        #         print(f"Rating: {m["Rating"]}\n")

