from pathlib import Path

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMainWindow, QWidget

ROOT = Path(__file__).parent.parent
UI_DIR = ROOT / 'resources/ui'


class BaseWindow(QMainWindow):
    """
    Базовий клас вікна, який завантажує .ui файл і вбудовує його як центральний віджет.
    Дочірні класи передають шлях до свого .ui файлу через конструктор.
    """

    def __init__(self, ui_path: str | Path, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self._ui_path = Path(UI_DIR / ui_path)
        self._ui: QWidget = self._load_ui(self._ui_path)

        self.setCentralWidget(self._ui)
        self.setWindowTitle(self._ui.windowTitle())
        self.resize(self._ui.size())

        self._setup_ui()
        self._connect_signals()

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _load_ui(path: Path) -> QWidget:
        if not path.exists():
            raise FileNotFoundError(f"UI file not found: {path}")

        ui_file = QFile(str(path))
        if not ui_file.open(QFile.OpenModeFlag.ReadOnly):
            raise RuntimeError(f"Cannot open UI file: {path}")

        loader = QUiLoader()
        widget = loader.load(ui_file)
        ui_file.close()

        if widget is None:
            raise RuntimeError(
                f"QUiLoader failed to load: {path}\n{loader.errorString()}"
            )

        return widget

    def _find_widget[T](self, widget_type: type[T], name: str) -> T:
        widget = self._ui.findChild(widget_type, name)
        if widget is None:
            raise RuntimeError(f"Widget '{name}' not found in UI")
        return widget

    # ------------------------------------------------------------------
    # Extension points for subclasses
    # ------------------------------------------------------------------

    def _setup_ui(self) -> None:
        """
        Викликається після завантаження UI.
        Перевизначте для початкового налаштування віджетів.
        """

    def _connect_signals(self) -> None:
        """
        Викликається після _setup_ui.
        Перевизначте для підключення сигналів і слотів.
        """
