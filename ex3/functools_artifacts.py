from collections.abc import Callable
from typing import Any
from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    length = len(spells)
    if length == 0:
        return 0

    if operation == "add":
        total = int(reduce(operator.add, spells))
        return total
    if operation == "multiply":
        multi = int(reduce(operator.mul, spells))
        return multi
    if operation == "max":
        maxi = int(reduce(max, spells))
        return maxi
    if operation == "min":
        mini = int(reduce(min, spells))
        return mini
    raise ValueError("Unspecified operation")


def partial_enchanter(
        base_enchantment: Callable
        [..., str]) -> dict[str, Callable[[str], str]]:
    enchanter: dict[str, Callable[[str], str]] = {
        "fire": partial(base_enchantment, power=50, element="fire"),
        "water": partial(base_enchantment, power=50, element="water"),
        "soil": partial(base_enchantment, power=50, element="soil")
    }
    return enchanter


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        value = n
    else:
        value = memoized_fibonacci(n-1) + memoized_fibonacci(n - 2)
    return value


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatcher(spell: Any) -> str:
        return (f"Unknown spell type: {type(spell).__name__}")

    @dispatcher.register(int)
    def damage_spell(number: int) -> str:
        return (f"{number} damage")

    @dispatcher.register(str)
    def enchantment(text: str) -> str:
        return (f"{text}")

    @dispatcher.register(list)
    def multi_cast(data_list: list[Any]) -> str:
        return (f"{len(data_list)} spells")
    return dispatcher


def main() -> None:
    try:
        print("Testing spell reducer...")
        numbers = [40, 17, 23, 5, 15]
        print(f"Sum: {spell_reducer(numbers, 'add')}")
        print(f"Product: {spell_reducer(numbers, 'multiply')}")
        print(f"Max: {spell_reducer(numbers, 'max')}")
        print(f"Min: {spell_reducer(numbers, 'min')}")
        print(f"Sum: {spell_reducer(numbers, 'difference')}")
    except ValueError as e:
        print(f"Error: {e}")
    print()
    print("Testing partial_enchanter...")

    def base_enchantment(power: int, element: str, target: str) -> str:
        return (f"Applied {power} power {element} enchantment to {target}.")
    test = partial_enchanter(base_enchantment)
    print(test["soil"]("Earth Golem"))
    print(test["fire"]("Dragon Shield"))

    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("Testing spell dispatcher...")
    func = spell_dispatcher()
    print(f"Damage spell: {func(100)}")
    print(f"Enchantment: {func('fireball')}")
    print(f"Multi-cast: {func([77, 42, 1907])}")
    print(func({"ecol": 42}))


if __name__ == "__main__":
    main()
