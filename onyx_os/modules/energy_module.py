from onyx_os.operator import SemanticOperator

class EnergyModule(SemanticOperator):
    def on_event(self, event):
        if event["type"] == "reasoning":
            return {"energy_flow": 1.5}
