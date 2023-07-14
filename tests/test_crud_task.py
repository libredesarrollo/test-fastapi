import pytest
from pro.schemas import Category

@pytest.fixture
def category() -> Category:
    return Category(
        id=5,
        name="FastAPI Book Launch",
    )

def test_event_name(category: Category) -> None:
    print(category)
    assert category.name == "FastAPI Book Launch"