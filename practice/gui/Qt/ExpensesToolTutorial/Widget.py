from PySide6.QtCharts import QChart, QPieSeries, QChartView
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QWidget, QTableWidget, QHBoxLayout, QHeaderView, QTableWidgetItem, QPushButton, \
    QVBoxLayout, QLabel, QLineEdit, QApplication


class Widget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.item_count = 0

        # Example data
        self._data = {"Water": 24.5, "Electricity": 55.1, "Rent": 850.0,
                      "Supermarket": 230.4, "Internet": 29.99, "Bars": 21.85,
                      "Public transportation": 60.0, "Coffee": 22.45, "Restaurants": 120}

        # Left
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Description", "Price"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Chart
        self.chart_view = QChartView()
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        # Right
        self.description = QLineEdit()
        self.price = QLineEdit()
        self.add = QPushButton("Add")
        self.clear = QPushButton("Clear")
        self.quit = QPushButton("Quit")
        self.plot = QPushButton("Plot")

        # Disabling 'Add' button
        self.add.setEnabled(False)

        self.right = QVBoxLayout()
        self.right.addWidget(QLabel("Description"))
        self.right.addWidget(self.description)
        self.right.addWidget(QLabel("Price"))
        self.right.addWidget(self.price)
        self.right.addWidget(self.add)
        self.right.addWidget(self.plot)
        self.right.addWidget(self.chart_view)
        self.right.addWidget(self.clear)
        self.right.addWidget(self.quit)

        # QWidget Layout
        self.layout = QHBoxLayout()

        #self.table_view.setSizePolicy(size)
        self.layout.addWidget(self.table)
        self.layout.addLayout(self.right)

        # Set the layout to the QWidget
        self.setLayout(self.layout)

        # Signals and Slots
        self.add.clicked.connect(self.add_element)
        self.quit.clicked.connect(self.quit_application)
        self.plot.clicked.connect(self.plot_data)
        self.clear.clicked.connect(self.clear_table)
        self.description.textChanged[str].connect(self.check_disable)
        self.price.textChanged[str].connect(self.check_disable)

        # Fill example data
        self.fill_table()

    @Slot()
    def add_element(self):
        des = self.description.text()
        price = self.price.text()

        try:
            price_item = QTableWidgetItem(f"{float(price):.2f}")
            price_item.setTextAlignment(Qt.AlignRight)

            self.table.insertRow(self.item_count)
            description_item = QTableWidgetItem(des)

            self.table.setItem(self.item_count, 0, description_item)
            self.table.setItem(self.item_count, 1, price_item)

            self.description.setText("")
            self.price.setText("")

            self.item_count += 1
        except ValueError:
            print("Wrong price", price)


    @Slot()
    def check_disable(self, s):
        if not self.description.text() or not self.price.text():
            self.add.setEnabled(False)
        else:
            self.add.setEnabled(True)

    @Slot()
    def plot_data(self):
        # Get table information
        series = QPieSeries()
        for i in range(self.table.rowCount()):
            text = self.table.item(i, 0).text()
            number = float(self.table.item(i, 1).text())
            series.append(text, number)

        chart = QChart()
        chart.addSeries(series)
        chart.legend().setAlignment(Qt.AlignLeft)
        self.chart_view.setChart(chart)

    @Slot()
    def quit_application(self):
        QApplication.quit()

    def fill_table(self, data=None):
        data = self._data if not data else data
        for desc, price in data.items():
            description_item = QTableWidgetItem(desc)
            price_item = QTableWidgetItem(f"{price:.2f}")
            price_item.setTextAlignment(Qt.AlignRight)
            self.table.insertRow(self.item_count)
            self.table.setItem(self.item_count, 0, description_item)
            self.table.setItem(self.item_count, 1, price_item)
            self.item_count += 1

    @Slot()
    def clear_table(self):
        self.table.setRowCount(0)
        self.item_count = 0
