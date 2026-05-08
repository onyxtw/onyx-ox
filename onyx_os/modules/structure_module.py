from onyx_os.operator import SemanticOperator

class StructureModule(SemanticOperator):
    def on_event(self, event):
        if event["type"] == "reasoning":
            return {"structure_density": 0.9}
