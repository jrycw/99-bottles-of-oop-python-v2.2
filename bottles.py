from abc import ABC, abstractmethod


class AbstractBottleNumber(ABC):
    @abstractmethod
    def quantity(self) -> str: ...

    @abstractmethod
    def container(self) -> str: ...

    @abstractmethod
    def action(self) -> str: ...

    @abstractmethod
    def pronoun(self) -> str: ...


class BottleNumber(AbstractBottleNumber):
    def __init__(self, number: int):
        self._number = number

    @property
    def number(self) -> int:
        """
        A public API to get the wrapped number
        """
        return self._number

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


class BottleNumber0(BottleNumber):
    def quantity(self) -> str:
        return "no more"

    def action(self) -> str:
        return "Go to the store and buy some more"


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


class BottleNumberFactory:
    @staticmethod
    def from_number(number: int) -> BottleNumber:
        """
        Make BottleNumber from an integer
        """
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

    @staticmethod
    def create_successor(bottle_number: BottleNumber) -> BottleNumber:
        """
        Create the successor of a BottleNumber-ish class
        """
        wrapped_number = bottle_number.number  # get the wrapped number via the public API
        match wrapped_number:
            case 0:
                successor_number = 99
            case _:
                successor_number = wrapped_number - 1
        return BottleNumberFactory.from_number(successor_number)


class BottleVerse:
    def __init__(self, bottle_number: BottleNumber):
        self._bottle_number = bottle_number

    @property
    def bottle_number(self) -> BottleNumber:
        """
        A public API to get the wrapped BottleNumber
        """
        return self._bottle_number

    @classmethod
    def lyrics(cls, number: int) -> str:
        bottle_number = BottleNumberFactory.from_number(number)
        return cls(bottle_number)._lyrics()

    def _lyrics(self) -> str:
        successor = BottleNumberFactory.create_successor(self.bottle_number)
        return (
            f"{self.bottle_number} of beer on the wall, ".capitalize()
            + f"{self.bottle_number} of beer.\n"
            f"{self.bottle_number.action()}, "
            f"{successor} of beer on the wall.\n"
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
