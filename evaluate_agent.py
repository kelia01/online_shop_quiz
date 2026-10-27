
import json

from deepeval import evaluate
from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric
from deepeval.test_case import LLMTestCase

from agent import agent
from tools import products

cases = [
    {
        "input": "What is the price of P002?",
        "expected": "Wireless Mouse: 15,000 RWF",
    },
    {
        "input": "Find the laptop",
        "expected": "Laptop with 8GB RAM and 256GB SSD",
    },
    {
        "input": "What is the price of P999?",
        "expected": "Product P999 not found",
    },
]

catalogue_context = [
    json.dumps(products, ensure_ascii=False)
]

test_cases = []

for case in cases:
    actual_output = agent(case["input"])

    print("\nInput:", case["input"])
    print("Expected:", case["expected"])
    print("Actual:", actual_output)

    test_cases.append(
        LLMTestCase(
            input=case["input"],
            actual_output=actual_output,
            expected_output=case["expected"],
            retrieval_context=catalogue_context,
        )
    )

metrics = [
    AnswerRelevancyMetric(threshold=0.7),
    FaithfulnessMetric(threshold=0.7),
]

evaluate(test_cases=test_cases, metrics=metrics)
