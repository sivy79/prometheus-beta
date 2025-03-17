import pytest
from src.email_validator import validate_email

def test_valid_emails():
    """Test a variety of valid email addresses."""
    valid_emails = [
        'user@example.com',
        'firstname.lastname@example.com',
        'user+tag@example.com',
        'user-name@example.co.uk',
        'user123@example.org',
        'user_name@sub.example.com',
    ]
    for email in valid_emails:
        assert validate_email(email), f"{email} should be valid"

def test_invalid_emails():
    """Test various invalid email address formats."""
    invalid_emails = [
        '',  # Empty string
        'invalid.email',  # No @ symbol
        '@invalid.com',  # No username
        'invalid@.com',  # No domain name
        'invalid@com',  # No top-level domain
        'in..valid@example.com',  # Consecutive dots
        '.invalid@example.com',  # Leading dot in username
        'invalid.@example.com',  # Trailing dot in username
        'in valid@example.com',  # Spaces not allowed
        'invalid@example.',  # Incomplete top-level domain
        123,  # Non-string input
        None,  # None input
    ]
    for email in invalid_emails:
        assert not validate_email(email), f"{email} should be invalid"

def test_email_length():
    """Test email length constraints."""
    # Very short email
    assert not validate_email('a@b.c')
    
    # Email with max valid length
    long_valid_email = 'a' * 64 + '@' + 'b' * 63 + '.' + 'c' * 63
    assert validate_email(long_valid_email)
    
    # Email exceeding max length
    long_invalid_email = 'a' * 255
    assert not validate_email(long_invalid_email)

def test_domain_checks():
    """Test specific domain validation rules."""
    # Valid domains
    assert validate_email('user@example.com')
    assert validate_email('user@sub.example.co.uk')
    
    # Invalid domains
    assert not validate_email('user@example')
    assert not validate_email('user@.com')
    assert not validate_email('user@example.')
    assert not validate_email('user@ex..ample.com')