def spell_combiner(spell1, spell2):
    def combiner(target, power):
        result_one = spell1(target, power)
        result_two = spell2(target, power)
        return (result_one, result_two)
    return combiner


def power_amplifier(base_spell, multiplier):
    def power(target, power):
        result = power * multiplier
        result_end = base_spell(target, result)
        return result_end
    return power


def conditional_caster(condition, spell):
    def conditional(target, power):
        result = condition(target, power)
        if result is True:
            return spell(target, power)
        else:
            return ("Spell fizzled")
    return conditional


def spell_sequence(spells):
    def sequence(target, power):
        result_list = []
        for elements in spells:
            result_list.append(elements(target, power))
        return result_list
    return sequence
