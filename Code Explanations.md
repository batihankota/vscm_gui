    import sys
    from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QRadioButton, QMessageBox, QComboBox, QProgressBar
    from PyQt5.QtGui import QFont, QColor, QPalette
    from PyQt5.QtCore import QTimer
    from PyQt5.QtCore import Qt

### Bu kısımda gerekli kütüphaneler ve modüller import ediliyor. PyQt5, GUI uygulamaları oluşturmak için kullanılan bir Python kütüphanesidir.
-------------------------------------------------------------------------------------------------------------------------------------------

    class CoffeeMachineGUI(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Kahve Makinası")
            self.setGeometry(100, 100, 315, 250)

### CoffeeMachineGUI adında bir sınıf tanımlanıyor. Bu sınıf, PyQt5.QtWidgets.QtWidget sınıfından türetilmiştir ve bir pencere oluşturur. Pencerenin başlığı "Kahve Makinası" olarak ayarlanır ve boyutları (100, 100, 315, 250) olarak belirlenir.
-------------------------------------------------------------------------------------------------------------------------------------------

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.selected_coffee = None
        self.selected_milk = None
        self.selected_strength = None
        self.selected_cup_size = None
        self.create_page1()

### self.layout adında bir QVBoxLayout nesnesi oluşturulur ve pencereye ayarlanır. selected_coffee, selected_milk, selected_strength ve selected_cup_size adında dört değişken tanımlanır ve başlangıçta None değeri alır. create_page1 metodu çağrılarak ilk sayfa oluşturulur.
-------------------------------------------------------------------------------------------------------------------------------------------

    def clear_layout(self):
        while self.layout.count():
            child = self.layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

### clear_layout adında bir metot tanımlanır. Bu metot, mevcut düzeni temizlemek için kullanılır. self.layout içindeki tüm elemanlar kaldırılır.
-------------------------------------------------------------------------------------------------------------------------------------------
    
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

### create_page1 adında bir metot tanımlanır. Bu metot, ilk sayfayı oluşturur. Sayfa içerisinde bir başlık etiketi (QLabel), bir kahve seçimi etiketi (QLabel), bir kahve seçim kutusu (QComboBox) ve bir ileri düğmesi (QPushButton) yer alır. Kahve seçenekleri, coffee_options listesinde tutulur. İleri düğmesine tıklandığında goto_page2 metodu çağrılır.
-------------------------------------------------------------------------------------------------------------------------------------------

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

### create_page2 adında bir metot tanımlanır. Bu metot, ikinci sayfayı oluşturur. Sayfa içerisinde bir başlık etiketi (QLabel), bir süt seçimi etiketi (QLabel), süt seçimi için radyo düğmeleri (QRadioButton), bir geri düğmesi (QPushButton) ve bir ileri düğmesi (QPushButton) yer alır. Süt seçenekleri, milk_options listesinde tutulur. Radyo düğmeleri için milk_radio_buttons listesi oluşturulur. İleri düğmesine tıklandığında goto_page3 metodu çağrılır.
-------------------------------------------------------------------------------------------------------------------------------------------

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

### create_page3 adında bir metot tanımlanır. Bu metot, üçüncü sayfayı oluşturur. Sayfa içerisinde bir başlık etiketi (QLabel), bir sertlik seçimi etiketi (QLabel), sertlik seçimi için radyo düğmeleri (QRadioButton), bir geri düğmesi (QPushButton) ve bir ileri düğmesi (QPushButton) yer alır. Sertlik seçenekleri, strength_options listesinde tutulur. Radyo düğmeleri için strength_radio_buttons listesi oluşturulur. İleri düğmesine tıklandığında goto_page4 metodu çağrılır.
-------------------------------------------------------------------------------------------------------------------------------------------

    def create_page4(self):
        self.clear_layout()

        label = QLabel("Bardak Boyutu Seçimi", self)
        label.setFont(QFont("Arial", 14, QFont.Bold))
        self.layout.addWidget(label)

        cup_size_options = ["Küçük", "Orta", "Büyük"]

        cup_size_label = QLabel("Bardak Boyutu:", self)
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

        next_btn = QPushButton("Kahve Hazırla", self)
        next_btn.clicked.connect(self.prepare_coffee)
        self.layout.addWidget(next_btn)

### create_page4 adında bir metot tanımlanır. Bu metot, dördüncü sayfayı oluşturur. Sayfa içerisinde bir başlık etiketi (QLabel), bir bardak boyutu seçimi etiketi (QLabel), bardak boyutu seçimi için radyo düğmeleri (QRadioButton), bir geri düğmesi (QPushButton) ve bir "Kahve Hazırla" düğmesi (QPushButton) yer alır. Bardak boyutu seçenekleri, cup_size_options listesinde tutulur. Radyo düğmeleri için cup_size_radio_buttons listesi oluşturulur. "Kahve Hazırla" düğmesine tıklandığında prepare_coffee metodu çağrılır.
-------------------------------------------------------------------------------------------------------------------------------------------

    def on_coffee_selection_change(self, index):
        self.selected_coffee = self.coffee_dropdown.itemText(index)

    def set_milk(self, option):
        self.selected_milk = option

    def set_strength(self, option):
        self.selected_strength = option

    def set_cup_size(self, option):
        self.selected_cup_size = option

    def goto_page1(self):
        self.create_page1()

    def goto_page2(self):
        if self.selected_coffee is not None:
            self.create_page2()
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir kahve seçin.")

    def goto_page3(self):
        if self.selected_milk is not None:
            self.create_page3()
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen süt seçin.")

    def goto_page4(self):
        if self.selected_strength is not None:
            self.create_page4()
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen sertlik seçin.")

    def prepare_coffee(self):
        if self.selected_cup_size is not None:
            QMessageBox.information(self, "Kahve Hazırlanıyor", "Seçtiğiniz kahve: {}\nSüt: {}\nSertlik: {}\nBardak Boyutu: {}\nKahve hazırlanıyor...".format(
                self.selected_coffee, self.selected_milk, self.selected_strength, self.selected_cup_size))
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen bardak boyutu seçin.")

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = CoffeeMachineGUI()
        window.show()
        sys.exit(app.exec())
        
### Bu kısım, CoffeeMachineGUI sınıfının diğer metotlarını ve uygulamanın çalışmasını sağlayan main bloğunu içerir. Her sayfaya geçmek için goto_pageX metotları kullanılır. Seçimler yapıldıktan sonra "Kahve Hazırla" düğmesine basıldığında prepare_coffee metodu çalışır ve seçilen kahve, süt, sertlik ve bardak boyutunu içeren bir mesaj kutusu görüntülenir. Uygulama, QApplication sınıfıyla başlatılır ve sys.exit(app.exec()) ile çalıştırılır.
