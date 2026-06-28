from notifications.telegram_sender import TelegramSender


def test_sender_creation():

    sender = TelegramSender()

    assert sender is not None