import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QFileDialog, QMessageBox, QListWidget, QListWidgetItem,
)
from PyQt5.QtCore import QSize
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
from PIL import Image


class ImageToHeaderConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.selected_folder = None
        self.screen_width = 135 
        self.screen_height = 240 

        self.pushButton.clicked.connect(self.select_folder)
        self.pushButton_2.clicked.connect(self.convert_images)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 300)
        Form.setMaximumSize(QtCore.QSize(700, 300))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        Form.setFont(font)

        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(339, 9, 351, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(
            "border: 2px black; border-style: none none solid none; border-radius: 6px; height: 20px; background-color: grey; color: white;"
        )
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)

        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setStyleSheet("border: none; border-left: 2px solid black;")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setStyleSheet("border: none; border-left: 2px solid black;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setStyleSheet("border: none; border-left: 2px solid black;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)

        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(
            "border: 2px black; border-style: none none solid none; border-radius: 6px; height: 20px; background-color: grey; color: white;"
        )
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)

        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)

        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet(
            "QProgressBar {\n"
            "    border: 2px solid black;\n"
            "    border-radius: 5px;\n"
            "    background-color: grey;\n"
            "    color: white;\n"
            "    text-align: center;\n"
            "}\n"
            "\n"
            "QProgressBar::chunk {\n"
            "    background-color: white;\n"
            "    width: 5px;\n"
            "    margin: 0.5px;\n"
            "}\n"
        )
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)

        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setStyleSheet("color: rgba(0,0,0,0.2);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)

        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 311, 281))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 309, 279))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.listWidget = QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 291, 281))
        self.listWidget.setViewMode(QListWidget.IconMode)
        self.listWidget.setIconSize(QSize(100, 100))
        self.listWidget.setSpacing(10)
        self.listWidget.setObjectName("listWidget")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Image to Header Converter"))
        self.label.setText(_translate("Form", "Folder: "))
        self.pushButton.setText(_translate("Form", "Select Folder"))
        self.label_2.setText(_translate("Form", "Input your screen size"))
        self.label_3.setText(_translate("Form", "Width: "))
        self.lineEdit.setPlaceholderText(_translate("Form", "Ex. 100"))
        self.label_4.setText(_translate("Form", "Height: "))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Ex. 200"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Name output"))
        self.pushButton_2.setText(_translate("Form", "Convert"))
        self.label_6.setText(_translate("Form", "Progress"))
        self.label_5.setText(_translate("Form", "Made By: framecodev"))

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.selected_folder = folder
            self.label.setText(f"Folder: {folder}")
            self.list_images(folder)

    def list_images(self, folder):
        self.listWidget.clear()

        for filename in os.listdir(folder):
            if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):
                file_path = os.path.join(folder, filename)
                pixmap = QPixmap(file_path)
                icon = QIcon(pixmap)
                item = QListWidgetItem(icon, filename)
                self.listWidget.addItem(item)

    def process_image(self, image_path):
        img = Image.open(image_path)
        img = img.convert("RGB")
        img.thumbnail((self.screen_width, self.screen_height))

        frame_data = []

        for y in range(img.height):
            row = []
            for x in range(img.width):
                r, g, b = img.getpixel((x, y))
                rgb565 = ((r >> 3) << 11) | ((g >> 2) << 5) | (b >> 3)
                row.append(rgb565)
            frame_data.append(row)

        return img.width, img.height, frame_data

    def convert_images(self):
        if not self.selected_folder:
            QMessageBox.warning(self, "Error", "Please select a folder first.")
            return
        try:
            self.screen_width = int(self.lineEdit.text().strip())
            self.screen_height = int(self.lineEdit_2.text().strip())
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter valid width and height values.")
            return

        output_name = self.lineEdit_3.text().strip()
        if not output_name:
            QMessageBox.warning(self, "Error", "Please enter a name for the output header file.")
            return

        output_file = os.path.join(self.selected_folder, f"{output_name}.h")

        try:
            with open(output_file, "w") as header_file:
                header_file.write("#ifndef IMAGES_H\n#define IMAGES_H\n\n")
                header_file.write("#include <stdint.h>\n\n")

                all_frames = []
                image_width, image_height = 0, 0

                for filename in os.listdir(self.selected_folder):
                    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):
                        file_path = os.path.join(self.selected_folder, filename)
                        width, height, frame_data = self.process_image(file_path)

                        image_width = width
                        image_height = height

                        frame_name = os.path.splitext(filename)[0]
                        all_frames.append(frame_name)

                        header_file.write(f"const uint16_t {frame_name}[{width} * {height}] = {{\n")

                        for row in frame_data:
                            row_data = ", ".join(f"0x{pixel:04X}" for pixel in row)
                            header_file.write(f"    {row_data},\n")

                        header_file.write("};\n\n")

                header_file.write(f"const uint16_t IMAGE_WIDTH = {image_width};\n")
                header_file.write(f"const uint16_t IMAGE_HEIGHT = {image_height};\n\n")

                header_file.write("const uint16_t* images[] = {\n")
                header_file.write(",\n".join(f"    {frame}" for frame in all_frames))
                header_file.write("\n};\n\n")

                header_file.write("const uint8_t NUM_IMAGES = sizeof(images) / sizeof(images[0]);\n\n")
                header_file.write("#endif // IMAGES_H\n")

            self.progressBar.setValue(100)
            QMessageBox.information(self, "Success", f"Images converted and saved to {output_file}")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")
            self.progressBar.setValue(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageToHeaderConverter()
    window.show()
    sys.exit(app.exec_())