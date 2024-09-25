import os
import sys  # Make sure to import sys for sys.argv
from pystyle import Colors, Colorate
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

# Set the title of the console window
os.system("title Nebula Logs")
os.system("cls")

def btp(t):
    print(Colorate.Diagonal(Colors.blue_to_purple, t))

def pr(txt):
    print(Colorate.Diagonal(Colors.red_to_blue, f"[LOGS]: {txt}"))

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        try:
            self.browser = QWebEngineView()
            self.browser.setUrl(QUrl("https://www.google.com"))  # Set initial URL with QUrl

            self.setCentralWidget(self.browser)
            self.setWindowTitle("Nebula - Browser")

            # Create navigation toolbar
            nav_bar = QToolBar()
            self.addToolBar(nav_bar)

            # Back button
            back_btn = QAction("Back", self)
            back_btn.triggered.connect(self.browser.back)
            nav_bar.addAction(back_btn)

            # Forward button
            forward_btn = QAction("Forward", self)
            forward_btn.triggered.connect(self.browser.forward)
            nav_bar.addAction(forward_btn)

            # Reload button
            reload_btn = QAction("Reload", self)
            reload_btn.triggered.connect(self.browser.reload)
            nav_bar.addAction(reload_btn)

            # Address bar
            self.url_bar = QLineEdit()
            self.url_bar.returnPressed.connect(self.navigate_to_url)
            nav_bar.addWidget(self.url_bar)

            # Update the address bar when the URL changes
            self.browser.urlChanged.connect(self.update_url_bar)

            # Show the window
            self.show()

        except Exception as e:
            pr(f"Error initializing the browser: {e}")

    def navigate_to_url(self):
        try:
            url = self.url_bar.text()
            if not url.startswith("http://") and not url.startswith("https://"):
                url = "http://" + url
            self.browser.setUrl(QUrl(url))  # Set URL with QUrl
        except Exception as e:
            pr(f"Error navigating to URL: {e}")

    def update_url_bar(self, q):
        try:
            self.url_bar.setText(q.toString())
        except Exception as e:
            pr(f"Error updating URL bar: {e}")

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        window = Browser()
        sys.exit(app.exec_())
    except Exception as e:
        pr(f"Error running the application: {e}")
