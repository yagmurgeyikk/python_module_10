from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def counter():
        nonlocal count
        count = count + 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    def accumulator(power: int):
        nonlocal initial_power
        initial_power = initial_power + power
        return initial_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def factory(goods: str):
        return (f"{enchantment_type} {goods}")
    return factory


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: str, value: int):
        memory[key] = value

    def recall(key: str):
        if key in memory:
            return memory[key]
        return ("Memory not found")
    return {'store': store, 'recall': recall}
