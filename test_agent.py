
from unittest.mock import patch

from tools import search_product, check_price
from agent import execute_tool


def test_search_existing_product():
    result = search_product("Laptop")

    assert isinstance(result, list)
    assert result[0]["id"] == "P001"


def test_p002_price():
    result = check_price("P002")

    assert "15,000 RWF" in result


def test_unknown_product_price():
    result = check_price("P999")

    assert "not found" in result.lower()
    assert "RWF" not in result


def test_tool_exception():
    with patch(
        "agent.search_product",
        side_effect=RuntimeError("Simulated failure")
    ):
        try:
            execute_tool("search_product", {"query": "Laptop"})
            assert False, "Expected the simulated exception"
        except RuntimeError as error:
            assert "Simulated failure" in str(error)


def test_prompt_cannot_invent_unknown_price():
    result = check_price("P999")

    assert "not found" in result.lower()
    assert "999" not in result or "P999" in result

