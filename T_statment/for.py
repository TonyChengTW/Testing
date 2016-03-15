chars = 'SAHFI'
for i, c in enumerate(chars):
    print i, c
print '\n'
#-------------------------------
cs = 'AO'
ws = ['Apple','Orange']
for c, w in zip(cs, ws):
    print c, w
print '\n'

#-----------------------------
student_scores = [(90,100), (60,80)]
print (sum(zip(*student_scores)[1])+.0) / len(student_scores)
