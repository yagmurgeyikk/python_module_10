from collections.abc import Callable
import time
from functools import wraps


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrap(number: int):
        name = func.__name__
        print(f"Casting {name}")
        start = time.time()
        result = func(number)
        end = time.time()
        func_time = end - start
        print(f"Spell completed in {func_time:.3f} seconds")
        return result
    return wrap


def power_validator(min_power: int) -> Callable:
    @wraps(min_power)
    def wrap(power: int):
        if power >= min_power:
            return wrap
        else:
            return ("Insufficient power for this spell")
    return power_validator
# sonra bak


def retry_spell(max_attempts: int) -> Callable:
    i = 0
    for i in max_attempts:
        try:
            return ("Hello")
        except Exception:
            print(f"Spell failed, retrying... (attempt {i}/{max_attempts}")
    return retry_spell
# sonra düzelt


class MageGuild:
    def validate_mage_name(name: str) -> bool:
        pass

    def cast_spell(self, spell_name: str, power: int) -> str:
        pass


def main():
    def fireball(number: int):
        time.sleep(3)
        return (f"Fireball cast! {number}")
    print("Testing spell timer...")
    result_timer = spell_timer(fireball)
    result = result_timer(34)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
