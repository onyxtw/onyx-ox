from onyx_os.operator import SemanticOperator

class TransformModule(SemanticOperator):
    def on_event(self, event):
        if event["type"] == "reasoning":
            return {"transform_factor": 1.1}
