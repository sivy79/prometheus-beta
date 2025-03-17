import re

def validate_email(email):
    """
    Validate the format of an email address.
    
    Args:
        email (str): The email address to validate.
    
    Returns:
        bool: True if the email is valid, False otherwise.
    
    Validation criteria:
    - Must have a username part before the @
    - Must have a domain part after the @
    - Username can contain letters, numbers, dots, underscores, and hyphens
    - Domain must have at least one dot
    - Total length between 3 and 254 characters
    - No consecutive dots in username or domain
    - No leading or trailing dots in username or domain
    """
    # Check if email is a string and not empty
    if not isinstance(email, str) or not email:
        return False
    
    # Check total length
    if len(email) < 3 or len(email) > 254:
        return False
    
    # Regular expression for email validation
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Additional checks beyond regex
    if not re.match(email_regex, email):
        return False
    
    # Split email into username and domain
    username, domain = email.split('@')
    
    # Check for consecutive or leading/trailing dots
    if '..' in username or '..' in domain or \
       username.startswith('.') or username.endswith('.') or \
       domain.startswith('.') or domain.endswith('.'):
        return False
    
    return True