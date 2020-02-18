from game.actions.action import MoveAction

class TestMoveAction:
    def test_move_x(self, source):
        move = MoveAction(0, source, 1, 0)
        move.resolve()
        expected = 1
        actual = source.x
        assert actual == expected
    
    def test_move_y(self, source):
        move = MoveAction(0, source, 0, 1)
        move.resolve()
        expected = 1
        actual = source.y
        assert actual == expected
    
    def test_move(self, source):
        move = MoveAction(0, source, 1, 1)
        move.resolve()
        expected_x = 1
        expected_y = 1
        actual_x = source.x
        actual_y = source.y
        assert actual_x == expected_x
        assert actual_y == expected_y
