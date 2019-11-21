import pytest
from pythonexercises import anti_vowel

def test_anti_vowel():
    assert anti_vowel.anti_vowel("HELLOWORLD")=="HLLWRLD"
