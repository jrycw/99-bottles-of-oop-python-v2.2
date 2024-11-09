from abc import ABC, abstractmethod
from typing import Self


class AbstractBottleNumber(ABC):
    @abstractmethod
    def quantity(self) -> str: ...

    @abstractmethod
    def container(self) -> str: ...

    @abstractmethod
    def action(self) -> str: ...

    @abstractmethod
    def pronoun(self) -> str: ...

    @abstractmethod
    def successor(self) -> str: ...

    @staticmethod
    def from_number(number: int) -> Self:
        match number:
            case 0:
                cls_ = BottleNumber0
            case 1:
                cls_ = BottleNumber1
            case 6:
                cls_ = BottleNumber6
            case _:
                cls_ = BottleNumber
        return cls_(number)


class BottleNumber(AbstractBottleNumber):
    def __init__(self, number: int):
        self._number = number

    def __str__(self) -> str:
        return f"{self.quantity()} {self.container()}"

    def quantity(self) -> str:
        return str(self._number)

    def container(self) -> str:
        return "bottles"

    def action(self) -> str:
        return f"Take {self.pronoun()} down and pass it around"

    def pronoun(self) -> str:
        return "one"

    def successor(self) -> Self:
        return self.from_number(self._number - 1)


class BottleNumber0(BottleNumber):
    def quantity(self) -> str:
        return "no more"

    def action(self) -> str:
        return "Go to the store and buy some more"

    def successor(self) -> Self:
        return self.from_number(99)


class BottleNumber1(BottleNumber):
    def container(self) -> str:
        return "bottle"

    def pronoun(self) -> str:
        return "it"


class BottleNumber6(BottleNumber):
    def quantity(self) -> str:
        return "1"

    def container(self) -> str:
        return "six-pack"


class BottleVerse:
    @classmethod
    def lyrics(cls, number: int) -> str:
        return cls(BottleNumber.from_number(number))._lyrics()

    def __init__(self, bottle_number: BottleNumber):
        self._bottle_number = bottle_number

    def _lyrics(self) -> str:
        return (
            f"{self._bottle_number} of beer on the wall, ".capitalize()
            + f"{self._bottle_number} of beer.\n"
            f"{self._bottle_number.action()}, "
            f"{self._bottle_number.successor()} of beer on the wall.\n"
        )


class CountdownSong:
    def __init__(self, verse_template, max: int = 999999, min: int = 0):
        self._verse_template = verse_template
        self._max = max
        self._min = min

    def song(self) -> str:
        return self.verses(self._max, self._min)

    def verses(self, upper: int, lower: int) -> str:
        return "\n".join(self.verse(i) for i in reversed(range(lower, upper + 1)))

    def verse(self, number) -> str:
        return self._verse_template.lyrics(number)


# def make_bottle_number(number: int) -> BottleNumber:
#     match number:
#         case 0:
#             cls = BottleNumber0
#         case 1:
#             cls = BottleNumber1
#         case 6:
#             cls = BottleNumber6
#         case _:
#             cls = BottleNumber
#     return cls(number)
