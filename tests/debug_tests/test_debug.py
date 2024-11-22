import time


class TestDebug:
    def test_debug_proxy(self, request):
        print()
        print(f"START {request.node.name}")

        time.sleep(60)

        print(f"FINISH {request.node.name}")
