__author__ = 'root'

def play_undercut(p1, p2):
    p1.reset_score()
    p2.reset_score()
    m1 = p1.get_move()
    m2 = p2.get_move()
    print '%s move: %d' % p1.get_name(), m1
