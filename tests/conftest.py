import pytest

import source.shapes as shapes
import source.school as school


@pytest.fixture
def defined_rectangle():
    return shapes.Rectangle(10, 5)


@pytest.fixture
def another_rectangle():
    return shapes.Rectangle(5, 2)


@pytest.fixture
def transfiguration_class():
    return school.Classroom(teacher="Minerva McGonagall",
                            students=[],
                            course_title="Transfiguration"
                            )


@pytest.fixture
def transfiguration_class_with_students():
    return school.Classroom(teacher="Minerva McGonagall",
                            students=["Harry Potter", "Ron Weasley", "Hermione Granger"],
                            course_title="Transfiguration"
                            )


@pytest.fixture
def harry_potter():
    return school.Student("Harry Potter")


@pytest.fixture
def ron_weasley():
    return school.Student("Ron Weasley")


@pytest.fixture
def hermione_granger():
    return school.Student("Hermione Granger")


@pytest.fixture
def mcgonagall():
    return school.Teacher("Minerva McGonagall")
