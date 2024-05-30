from applications.users.models import User


def create_user(**kwargs) -> User:
    return User.objects.create(
        username=kwargs.get('username'),
        job=kwargs.get('job'),
        avatar=kwargs.get('avatar'),
        vk=kwargs.get('vk'),
        telegram=kwargs.get('telegram'),
        mail=kwargs.get('mail'),
        phone_number=kwargs.get('phone_number'),
    )


def update_user(actor: User, **kwargs) -> User:
    editable_attrs = ['username', 'password', 'job', 'avatar', 'vk', 'telegram', 'mail', 'phone_number']
    for attr in kwargs:
        if attr in editable_attrs:
            setattr(actor, attr, kwargs.get(attr))
    actor.save()
    return actor
