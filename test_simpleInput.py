import simpleInput


class TestClass:
    def test_integer(self):
        simpleInput.input = lambda: 5
        result = simpleInput.sinput("", __builtins__.int, "", 0, 10)
        assert type(result) == __builtins__.int
        assert result == 5

    def test_float(self):
        simpleInput.input = lambda: 3.1
        result = simpleInput.sinput("", __builtins__.float, "", 0, 5)
        assert type(result) == __builtins__.float
        assert result == 3.1
