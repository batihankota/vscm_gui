import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QRadioButton, QMessageBox, QComboBox, QProgressBar
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt

class CoffeeMachineGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cofee Machine GUI")
        self.setGeometry(100, 100, 315, 250)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.selected_coffee = None
        self.selected_milk = None
        self.selected_strength = None
        self.selected_cup_size = None

        self.create_page1()

    def clear_layout(self):
        while self.layout.count():
            child = self.layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def create_page1(self):
        self.clear_layout()

        label = QLabel("Kahve Seçimi", self)
        label.setFont(QFont("Arial", 14, QFont.Bold))
        self.layout.addWidget(label)

        coffee_options = ["Lütfen Bir Kahve Seçin", "Americano", "Mocha", "Latte", "Cappuccino", "Filtre Kahve"]

        coffee_label = QLabel("Kahve:", self)
        self.layout.addWidget(coffee_label)

        self.coffee_dropdown = QComboBox(self)
        self.coffee_dropdown.addItems(coffee_options)
        self.coffee_dropdown.setCurrentIndex(0)
        self.coffee_dropdown.currentIndexChanged.connect(self.on_coffee_selection_change)
        self.layout.addWidget(self.coffee_dropdown)

        next_btn = QPushButton("İleri", self)
        next_btn.clicked.connect(self.goto_page2)
        self.layout.addWidget(next_btn)

    def create_page2(self):
        self.clear_layout()

        label = QLabel("Sütlü / Sütsüz / Az Sütlü Seçimi", self)
        label.setFont(QFont("Arial", 14, QFont.Bold))
        self.layout.addWidget(label)

        milk_options = ["Sütlü", "Sütsüz", "Az Sütlü"]

        milk_label = QLabel("Süt:", self)
        self.layout.addWidget(milk_label)

        self.milk_radio_buttons = []

        for option in milk_options:
            radio_btn = QRadioButton(option, self)
            radio_btn.clicked.connect(lambda _, option=option: self.set_milk(option))
            self.layout.addWidget(radio_btn)
            self.milk_radio_buttons.append(radio_btn)

        prev_btn = QPushButton("Geri", self)
        prev_btn.clicked.connect(self.goto_page1)
        self.layout.addWidget(prev_btn)

        next_btn = QPushButton("İleri", self)
        next_btn.clicked.connect(self.goto_page3)
        self.layout.addWidget(next_btn)

    def create_page3(self):
        self.clear_layout()

        label = QLabel("Sertlik Seçimi", self)
        label.setFont(QFont("Arial", 14, QFont.Bold))
        self.layout.addWidget(label)

        strength_options = ["Hafif", "Orta", "Yoğun"]

        strength_label = QLabel("Sertlik:", self)
        self.layout.addWidget(strength_label)

        self.strength_radio_buttons = []

        for option in strength_options:
            radio_btn = QRadioButton(option, self)
            radio_btn.clicked.connect(lambda _, option=option: self.set_strength(option))
            self.layout.addWidget(radio_btn)
            self.strength_radio_buttons.append(radio_btn)

        prev_btn = QPushButton("Geri", self)
        prev_btn.clicked.connect(self.goto_page2)
        self.layout.addWidget(prev_btn)

        next_btn = QPushButton("İleri", self)
        next_btn.clicked.connect(self.goto_page4)
        self.layout.addWidget(next_btn)

    def create_page4(self):
        self.clear_layout()

        label = QLabel("Bardak Boyu Seçimi", self)
        label.setFont(QFont("Arial", 14, QFont.Bold))
        self.layout.addWidget(label)

        cup_size_options = ["Küçük", "Orta", "Büyük"]

        cup_size_label = QLabel("Bardak Boyu:", self)
        self.layout.addWidget(cup_size_label)

        self.cup_size_radio_buttons = []

        for option in cup_size_options:
            radio_btn = QRadioButton(option, self)
            radio_btn.clicked.connect(lambda _, option=option: self.set_cup_size(option))
            self.layout.addWidget(radio_btn)
            self.cup_size_radio_buttons.append(radio_btn)

        prev_btn = QPushButton("Geri", self)
        prev_btn.clicked.connect(self.goto_page3)
        self.layout.addWidget(prev_btn)

        next_btn = QPushButton("Onayla", self)
        next_btn.clicked.connect(self.show_loading_screen)
        self.layout.addWidget(next_btn)

    def goto_page1(self):
        self.create_page1()

    def goto_page2(self):
        if not self.selected_coffee:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir kahve seçin!")
            return
        self.create_page2()

    def goto_page3(self):
        if not self.is_milk_selected():
            QMessageBox.warning(self, "Uyarı", "Lütfen bir süt seçin!")
            return
        self.create_page3()

    def goto_page4(self):
        if not self.is_strength_selected():
            QMessageBox.warning(self, "Uyarı", "Lütfen bir sertlik seçin!")
            return
        self.create_page4()

    def on_coffee_selection_change(self, index):
        self.set_coffee(self.coffee_dropdown.itemText(index))

    def is_milk_selected(self):
        return any(btn.isChecked() for btn in self.milk_radio_buttons)

    def is_strength_selected(self):
        return any(btn.isChecked() for btn in self.strength_radio_buttons)

    def is_cup_size_selected(self):
        return any(btn.isChecked() for btn in self.cup_size_radio_buttons)

    def set_coffee(self, coffee):
        self.selected_coffee = coffee

    def set_milk(self, milk):
        self.selected_milk = milk

    def set_strength(self, strength):
        self.selected_strength = strength

    def set_cup_size(self, cup_size):
        self.selected_cup_size = cup_size

    def show_loading_screen(self):
        if not self.is_cup_size_selected():
            QMessageBox.warning(self, "Uyarı", "Lütfen bir bardak boyu seçin!")
            return

        self.clear_layout()

        label = QLabel("Kahveniz Hazırlanıyor...", self)
        label.setFont(QFont("Arial", 14, QFont.Bold))
        self.layout.addWidget(label)

        selection_label = QLabel(f"Kahve Seçimi: {self.selected_coffee}\n"
                                 f"Süt Seçimi: {self.selected_milk}\n"
                                 f"Sertlik Seçimi: {self.selected_strength}\n"
                                 f"Bardak Boyu Seçimi: {self.selected_cup_size}", self)
        self.layout.addWidget(selection_label)

        progress_bar = QProgressBar(self)
        progress_bar.setMaximum(30)
        

        palette = progress_bar.palette()
        palette.setColor(QPalette.Highlight, QColor(153, 196, 184))  # İlerleme çubuğu rengi
        progress_bar.setPalette(palette)
        progress_bar.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(progress_bar)

        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: self.update_progress(progress_bar))
        self.timer.start(1000)

    def update_progress(self, progress_bar):
        current_value = progress_bar.value()
        if current_value >= progress_bar.maximum():
            self.timer.stop()
            QMessageBox.information(self, "Kahve Hazır", "Afiyet olsun!")
            self.close()
        else:
            progress_bar.setValue(current_value + 1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    coffee_machine = CoffeeMachineGUI()

    # Arka plan rengi
    palette = coffee_machine.palette()
    palette.setColor(coffee_machine.backgroundRole(), QColor(0, 0, 0))
    coffee_machine.setPalette(palette)

    # Metin renkleri
    palette.setColor(coffee_machine.foregroundRole(), QColor(41, 252, 195))
    coffee_machine.setStyleSheet("QPushButton { color: crimson; } QLabel { color: white; } QRadioButton { color: white; } QLabel#page_title { color: white; }"
                                 "QMessageBox { background-color: black; color: white; }")

    coffee_machine.show()
    sys.exit(app.exec_())