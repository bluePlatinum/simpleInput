import simpleInput

class TestClass:

    def test_integer(self):
        simpleInput.input = lambda: 5
        result = simpleInput.sinput("", __builtins__.int, "", 0, 10)
        assert result == 5