# A sample RGC program
def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

class Counter:
    value: int = 0

    def increment(self) -> None:
        self.value += 1

counter: Counter = @var Counter()
for i in range(10):
    counter.increment()
match counter.value:
    case 10 => print("ten")
    case _ => print(counter.value)
print(counter.value)