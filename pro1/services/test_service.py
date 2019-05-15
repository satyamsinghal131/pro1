from ..managers.test_manager import TestManager

test_manager = TestManager()

class TestService(object):
    @staticmethod
    def create_test(name):
        test_manager.create(name)

    @staticmethod
    def filter_by_name(name):
        resp = []
        tests = test_manager.filter_by_name(name)
        for test in tests:
            resp.append({"id": test.id, "name": test.name})

        return resp

    @staticmethod
    def get_all():
        resp = []
        tests = test_manager.get_all()
        for test in tests:
            resp.append({"id": test.id, "name": test.name})

        return resp