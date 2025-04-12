from textual.app import App, ComposeResult
from textual.containers import Container
from widgets.home_widget import HomeWidget


class ShoppingApp(App):
    
    CSS_PATH = "theme.tcss"
    BINDINGS = [("ctrl+q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        with Container(id="body"):
           yield HomeWidget()

           
if __name__ == "__main__":
    ShoppingApp().run(inline=True)