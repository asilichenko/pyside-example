import logging

from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow

logger = logging.getLogger(__name__)


class PySide6Example:

    def run(self):
        app = QApplication([])

        try:
            main_wnd = MainWindow()
            main_wnd.show()
        except Exception:
            logger.error("Failed to start")
            raise

        app.exec_()
