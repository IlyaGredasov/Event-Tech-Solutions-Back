from applications.api.exceptions import BaseServiceException, PermissionDeniedException
from applications.api.permissions import is_manager
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
