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
        def wrap(power: int):
            if power >= min_power:
                return func()
            else:
                return ("Insufficient power for this spell")
        return wrap
    return validator


def retry_spell(max_attempts: int) -> Callable:
    def retry():
        counter = 1
        while counter <= max_attempts:
            try:
                int("abc")
            except Exception:
                print(f"Spell failed, retrying... "
                      f"(attempt {counter}/{max_attempts})")
            counter = counter + 1
        return "Spell casting failed after max_attempts attempts"
    return retry


class MageGuild:
    def validate_mage_name(name: str) -> bool:
        pass

    def cast_spell(self, spell_name: str, power: int) -> str:
        pass


def main():
    @spell_timer
    def fireball():
        time.sleep(3)
        return ("Fireball cast!")
    print("Testing spell timer...")
    result = fireball()
    print(f"Result: {result}")

    def func():
        return ("power is higher than the specified number")
    print("Testing power validator...")
    res = power_validator(54)
    result = res(func)
    print(result(23))

    print("Testing retry_spell")
    res = retry_spell(3)
    result = res()
    print(result)





if __name__ == "__main__":
    main()
