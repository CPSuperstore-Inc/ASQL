class ASQL:
    def __init__(self, iterable:list):
        self.array = iterable
        self.operation_mode = None
        self.selection_type = None

        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= len(self.array):
            raise StopIteration
        else:
            self.current += 1
            return self.array[self.current - 1]

    def __len__(self):
        return len(self.array)

    def max(self, prop, where:str=""):
        return max(getattr(node, prop) for node in self.filter(where))

    def min(self, prop, where:str=""):
        return min(getattr(node, prop) for node in self.filter(where))

    def sum(self, prop, where:str=""):
        return sum(getattr(node, prop) for node in self.filter(where))

    def avg(self, prop, where:str=""):
        results = self.filter(where)
        return sum(getattr(node, prop) for node in results) / float(len(results))

    def filter(self, query:str=""):
        results = self.array.copy()
        if query == "":
            return results
        args = query.split(" ")
        comparisons = ["<=", ">=","<", ">", "==", "!="]

        for a in args:
            for item in self.array:
                for c in comparisons:
                    if c in a:
                        prop, expected = a.split(c)
                        value = getattr(item, prop)
                        # noinspection PyUnusedLocal
                        expected = type(value)(expected)
                        if not eval("value {} expected".format(c)):
                            results.remove(item)
                        break

        return results

    def delete(self, query:str=""):
        queued = self.filter(query)
        for i in queued:
            self.array.remove(i)

        return queued

    def update(self, change, where):
        queued = self.filter(where)
        for item in range(len(queued)):
            for i in change.split(" "):
                prop, val = i.split("=")
                setattr(queued[item], prop, eval(val))
