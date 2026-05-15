import logging

from controllers.main_window_controller import MainWindowController
from ui.base_window import BaseWindow

logger = logging.getLogger(__name__)

from PySide6.QtWidgets import QPushButton, QLineEdit, QLabel


class MainWindow(BaseWindow):
    UI_PATH = "main_window.ui"

    """
    Конкретне головне вікно програми.
    Всі посилання на елементи UI йдуть через self._ui.<widget_name>.
    """

    def __init__(self):
        super().__init__(self.UI_PATH)

        self._controller = MainWindowController()

    # ------------------------------------------------------------------
    # BaseWindow extension points
    # ------------------------------------------------------------------

    def _setup_ui(self) -> None:
        """Початкове налаштування стану віджетів."""
        self.submit_btn: QPushButton = self._find_widget(QPushButton, "submitButton")
        self.input_field: QLineEdit = self._find_widget(QLineEdit, "inputField")
        self.status_label: QLabel = self._find_widget(QLabel, "statusLabel")

    def _connect_signals(self) -> None:
        """Підключення сигналів до слотів."""
        self.submit_btn.clicked.connect(self._on_submit)

    # ------------------------------------------------------------------
    # Slots / handlers
    # ------------------------------------------------------------------

    # handler — у вікні, але делегує контролеру
    def _on_submit(self):
        logger.debug('')

        text = self.input_field.text()
        result = self._controller.process_input(text)
        self.status_label.setText(result)
