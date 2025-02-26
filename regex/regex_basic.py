def parse_shape(param):
    """
    Parse a regex string into an abstract syntax tree (AST) representation.

    Args:
        param (str): The regex string to parse.

    Returns:
        The AST representation of the regex.

    Raises:
        Exception: If the regex string contains invalid syntax.
    """
    if not param:
        return None
    idx, ast = parse_concat(param, 0)
    if idx != len(param):
        raise Exception("Invalid regex syntax")
    return ast


def parse_int(regex_str, idx):
    """
    Parse an integer from the regex string starting at the given index.

    Args:
        regex_str (str): The regex string.
        idx (int): The starting index.

    Returns:
        tuple: A tuple containing the new index and the parsed integer (or None if no integer is found).
    """
    save = idx
    while idx < len(regex_str) and regex_str[idx].isdigit():
        idx += 1
    return idx, int(regex_str[save:idx]) if save != idx else None


def parse_postfix(regex_str, idx, node):
    """
    Parse postfix operators (*, +, ?, {m,n}) following a node.

    Args:
        regex_str (str): The regex string.
        idx (int): The current index in the regex string.
        node: The current node being parsed.

    Returns:
        tuple: A tuple containing the new index and the modified node.

    Raises:
        Exception: If the postfix syntax is invalid.
    """
    if idx >= len(regex_str):
        return idx, node

    char = regex_str[idx]
    if char == '*':
        idx += 1
        return idx, ('repeat', node, 0, None)  # * means 0 or more
    elif char == '+':
        idx += 1
        return idx, ('repeat', node, 1, None)  # + means 1 or more
    elif char == '?':
        idx += 1
        return idx, ('repeat', node, 0, 1)  # ? means 0 or 1
    elif char == '{':
        idx += 1
        # Parse the min value
        idx, min_val = parse_int(regex_str, idx)
        if min_val is None:
            raise Exception("Invalid {} syntax")
        max_val = min_val
        # Parse the max value if present
        if idx < len(regex_str) and regex_str[idx] == ',':
            idx += 1
            idx, max_val_part = parse_int(regex_str, idx)
            if max_val_part is not None:
                max_val = max_val_part
            else:
                max_val = None  # {3,} means 3 or more
        if idx >= len(regex_str) or regex_str[idx] != '}':
            raise Exception("Unclosed {")
        idx += 1
        return idx, ('repeat', node, min_val, max_val)
    else:
        return idx, node


def parse_node(regex_str, idx):
    """
    Parse a single node in the regex (character, group, or postfix operator).

    Args:
        regex_str (str): The regex string.
        idx (int): The current index in the regex string.

    Returns:
        tuple: A tuple containing the new index and the parsed node.

    Raises:
        Exception: If the syntax is invalid.
    """
    char = regex_str[idx]
    idx += 1
    assert char not in '|)', "Invalid character in parse_node"
    if char == '(':
        # Parse a group
        idx, node = parse_split(regex_str, idx)
        if idx < len(regex_str) and regex_str[idx] == ')':
            idx += 1
        else:
            raise Exception('Unbalanced parenthesis')
    elif char in '*+{':
        raise Exception('Nothing to repeat')
    else:
        node = char  # Single character node
    # Handle postfix operators
    idx, node = parse_postfix(regex_str, idx, node)
    return idx, node


def parse_concat(regex_str, idx):
    """
    Parse a concatenation of nodes (e.g., 'ab').

    Args:
        regex_str (str): The regex string.
        idx (int): The current index in the regex string.

    Returns:
        tuple: A tuple containing the new index and the parsed concatenation node.
    """
    prev = None
    while idx < len(regex_str):
        if regex_str[idx] in '|)':
            break  # Stop if alternation or group end is encountered
        idx, node = parse_node(regex_str, idx)
        if prev is None:
            prev = node
        else:
            prev = ('cat', prev, node)  # Create a concatenation node
    return idx, prev


def parse_split(regex_str, idx):
    """
    Parse an alternation (e.g., 'a|b').

    Args:
        regex_str (str): The regex string.
        idx (int): The current index in the regex string.

    Returns:
        tuple: A tuple containing the new index and the parsed alternation node.
    """
    idx, prev = parse_concat(regex_str, idx)
    while idx < len(regex_str):
        if regex_str[idx] == ')':
            break  # Stop if group end is encountered
        assert regex_str[idx] == '|', 'BUG: Expected alternation operator'
        idx, node = parse_concat(regex_str, idx + 1)
        prev = ('split', prev, node)  # Create an alternation node
    return idx, prev


# Test cases
assert parse_shape('') is None
assert parse_shape('a') == 'a'
assert parse_shape('ab') == ('cat', 'a', 'b')
assert parse_shape('a+') == ('repeat', 'a', 1, None)
assert parse_shape('a{3,6}') == ('repeat', 'a', 3, 6)
