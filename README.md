# Array SQL
This project creates a new class, which takes a single list.
Each item in the list MUST be of the same datatype.
This allows you to query the properties in a list quickly and easily

# Code Examples
Creating A New ASQL Class:
```python
from ASQL import ASQL

class Person:
    def __init__(self, age):
        self.age = age

a = ASQL([Person(5), Person(6), Person(7), Person(8)])
```

The objects passed into the array can be custom or built-in. They just need to be the same.
_Note_: This is not enforced in code, however, may cause problems if all objects do not have the same properties.


Querying A Class:
```python
a.filter("age>5")
# returns 3 items
```
This returns each instance of the class, where the age is less than 5.
It supports all 6 basic comparison operators: `<=`, `>=`,`<`, `>`, `==`, and `!=`
You can have multiple filters in one call. Just seporate each operation with a space.

**PLEASE NOTE**: Comparisons can not contain spaces!
This is ok: `age<5`. This is NOT ok: `age < 5`.

Deleting Records
```python
a.delete("age>5")
```
This deletes every record which would otherwise be returned from the filter function.

Updating Records:
```python
a.update("age=5", "age>5")
```
This updates every record which would otherwise be returned from the filter function.
The first arguement is the replacement in the format of `property=value`.
There can be multiple which are seporated by spaces, but there can be no spaces inbetween each equality statement.

#Other Operations
There are other operations which can be applied to the ASQL object.

`a.max(property, query)` returns the largest value stored in a specified propery, and respects the query.

`a.min(property, query)` returns the smallest value stored in a specified propery, and respects the query.

`a.sum(property, query)` returns the sum of all of the values stored in a specified propery, and respects the query.

`a.avg(property, query)` returns the average of the values stored in a specified propery, and respects the query.

# Other Features
The ASQL object can return the length of the items in it with `len(a)`

You can iterate over each item with a basic `for` loop
