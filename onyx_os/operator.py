class SemanticOperator:
    """
    Base operator class for ONYX-OS.
    Modules extend this to react to semantic events.
    """

    def on_event(self, event):
        return None
