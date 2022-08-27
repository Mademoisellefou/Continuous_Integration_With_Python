import uno
class TestUno:
    def test_addition(self):
        assert 4==uno.add_two(2,2)
    def test_subtraction(self):
        assert 0==uno.sub_two(2,2)