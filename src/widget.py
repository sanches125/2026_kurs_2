from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card_number: str) -> str:
    """Функция, которая определяет счет или карту необходимо замаскмровать и делает это"""

    if "Счет" in account_card_number:  # вызываем из модуля Masks функцию маскирования "Счета"
        masked_account_number = get_mask_account(account_card_number)
        message = masked_account_number
    else:  # вызываем из модуля Masks функцию маскирования "карты"
        masked_card_number = get_mask_card_number(account_card_number)
        message = masked_card_number

    return str(message)
