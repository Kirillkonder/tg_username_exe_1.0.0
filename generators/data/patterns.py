import random
PATTERNS_4CHAR = ['cvcv', 'vcvc', 'cvc', 'vcv', 'vvcc', 'ccvv']
PATTERNS_5CHAR = ['cvcvc', 'vcvcv', 'cvccv', 'vcvcv', 'cvvcc', 'ccvvc']

def generate_from_pattern(pattern: str) -> str:
    """Генерация юзернейма по паттерну"""
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    
    result = []
    for char in pattern:
        if char == 'c':
            result.append(random.choice(consonants))
        elif char == 'v':
            result.append(random.choice(vowels))
        else:
            result.append(char)
    
    return ''.join(result)