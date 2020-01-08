import simpleInput
import builtins


class TestClass:
    def test_integer(self):
        simpleInput.input = lambda x: 5
        result = simpleInput.sinput("", builtins.int, "", 0, 10)
        assert type(result) == builtins.int
        assert result == 5

    def test_float(self):
        simpleInput.input = lambda x: 3.1
        result = simpleInput.sinput("", builtins.float, "", 0, 5)
        assert type(result) == builtins.float
        assert result == 3.1

    def test_string(self):
        simpleInput.input = lambda x: "hello"
        result = simpleInput.sinput("", builtins.str, "")
        assert type(result) == builtins.str
        assert result == "hello"