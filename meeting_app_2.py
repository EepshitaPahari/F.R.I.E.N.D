import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage


class CustomWebEnginePage(QWebEnginePage):
    def __init__(self, parent=None):
        super().__init__(parent)

    def featurePermissionRequested(self, origin, feature):
        # Show a popup dialog to ask the user for permission
        feature_name = ""
        if feature == QWebEnginePage.MediaAudioCapture:
            feature_name = "microphone"
        elif feature == QWebEnginePage.MediaVideoCapture:
            feature_name = "camera"

        if feature_name:
            # Create a permission dialog
            user_response = QMessageBox.question(
                None,
                "Permission Request",
                f"The website at {origin} wants to access your {feature_name}. Allow?",
                QMessageBox.Yes | QMessageBox.No,
            )

            # Grant or deny permission based on user response
            if user_response == QMessageBox.Yes:
                self.setFeaturePermission(origin, feature, QWebEnginePage.PermissionGrantedByUser)
            else:
                self.setFeaturePermission(origin, feature, QWebEnginePage.PermissionDeniedByUser)


class JitsiApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jitsi Meet Embedded App")
        self.setGeometry(100, 100, 1024, 768)

        # Create the central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create a QWebEngineView and set a custom WebEnginePage
        self.web_view = QWebEngineView()
        self.web_page = CustomWebEnginePage()
        self.web_view.setPage(self.web_page)

        # Load the Jitsi Meet URL
        jitsi_url = "https://meet.jit.si/Pi#userInfo.displayName=%22Pi%22"
        self.web_view.setUrl(QUrl(jitsi_url))

        # Add the web view to the layout
        layout.addWidget(self.web_view)


def video_call():
    app = QApplication(sys.argv)
    main_window = JitsiApp()
    main_window.show()
    app.exec_()
