# 99-bottles-of-oop-python-v2.2

## Thoughts on Python Version 2.2

* Assigning the responsibility of creating `BottleNumber`-like instances to `BottleNumber.__new__()` has a few implications:
	* All `BottleNumber`-like classes must inherit from `BottleNumber`.
	* Subclasses of `BottleNumber` behave oddly when directly instantiated. For example, `BottleNumber0(500)` calls the `__new__()` method it inherits, but `__init__()` isn’t called automatically. This is because the return of `__new__()` isn’t of type `BottleNumber0` or its subtype; instead, it may be one of its siblings (`BottleNumber1`, `BottleNumber6`, etc.) or its superclass (`BottleNumber`).

* The `BottleNumber`-like classes include an instance method called `successor()`, meaning each class instance is responsible for knowing its successor and creating it. This design seems a bit counterintuitive.

## Proposed Solution

Introduce a `BottleNumberFactory` to:
* Create `BottleNumber`-like instances from an integer via `BottleNumberFactory.from_number()`. This provides a unified way to create `BottleNumber`-like instance from integers.

* Generate a successor for any `BottleNumber`-like instance using `BottleNumberFactory.create_successor()`. This centralizes the logic for determining successors and uses `BottleNumberFactory.from_number()` internally to create the successor (another `BottleNumber`-like instance).

With this modification, we can now create a `BottleNumber`-like class without inheriting from `BottleNumber`, as long as it implements the `AbstractBottleNumber` interface. The created class can then be used with `BottleNumberFactory.from_number()`, which selects the appropriate `BottleNumber`-like class. Additionally, `BottleNumber`-like classes can now be instantiated directly without odd behavior, but you should have a strong reason to do something like `BottleNumber0(500)`. Generally, `BottleNumberFactory.from_number()` should be the preferred method to create a `BottleNumber`-like instance.