def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты"""

    card_number_masked = card_number[len(card_number) * -1 : -10] + "******" + card_number[-4:]  # Используем срезы
    card_number_masked_formated = (
        card_number_masked[len(card_number) * -1 : -12]
        + " "
        + card_number_masked[-12:-8]
        + " "
        + card_number_masked[-8:-4]
        + " "
        + card_number_masked[-4:]
    )

    return card_number_masked_formated


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер счета"""

    account_masked = "Счет " + "**" + account_number[-4:]  # Используя срезы получаем результат

    return account_masked
