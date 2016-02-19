__author__ = 'Tony'
def eat_vowerls(s):
    """
    :param s: Remoes the vowels from s
    :return: s
    """
    return ''.join([c for c in s if c.lower() not in 'a'])

print [n * n for n in range(1, 11)]
print [a for a in 'pizza']
print eat_vowerls('apple')