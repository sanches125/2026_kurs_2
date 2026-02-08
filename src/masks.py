def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты"""

    card_number_masked = card_number[0:6] + "******" + card_number[12:16]  # Используя срезы получаем результат
    card_number_masked_formated = (
        card_number_masked[0:4]
        + " "
        + card_number_masked[4:8]
        + " "
        + card_number_masked[8:12]
        + " "
        + card_number_masked[12:16]
    )

    return card_number_masked_formated


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер счета"""

    account_masked = "**" + account_number[-4:]  # Используя срезы получаем результат

    return account_masked
