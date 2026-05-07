def response(hey_bob):
    stripped = hey_bob.strip()

    # Silence
    if stripped == "":
        return "Fine. Be that way!"

    # Check if it's yelling
    letters = [c for c in stripped if c.isalpha()]
    is_yelling = letters and all(c.isupper() for c in letters)

    # Check if it's a question
    is_question = stripped.endswith("?")

    # Yelling question
    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"

    # Question
    if is_question:
        return "Sure."

    # Yelling
    if is_yelling:
        return "Whoa, chill out!"

    # Anything else
    return "Whatever."