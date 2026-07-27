from collections.abc import Callable
import time
from functools import wraps


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrap():
        name = func.__name__
        print(f"Casting {name}")
        start = time.time()
        result = func()
        end = time.time()
        func_time = end - start
        print(f"Spell completed in {func_time:.3f} seconds")
        return result
    return wrap


def power_validator(min_power: int) -> Callable:
    def validator(func) -> Callable:
        @wraps(func)
        def wrap(self, spell_name, power: int):
            if power >= min_power:
                return func(self, spell_name, power)
            else:
                return ("Insufficient power for this spell")
        return wrap
    return validator


def retry_spell(max_attempts: int) -> Callable:
    def retry(func: Callable) -> Callable:
        @wraps(func)
        def wrap():
            counter = 1
            while counter <= max_attempts:
                try:
                    return func()
                except Exception:
                    print(f"Spell failed, retrying... "
                          f"(attempt {counter}/{max_attempts})")
                counter = counter + 1
            return "Spell casting failed after max_attempts attempts"
        return wrap
    return retry


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        length = len(name)
        if length <= 3:
            return False
        if not name.isalpha() and name.strip():
            return False
        return True

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return (f"Successfully cast {spell_name} with <{power}> power")


def main():
    @spell_timer
    def fireball():
        time.sleep(3)
        return ("Fireball cast!")
    print("Testing spell timer...")
    result = fireball()
    print(f"Result: {result}")
    print()
    print("Testing retrying spell...")

    def func():
        int("abc")
    res = retry_spell(3)(func)
    result = res()
    print(result)
    print()
    print("Testing MageGuild...")
    obj = MageGuild()
    res_one = obj.validate_mage_name("yagmur")
    res_two = obj.validate_mage_name("yg")
    print(res_one)
    print(res_two)
    res_three = obj.cast_spell("Lightning", 15)
    res_four = obj.cast_spell("Lightning", 7)
    print(res_three)
    print(res_four)


if __name__ == "__main__":
    main()
