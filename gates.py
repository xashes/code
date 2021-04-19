#!/usr/bin/env python3


def and_gate(m: int, n: int) -> bool:
    return bool(m * n)


def or_gate(m: int, n: int) -> bool:
    return bool(m + n)


def test_gates():
    assert and_gate(0, 0) is False
    assert and_gate(1, 0) is False
    assert and_gate(0, 1) is False
    assert and_gate(1, 1) is True

    assert or_gate(0, 0) is False
    assert or_gate(1, 0) is True
    assert or_gate(0, 1) is True
    assert or_gate(1, 1) is True
