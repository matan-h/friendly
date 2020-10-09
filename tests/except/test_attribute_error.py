import friendly_traceback


def test_attribute_error():
    class A:
        pass

    A()
    try:
        A.x
    except Exception:
        friendly_traceback.explain(redirect="capture")
    result = friendly_traceback.get_output()
    assert "AttributeError: type object 'A' has no attribute 'x'" in result
    if friendly_traceback.get_lang() == "en":
        assert "In your program, the object is `A` and the attribute is `x`." in result
    return result


def test_misspelled_module_attribute():
    import string

    try:
        string.ascii_lowecase
    except Exception:
        friendly_traceback.explain(redirect="capture")
    result = friendly_traceback.get_output()
    assert "AttributeError: module 'string' has no attribute 'ascii_lowecase'" in result
    if friendly_traceback.get_lang() == "en":
        assert "perhaps you meant one of the following:" in result
        assert " [`ascii_lowercase`," in result
    return result


def test_misspelled_module_attribute_2():
    import math

    try:
        math.cost
    except Exception:
        friendly_traceback.explain(redirect="capture")
    result = friendly_traceback.get_output()
    assert ("AttributeError: module 'math' has no attribute 'cost'") in result
    if friendly_traceback.get_lang() == "en":
        assert (
            "Instead of writing `cost`, perhaps you meant one of the following:\n"
            in result
        )
    assert "`cos`, `cosh`" in result
    return result


def test_nonetype():
    a = None
    try:
        a.b
    except Exception:
        friendly_traceback.explain(redirect="capture")
    result = friendly_traceback.get_output()
    assert "'NoneType' object has no attribute 'b'" in result
    if friendly_traceback.get_lang() == "en":
        assert "for a variable whose value is `None`" in result


if __name__ == "__main__":
    print(test_attribute_error())
