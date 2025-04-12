
from options.num import OptionsNum

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Log, TextArea
import widgets.detailed_mall_widget as tdm
from textual import events, on
from textual.css.query import NoMatches
from widgets.list_shopping_mall_widget import ListShoppingMall
from widgets.home_widget import HomeWidget


class ShoppingApp(App):
    
    CSS_PATH = "theme.tcss"

    def compose(self) -> ComposeResult:
        with Container(id="body"):
           yield HomeWidget()
           
if __name__ == "__main__":
    ShoppingApp().run(inline=True)