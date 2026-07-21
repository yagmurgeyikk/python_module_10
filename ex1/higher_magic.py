from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combiner(target, power):
        result_one = spell1(target, power)
        result_two = spell2(target, power)
        return (result_one, result_two)
    return combiner


def power_amplifier(base_spell: Callable, multiplier) -> Callable:
    def power(target, power):
        result = power * multiplier
        result_end = base_spell(target, result)
        return result_end
    return power


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(target, power):
        result = condition(target, power)
        if result is True:
            return spell(target, power)
        else:
            return ("Spell fizzled")
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target, power):
        result_list = []
        for elements in spells:
            result_list.append(elements(target, power))
        return result_list
    return sequence


def main() -> None:
    print("Testing spell combiner...")

    def fireball():
        print("Fireball hits Dragon, ", end="")

    def heal():
        print("Heals Dragon")

    print("Combined spell result: ", end="")
    print(f"{spell_combiner(fireball(), heal())}")


if __name__ == "__main__":
    main()
