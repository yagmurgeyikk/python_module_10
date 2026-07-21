from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combiner(target: str, power: int):
        result_one = spell1(target, power)
        result_two = spell2(target, power)
        return (result_one, result_two)
    return combiner


def power_amplifier(base_spell: Callable, multiplier) -> Callable:
    def power(target: str, power: int):
        result = power * multiplier
        result_end = base_spell(target, result)
        return result_end
    return power


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(target: str, power: int):
        result = condition(target, power)
        if result is True:
            return spell(target, power)
        else:
            return ("Spell fizzled")
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int):
        result_list = []
        for elements in spells:
            result_list.append(elements(target, power))
        return result_list
    return sequence


def main() -> None:
    print("Testing spell combiner...")

    def fireball(target, power):
        return (f"Fireball hits {target}")

    def heal(target, power):
        return (f"Heals {target}")

    func = spell_combiner(fireball, heal)
    result = func("Dragon", 5)
    print("Combined spell result: ", end="")
    print(result)

    print("Testing power amplifier...")

    def amplified(target, power):
        return (f"{power}")
    func = power_amplifier(amplified, 5)
    power = 6
    result = func("Dragon", power)
    print(f"Original: {power}, Amplified: {result}")

    print("Testing conditional caster...")

    def selection(target, power):
        if power >= 50 and power < 100:
            return True
        else:
            return False

    def spell(target, power):
        return ("Mission Completed")

    func = conditional_caster(selection, spell)
    result = func("Dragon", 23)
    print(result)

    print("Testing spell sequence...")
    func = spell_sequence([fireball, heal])
    result = func("Dragon", 57)
    print(result)


if __name__ == "__main__":
    main()
