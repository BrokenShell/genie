#!python3
#distutils: language = c++


cdef extern from "genie.hpp":
    int _generate_integer "generate_integer"(int, int)
    double _generate_float "generate_float"(double, double)


def random_integer(low: int, high: int) -> int:
    return _generate_integer(low, high)


def random_float(low: float, high: float) -> float:
    return _generate_float(low, high)
