from applications.users.models import User


def is_admin(user: User) -> bool:
    return user.groups.filter(name='Администраторы').exists()


def is_manager(user: User) -> bool:
    return user.groups.filter(name='Менеджеры').exists()
