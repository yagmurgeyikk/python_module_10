def spell_combiner(spell1, spell2):
    def combiner(target, power):
        result_one = spell1(target, power)
        result_two = spell2(target, power)
        return (result_one, result_two)
    return combiner


def power_amplifier(base_spell, multiplier):
    def power(target, power):
        result = power * multiplier
        result_end = base_spell(result)
        return result_end
    return power


def conditional_caster(condition, spell):
    pass
