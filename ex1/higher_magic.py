from collections.abc import Callable
from typing import Any


def spell_combiner(
        spell1: Callable[[str, int], Any],
        spell2: Callable[[str, int], Any]) -> Callable[[str, int],
                                                       tuple[Any, Any]]:
    def combiner(target: str, power: int) -> tuple[Any, Any]:
        result_one = spell1(target, power)
        result_two = spell2(target, power)
        return (result_one, result_two)
    return combiner


def power_amplifier(
        base_spell: Callable[[str, int], Any],
        multiplier: int | float) -> Callable[[str, int], Any]:
    def power(target: str, power: int) -> Any:
        result = int(power * multiplier)
        result_end = base_spell(target, result)
        return result_end
    return power


def conditional_caster(
        condition: Callable[[str, int], bool],
        spell: Callable[[str, int], Any]) -> Callable[[str, int], Any]:
    def conditional(target: str, power: int) -> Any:
        result = condition(target, power)
        if result is True:
            return spell(target, power)
        else:
            return ("Spell fizzled")
    return conditional


def spell_sequence(
        spells: list[Callable[[str, int], Any]]) -> Callable[[str, int],
                                                             list[Any]]:
    def sequence(target: str, power: int) -> list[Any]:
        result_list = []
        for elements in spells:
            result_list.append(elements(target, power))
        return result_list
    return sequence


def main() -> None:
    print("Testing spell combiner...")

    def fireball(target: str, power: int) -> str:
        return (f"Fireball hits {target}")

    def heal(target: str, power: int) -> str:
        return (f"Heals {target}")

    func = spell_combiner(fireball, heal)
    result = func("Dragon", 5)
    print("Combined spell result: ", end="")
    print(result)
    print()
    print("Testing power amplifier...")

    def amplified(target: str, power: int) -> str:
        return (f"{power}")
    func = power_amplifier(amplified, 5)
    power = 6
    result = func("Dragon", power)
    print(f"Original: {power}, Amplified: {result}")

    print("Testing conditional caster...")

    def selection(target: str, power: int) -> bool:
        if power >= 50 and power < 100:
            return True
        else:
            return False

    def spell(target: str, power: int) -> str:
        return ("Mission Completed")

    func = conditional_caster(selection, spell)
    result = func("Dragon", 23)
    print(result)
    print()
    print("Testing spell sequence...")
    func_sequence = spell_sequence([fireball, heal])
    result_sequence = func_sequence("Dragon", 57)
    print(result_sequence)


if __name__ == "__main__":
    main()
