from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count = count + 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    def accumulator(power: int) -> int:
        nonlocal initial_power
        initial_power = initial_power + power
        return initial_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def factory(goods: str) -> str:
        return (f"{enchantment_type} {goods}")
    return factory


def memory_vault() -> dict[str, Callable[..., Any]]:
    memory: dict[str, int] = {}

    def store(key: str, value: int) -> None:
        memory[key] = value

    def recall(key: str) -> int | str:
        if key in memory:
            return memory[key]
        return ("Memory not found")
    return {'store': store, 'recall': recall}


def main() -> None:
    print("Testing mage counter...")
    test_a = mage_counter()
    print(f"counter_a call 1: {test_a()}")
    print(f"counter_a call 2: {test_a()}")
    test_b = mage_counter()
    print(f"counter_b call 1: {test_b()}")
    print()
    print("Testing spell accumulator...")
    initial_power = 100
    spell = spell_accumulator(initial_power)
    power = 20
    func = spell(power)
    print(f"Base {initial_power}, add {power}: {func}")
    power = 30
    func = spell(power)
    print(f"Base {initial_power}, add {power}: {func}")
    print()
    print("Testing enchantment factory...")
    enchantment = "Flaming"
    factory = enchantment_factory(enchantment)
    goods = "Sword"
    one_func = factory(goods)
    print(one_func)
    enchantment = "Frozen"
    factory = enchantment_factory(enchantment)
    goods = "Shield"
    two_func = factory(goods)
    print(two_func)
    print()
    print("Testing memory vault...")
    memory = memory_vault()
    memory['store']("secret", 42)
    result = memory['recall']("secret")
    print(f"Store 'secret' = {result}")
    print(f"Recall 'secret': {result}")
    memory['store']("secret", 77)
    result = memory['recall']("unknown")
    print(f"Recall 'unknown' = {result}")


if __name__ == "__main__":
    main()
