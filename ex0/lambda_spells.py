def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sorter = sorted(artifacts, key=lambda elements: elements['power'],
                    reverse=True)
    return sorter


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    powers = list(filter(lambda elements: elements['power'] >= min_power,
                         mages))
    return powers


def spell_transformer(spells: list[str]) -> list[str]:
    pass


def mage_stats(mages: list[dict]) -> dict:
    pass
