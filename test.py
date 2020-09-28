from . import example_pb2 as t


def add(a1: t.Amount, a2: t.Amount) -> t.Amount:
    return Amount(amount=a1.amount + a2.amount, currency=a1.currency)
