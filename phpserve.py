from PyQt5.QtWidgets import QApplication, QMainWindow, QGroupBox, QLabel, QLineEdit, QPushButton, QRadioButton, QScrollArea, QWidget, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt
import sys
import subprocess
import psutil

class LaravelServer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LARAVEL PROJECT SERVER")
        self.setGeometry(100, 100, 640, 499)
        self.setFont(self.font())
        self.centralwidget = QWidget(self)
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(100, 20, 681, 41)
        self.label.setFont(self.font())
        self.setFixedSize(self.size())  # Set fixed window size
        self.label.setText("LARAVEL PROJECT SERVER")

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(20, 60, 601, 171)
        self.groupBox.setFont(self.font())
        self.groupBox.setTitle("")

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setGeometry(30, 20, 211, 16)
        self.label_2.setText("Choose Laravel Folder :")

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(260, 20, 161, 21)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setGeometry(430, 10, 111, 41)
        self.pushButton.setFont(self.font())
        self.pushButton.setText("Browse Folder")
        self.pushButton.clicked.connect(self.browse_folder)

        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setGeometry(40, 70, 95, 20)
        self.radioButton.setChecked(False)
        self.radioButton.setText("Active")

        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(140, 70, 111, 20)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setText("Inactive")

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(252, 120, 131, 28)
        self.pushButton_2.setFont(self.font())
        self.pushButton_2.setStyleSheet("border: 1px solid black; background-color: #00994d;")
        self.pushButton_2.setText("Start Server")
        self.pushButton_2.clicked.connect(self.start_server)

        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(390, 120, 131, 28)
        self.pushButton_3.setFont(self.font())
        self.pushButton_3.setStyleSheet("border: 1px solid black; background-color: #ff3333;")
        self.pushButton_3.setText("Stop Server")
        self.pushButton_3.clicked.connect(self.stop_server)
        self.pushButton_3.setEnabled(False)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(20, 270, 591, 161)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(0, 0, 589, 159)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setGeometry(30, 250, 111, 16)
        self.label_3.setText("TERMINAL")

        self.label_status = QLabel(self.centralwidget)
        self.label_status.setGeometry(30, 290, 550, 100)
        self.label_status.setAlignment(Qt.AlignTop)
        self.label_status.setStyleSheet("font-family: Courier New; font-size: 10pt")
        self.label_status.setWordWrap(True)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setGeometry(510, 440, 101, 21)
        self.label_4.setFont(self.font())
        self.label_4.setText("ⓒ SnYpe")

        self.statusbar = self.statusBar()

        self.setCentralWidget(self.centralwidget)

        self.process = None

    def browse_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        self.lineEdit.setText(folder_path)

    def start_server(self):
        folder_path = self.lineEdit.text()
        if folder_path:
            if self.process and self.process.poll() is None:
                QMessageBox.warning(self, "Server Already Running", "The server is already running.")
                return

            cmd = "php artisan serve"
            self.process = subprocess.Popen(
                cmd,
                cwd=folder_path,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True
            )
            self.pushButton_2.setEnabled(False)
            self.pushButton_3.setEnabled(True)
            self.radioButton.setChecked(True)
            self.radioButton_2.setChecked(False)
            self.label_status.setText("<font color='green'>Server started.</font>")
        else:
            self.label_status.setText("Please choose a folder first.")

    def stop_server(self):
        if self.process and self.process.poll() is None:
            process_id = self.process.pid
            process = psutil.Process(process_id)
            for child in process.children(recursive=True):
                child.kill()
            process.kill()
            self.process.wait()  # Wait for the process to terminate
            self.process = None
            self.pushButton_2.setEnabled(True)
            self.pushButton_3.setEnabled(False)
            self.radioButton.setChecked(False)
            self.radioButton_2.setChecked(True)
            self.label_status.setText("<font color='red'>Server stopped.</font>")
        else:
            QMessageBox.warning(self, "Server Not Running", "The server is not running.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LaravelServer()
    window.show()
    sys.exit(app.exec_())
