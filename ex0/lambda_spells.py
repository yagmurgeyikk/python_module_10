def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sorter = sorted(artifacts, key=lambda elements: elements['power'],
                    reverse=True)
    return sorter


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    powers = list(filter(lambda elements: elements['power'] >= min_power,
                         mages))
    return powers


def spell_transformer(spells: list[str]) -> list[str]:
    spell = list(map(lambda elements: f"* {elements} *", spells))
    return spell


def mage_stats(mages: list[dict]) -> dict:
    maxi = max(mages, key=lambda elements: elements['power'])['power']
    mini = min(mages, key=lambda elements: elements['power'])['power']
    summ = sum(map(lambda elements: elements['power'], mages))
    length = len(mages)
    avg = round(summ / length, 2)

    return {
        'max_power': maxi,
        'min_power': mini,
        'avg_power': avg
    }


def main() -> None:
    print("Testing artifact sorter...")
    artifact = [{'name': "Fire Staff", 'power': 92},
                {'name': "Crystal Orb", 'power': 85}]

    data_dict = artifact_sorter(artifact)

    print(f"{data_dict[0]['name']} ({data_dict[0]['power']} power) comes "
          f"before {data_dict[1]['name']} ({data_dict[1]['power']} power)")
    print()
    print("Testing spell transformer...")
    spell = ["fireball", "heal", "shield"]
    spell_list = spell_transformer(spell)
    print(spell_list)
    print()
    print("Testing power filter...")
    power = [{'name': "Fire Staff", 'power': 92},
             {'name': "Crystal Orb", 'power': 85},
             {'name': "Dua Lipa", 'power': 98}]
    power_list = power_filter(power, 86)
    print(power_list)
    print()
    print("Testing mage stats...")
    mage = [{'name': "Fire Staff", 'power': 92},
            {'name': "Crystal Orb", 'power': 85},
            {'name': "Dua Lipa", 'power': 98}]

    mage_dict = mage_stats(mage)
    print(mage_dict)


if __name__ == "__main__":
    main()
