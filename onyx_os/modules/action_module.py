from onyx_os.operator import SemanticOperator

class ActionModule(SemanticOperator):
    def on_event(self, event):
        if event["type"] == "reasoning":
            return {"action_strength": 1.0}
