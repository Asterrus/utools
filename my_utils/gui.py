from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Input, Button, Static
# from core import generate_qr  # используем ту же бизнес-логику


class MyUtilsApp(App):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Input(placeholder='Text for QR', type='text')
        yield Button(label='Create QR')

        # self.output = Static("Результат появится здесь")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        print('event.button', event.button)
        # result = generate_qr(text)
        # self.output.update(f"QR-код создан: {result}")
        self.exit(str(event.button))


if __name__ == '__main__':
    app = MyUtilsApp()
    app.run()
