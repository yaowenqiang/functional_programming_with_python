> python imperative(命令式) vs declarative(声明式)

> imperative has state changes

> python -c 'import this'

basic dictionary comprehensions

{key: value for key, value in source}

{key: value for key, value in source if condition}
{key: value for key, value in source.items() if key == x}
{key: func(value) for key, value in source.items() if key == x}

