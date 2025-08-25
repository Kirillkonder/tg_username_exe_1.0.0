import random
import string
from typing import List, Set

def generate_random_letters(length: int) -> str:
    """Генерация случайных букв заданной длины"""
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def should_clear_memory(used_usernames: Set[str], generation_attempts: int, 
                       max_used: int = 5000, max_attempts: int = 10000) -> bool:
    """Проверяет, нужно ли очистить память"""
    return len(used_usernames) > max_used or generation_attempts > max_attempts