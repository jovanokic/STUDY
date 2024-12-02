import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPlainTextEdit

def set_theme_colors(widget, background, text):
    style = f"background-color: {background}; color: {text};"
    widget.setStyleSheet(style)

def main():
    app = QApplication(sys.argv)

    # Create the main window
    window = QWidget()
    window.setWindowTitle("PyCharm Theme Color Tester")

    # Create a text editor to display the theme colors
    text_editor = QPlainTextEdit()
    text_editor.setReadOnly(True)

    # Create a layout and add the text editor to it
    layout = QVBoxLayout()
    layout.addWidget(text_editor)

    # Set the initial theme colors
    set_theme_colors(window, "#1E1E1E", "#FFFFFF")
    set_theme_colors(text_editor, "#1E1E1E", "#FFFFFF")

    # Update the text editor with the current theme colors
    def update_text_editor():
        background_color = window.palette().color(window.backgroundRole()).name()
        text_color = text_editor.palette().color(text_editor.foregroundRole()).name()
        text_editor.setPlainText(f"Background Color: {background_color}\nText Color: {text_color}")

    # Change the theme colors when the window is clicked
    def change_theme_colors():
        # Define your desired theme colors here
        background_color = "#FF0000"  # Red
        text_color = "#0000FF"  # Blue

        set_theme_colors(window, background_color, text_color)
        set_theme_colors(text_editor, background_color, text_color)
        update_text_editor()

    window.clicked.connect(change_theme_colors)

    # Update the text editor with the initial theme colors
    update_text_editor()

    # Set the layout for the main window
    window.setLayout(layout)
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
