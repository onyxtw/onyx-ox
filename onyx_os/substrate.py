class SemanticSubstrate:
    """
    The base semantic field where all ONYX operations occur.
    Holds raw semantic values and provides event dispatch.
    """

    def __init__(self):
        self.events = []

    def emit(self, event_type, payload):
        event = {"type": event_type, "payload": payload}
        self.events.append(event)
        return event

    def get_events(self):
        return self.events
