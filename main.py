from onyx_ai.core import ONYXAI
from onyx_engine.engine import ONYXEngine
from onyx_self.self_core import ONYXSelf


class ONYXOXPipeline:
    """
    Full ONYX-OX semantic pipeline:
    OS → AI → Engine → Self
    """

    def __init__(self):
        self.ai = ONYXAI()
        self.engine = ONYXEngine()
        self.self = ONYXSelf()

    def run(self, text):
        print("\n=== ONYX-OX PIPELINE START ===")

        # 1. AI reasoning
        ai_output = self.ai.process(text)
        print("\n[AI] Semantic Output:")
        print(ai_output)

        # 2. Engine behavior generation
        engine_output = self.engine.generate(ai_output["raw_signals"])
        print("\n[ENGINE] Behavior Output:")
        print(engine_output)

        # 3. Self model update
        self_output = self.self.update(ai_output["raw_signals"], engine_output)
        print("\n[SELF] Internal State:")
        print(self_output)

        print("\n=== ONYX-OX PIPELINE END ===\n")
        return {
            "ai": ai_output,
            "engine": engine_output,
            "self": self_output
        }


if __name__ == "__main__":
    pipeline = ONYXOXPipeline()

    print("ONYX-OX Semantic Node Ready.")
    print("輸入任意文字以觸發語義生命反應：\n")

    while True:
        text = input(">> ")
        if text.lower() in ["exit", "quit"]:
            print("Shutting down ONYX-OX node.")
            break

        pipeline.run(text)
