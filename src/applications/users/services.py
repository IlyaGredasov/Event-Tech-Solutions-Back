from django.contrib.auth.models import Group

from applications.api.exceptions import PermissionDeniedException, BaseServiceException
from applications.api.permissions import is_admin
from applications.users.models import User


def create_user(**kwargs) -> User:
    new_user = User.objects.create(
        username=kwargs.get('username'),
        first_name=kwargs.get('first_name'),
        last_name=kwargs.get('last_name'),
        job=kwargs.get('job'),
        avatar=kwargs.get('avatar'),
        vk=kwargs.get('vk'),
        telegram=kwargs.get('telegram'),
        mail=kwargs.get('mail'),
        phone_number=kwargs.get('phone_number'),
    )
    new_user.set_password(kwargs.get('password'))
    new_user.save()
    return new_user


def update_user(actor: User, **kwargs) -> User:
    editable_attrs = ['username', 'first_name', 'last_name', 'job', 'avatar', 'vk', 'telegram', 'mail', 'phone_number']
    for attr in kwargs:
        if attr in editable_attrs:
            setattr(actor, attr, kwargs.get(attr))
    if 'password' in kwargs:
        actor.set_password(kwargs.get('password'))
    actor.save()
    return actor


def add_user_groups(actor: User,
                    modifiable_user: User,
                    **kwargs) -> User:
    for group in kwargs.get('groups'):
        print(group)
    if not is_admin(actor):
        raise PermissionDeniedException()
    if not all(Group.objects.filter(name=group).exists() for group in kwargs.get('groups')):
        raise BaseServiceException('Не все группы в запросе существуют')
    for group in kwargs.get('groups'):
        modifiable_user.groups.add(group)
    modifiable_user.save()
    return modifiable_user


def delete_user_groups(actor: User,
                       modifiable_user: User,
                       **kwargs) -> User:
    if not is_admin(actor):
        raise PermissionDeniedException()
    for group in kwargs.get('groups'):
        print(group)
    if not all(Group.objects.filter(name=group).exists() for group in kwargs.get('groups')):
        raise BaseServiceException('Не все группы в запросе существуют')

    for group in kwargs.get('groups'):
        modifiable_user.groups.remove(group)
    modifiable_user.save()
    return modifiable_user
