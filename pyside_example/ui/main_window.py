import logging
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QPushButton, QLineEdit, QLabel, QStatusBar
from ui import BaseWindow

logger = logging.getLogger(__name__)


class MainWindow(BaseWindow):
    """
    Конкретне головне вікно програми.
    Всі посилання на елементи UI йдуть через self._ui.<widget_name>.
    """

    UI_PATH = "main_window.ui"

    submit_requested = Signal(str)  # передає текст поля

    def __init__(self):
        super().__init__(self.UI_PATH)

    # ------------------------------------------------------------------
    # BaseWindow extension points
    # ------------------------------------------------------------------

    def _setup_ui(self) -> None:
        """Початкове налаштування стану віджетів."""
        self.submit_btn: QPushButton = self._find_widget(QPushButton, "submitButton")
        self.input_field: QLineEdit = self._find_widget(QLineEdit, "inputField")
        self.status_label: QLabel = self._find_widget(QLabel, "statusLabel")
        self.statusbar: QStatusBar = self._find_widget(QStatusBar, "statusbar")

    def _connect_signals(self) -> None:
        """Підключення сигналів до слотів."""
        self.submit_btn.clicked.connect(self._on_submit)

    # ------------------------------------------------------------------
    # Slots / handlers
    # ------------------------------------------------------------------

    # handler — у вікні, але делегує контролеру
    def _on_submit(self):
        logger.debug('submit')
        self.submit_requested.emit(self.input_field.text())

    # ------------------------------------------------------------------
    # Public methods
    # ------------------------------------------------------------------

    def show_status(self, text: str) -> None:
        logger.debug(f'{text = }')
        self.status_label.setText(text)
        self.statusbar.showMessage(text)
