# app/moderation.py


# A very simple moderation module example
# Purpose: Block unsafe prompts early

BLOCKLIST = ["kill", "bomb", "attack", "terror", "hack"]

def is_safe(prompt: str) -> bool:
    """
    Check if the prompt is safe.
    Returns (True, "") if safe, (False, reason) if blocked.
    """
    lower_prompt = prompt.lower()
    for word in BLOCKLIST:
        if word in lower_prompt:
            return False, f"Blocked due to forbidden term: '{word}'"
    return True, ""