from applications.api.exceptions import BaseServiceException, PermissionDeniedException
from applications.api.permissions import is_manager, is_admin
from applications.events.enums import EventParticipantState
from applications.events.models import Event, EventParticipant, EventComment
from applications.users.models import User


def create_event_participant(event: Event,
                             user: User) -> EventParticipant:
    if EventParticipant.objects.filter(event=event, user=user).exists():
        raise BaseServiceException(
            'Пользователь уже зарегистрирован на мероприятие',
        )
    return EventParticipant.objects.create(
        event=event,
        user=user,
        state=EventParticipantState.REGISTERED,
    )


def update_event_participant(event_participant: EventParticipant,
                             actor: User,
                             state: EventParticipantState) -> EventParticipant:
    moderated_states = (EventParticipantState.ARRIVED, EventParticipantState.SKIPPED)

    if state in moderated_states or event_participant.state in moderated_states:
        can_set_moderated_state = (
                event_participant.event.author == actor or
                event_participant.event.managers.filter(id=actor.id).exists() or
                is_manager(actor)
        )
        if not can_set_moderated_state:
            raise PermissionDeniedException()

    event_participant.state = state
    event_participant.save()
    return event_participant


def create_event_comment(event: Event,
                         actor: User, comment: str) -> EventComment:
    return EventComment.objects.create(
        event=event,
        user=actor,
        comment=comment,
    )


def create_event(actor: User, **kwargs) -> Event:
    if not is_manager(actor) and not is_admin(actor):
        raise PermissionDeniedException()
    return Event.objects.create(
        author=actor,
        name=kwargs.get('name'),
        type=kwargs.get('event_type'),
        place=kwargs.get('place'),
        time_start=kwargs.get('time_start'),
        time_end=kwargs.get('time_end'),
        speaker=kwargs.get('speaker'),
        reference=kwargs.get('reference'),
        reference_video=kwargs.get('reference_video'),
        image=kwargs.get('image'),
        is_online=kwargs.get('is_online'),
        description=kwargs.get('description'),
    )


def update_event(event: Event, actor: User, **kwargs) -> Event:
    if event.author != actor and not is_manager(actor) and not is_admin(actor):
        raise PermissionDeniedException()
    editable_attrs = ['name', 'event_type', 'place', 'time_start', 'time_end', 'speaker',
                      'reference', 'reference_video', 'image', 'is_online', 'description']
    for attr in kwargs:
        if attr in editable_attrs:
            setattr(event, attr, kwargs.get(attr))
    event.save()
    return event


def add_managers(actor: User,
                 event: Event,
                 **kwargs) -> Event:
    if not is_admin(actor):
        raise PermissionDeniedException()
    if not all(is_manager(user) for user in kwargs.get('managers')):
        raise BaseServiceException("Не все пользователи в запросе являются менеджерами")
    for user in kwargs.get('managers'):
        event.managers.add(user)
    event.save()
    return event


def delete_managers(actor: User,
                    event: Event,
                    **kwargs) -> Event:
    if not is_admin(actor):
        raise PermissionDeniedException()
    if not all(is_manager(user) for user in kwargs.get('managers')):
        raise BaseServiceException("Не все пользователи в запросе являются менеджерами")
    for user in kwargs.get('managers'):
        event.managers.remove(user)
    event.save()
    return event
