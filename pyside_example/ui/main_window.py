import logging

from ui.base_window import BaseWindow

logger = logging.getLogger(__name__)

from PySide6.QtWidgets import QWidget


class MainWindow(BaseWindow):
    UI_FILE = "main_view.ui"

    """
    Конкретне головне вікно програми.
    Всі посилання на елементи UI йдуть через self._ui.<widget_name>.
    """

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(self.UI_FILE, parent)

    # ------------------------------------------------------------------
    # BaseWindow extension points
    # ------------------------------------------------------------------

    def _setup_ui(self) -> None:
        """Початкове налаштування стану віджетів."""
        # Приклад: self._ui.statusBar().showMessage("Ready")
        # Приклад: self._ui.lineEditSearch.setPlaceholderText("Пошук…")

    def _connect_signals(self) -> None:
        """Підключення сигналів до слотів."""
        # Приклад: self._ui.pushButtonOk.clicked.connect(self._on_ok_clicked)
        # Приклад: self._ui.actionExit.triggered.connect(self.close)

    # ------------------------------------------------------------------
    # Slots / handlers
    # ------------------------------------------------------------------

    def _on_ok_clicked(self) -> None:
        """Обробник натискання кнопки OK."""
