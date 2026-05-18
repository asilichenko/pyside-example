import logging

from pyside_example.ui import MainWindow

logger = logging.getLogger(__name__)


class MainWindowController:

    def __init__(self, view: MainWindow):
        self._view = view
        self._setup_signals()

    def _setup_signals(self) -> None:
        self._view.submit_requested.connect(self._on_submit)

    def _on_submit(self, text: str) -> None:
        logger.debug(f'{text = }')

        result: str = "Порожній ввід" if not text.strip() else f"Оброблено: {text.upper()}"
        self._view.show_status(result)
