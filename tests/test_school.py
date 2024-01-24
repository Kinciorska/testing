import pytest
from source.school import *


def test_classroom_fixture(transfiguration_class):
    assert transfiguration_class.students == []


def test_add_student(transfiguration_class, harry_potter):
    new_student = harry_potter
    transfiguration_class.add_student(new_student)
    assert new_student in transfiguration_class.students


def test_add_too_many_students(transfiguration_class, hermione_granger):
    new_students = hermione_granger
    with pytest.raises(TooManyStudents):
        for student_number in range(11):
            transfiguration_class.add_student(new_students)
