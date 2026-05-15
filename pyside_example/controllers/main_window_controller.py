import logging

logger = logging.getLogger(__name__)


class MainWindowController:
    @staticmethod
    def process_input(text: str) -> str:
        logger.debug(f'{text = }')

        if not text.strip():
            return "Порожній ввід"
        return f"Оброблено: {text.upper()}"
