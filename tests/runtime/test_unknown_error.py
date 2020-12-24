import friendly_traceback


class MyException(Exception):
    pass


def test_Generic():
    try:
        raise MyException("Some informative message about an unknown exception.")
    except Exception as e:
        message = str(e)
        friendly_traceback.explain_traceback(redirect="capture")
    result = friendly_traceback.get_output()
    
    assert "Some informative message" in result
    if friendly_traceback.get_lang() == "en":
        assert "No information is available about this exception." in result
    return result, message


if __name__ == "__main__":
    print(test_function_unknown_error()[0])
