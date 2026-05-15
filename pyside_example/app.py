import logging
import sys

from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow

logger = logging.getLogger(__name__)


def run() -> None:
    logging_config()
    logger.info("Starting")

    app = QApplication(sys.argv)
    app.aboutToQuit.connect(on_shutdown)

    try:
        main_wnd = MainWindow()
    except Exception:
        logger.exception("Failed to start")  # автоматично додає traceback
        raise

    main_wnd.show()
    sys.exit(app.exec())  # блокуючий, код після цього рядка вже не виконається


def on_shutdown() -> None:
    logger.info("Shutdown")


def logging_config(level=logging.DEBUG):
    root_logger = logging.getLogger()
    root_logger.setLevel(level)

    if root_logger.hasHandlers():
        root_logger.handlers.clear()

    date_format: str = '%Y-%m-%d %H:%M:%S'
    log_format: str = '%(asctime)s [%(levelname)s] %(name)s[%(funcName)s]: %(message)s'
    formatter = logging.Formatter(log_format, date_format)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)

    # err_log_handler: logging.FileHandler = RotatingFileHandler("logs/error.log", maxBytes=1_000_000, backupCount=3)
    # err_log_handler.setLevel(logging.ERROR)
    # err_log_handler.setFormatter(formatter)
    # root_logger.addHandler(err_log_handler)
    #
    # debug_log_handler: logging.FileHandler = RotatingFileHandler("logs/debug.log", maxBytes=1_000_000, backupCount=3)
    # debug_log_handler.setLevel(logging.DEBUG)
    # debug_log_handler.setFormatter(formatter)
    # root_logger.addHandler(debug_log_handler)


if __name__ == '__main__':
    run()
