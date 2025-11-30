def safe_divide(numerator, denominator):
    """
    Perform division while handling errors.

    Parameters:
        numerator (str or float): numerator value
        denominator (str or float): denominator value

    Returns:
        str: result message or error message
    """
    try:
        # Convert inputs to floats
        num = float(numerator)
        denom = float(denominator)

        # Attempt division
        result = num / denom
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
