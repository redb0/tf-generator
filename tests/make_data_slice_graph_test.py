import pytest

# тестируемый метод make_data
from graph.slice_graph import CanvasSliceGraph


# expression = ["x1", "x2", "0", "-4", "3", "(x1+1)*1.5"]
expression = ["x1", "x2", "0", "-4", "3"]


@pytest.fixture(params=expression)
def expression_loop(request):
    return request.param


def mock_func(point):
    if point[0] == point[1]:
        return point[0]
    else:
        return 1


class TestMakeData:
    def setup(self):
        print("Подготовка окружения")
        self.obj = CanvasSliceGraph()
        self.constraints = [-6, 6]

    def teardown(self):
        pass

    def test_make_data(self, expression_loop):
        x, y = self.obj.make_data(self.constraints, self.constraints, mock_func, expression_loop)
        print(x)
        print(y)
        if expression_loop in ["x1", "x2"]:
            for i in range(len(y)):
                assert y[i] == x[i]
        elif expression_loop in ["0", "-4", "3"]:
            expected = [1. for _ in range(len(y))]
            for i in range(len(y)):
                assert y[i] == expected[i]
