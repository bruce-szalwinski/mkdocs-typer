def pytest_assertrepr_compare(config, op, left, right):
    if op in ('==', '!='):
        return ['{0} {1} {2}'.format(left, op, right)]
