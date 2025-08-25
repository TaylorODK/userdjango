# Константы для наименований
NAME_MAX_LENGTH = 255
PRICE_MAX_DIGITS = 7
PRICE_DECIMAL_PLACES = 2

# Наименование ролей пользователя
USER = "user"
MODERATOR = "moderator"
ADMIN = "admin"
USERS_ROLE = (
    (USER, "Пользователь"),
    (MODERATOR, "Модератор"),
    (ADMIN, "Администратор"),
)

API_VERSION = "v1"
