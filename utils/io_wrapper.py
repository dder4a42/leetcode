#!/usr/bin/env python3
"""
Decorator system for automatic I/O conversion based on type annotations.
"""

import inspect
from typing import Any, get_type_hints, get_origin, get_args
from .io_conversion import convert_to_target_type, convert_from_type


def auto_io(func):
    """
    Decorator that automatically converts function arguments and return values
    based on type annotations.
    """
    hints = get_type_hints(func)
    sig = inspect.signature(func)

    def wrapper(*args, **kwargs):
        has_varargs = any(
            p.kind == inspect.Parameter.VAR_POSITIONAL for p in sig.parameters.values()
        )

        if has_varargs or not sig.parameters:
            result = func(*args, **kwargs)
        else:
            bound = sig.bind_partial(*args, **kwargs)
            bound.apply_defaults()

            for param_name, param in sig.parameters.items():
                if param_name in hints and param_name in bound.arguments:
                    arg_value = bound.arguments[param_name]
                    target_type = hints[param_name]
                    bound.arguments[param_name] = convert_to_target_type(
                        arg_value, target_type
                    )

            result = func(**bound.arguments)

        # Convert return value based on return type annotation
        if "return" in hints:
            result = convert_from_type(result, hints["return"])

        return result

    # Preserve the original function's metadata
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    wrapper.__annotations__ = func.__annotations__

    return wrapper


def with_types(*input_types, return_type=None):
    """
    Decorator that explicitly specifies input and output types for conversion.
    Use this when type annotations are not available or you want to override them.

    Example:
        @with_types(ListNode, return_type=ListNode)
        def solve(head):
            ...
    """

    def decorator(func):
        # Store type info as function attribute
        func._input_types = input_types
        func._return_type = return_type

        def wrapper(*args, **kwargs):
            # Convert input arguments
            converted_args = []
            for i, arg in enumerate(args):
                if i < len(input_types):
                    converted_args.append(convert_to_target_type(arg, input_types[i]))
                else:
                    converted_args.append(arg)

            # Call the function
            result = func(*converted_args, **kwargs)

            # Convert return value
            if return_type is not None:
                result = convert_from_type(result, return_type)

            return result

        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        return wrapper

    return decorator
