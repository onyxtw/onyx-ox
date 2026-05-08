class CivilizationState:
    """
    Tracks the semantic civilization level of the node.
    """

    def __init__(self):
        self.level = "C-0"

    def update(self, new_level):
        self.level = new_level
        return self.level
