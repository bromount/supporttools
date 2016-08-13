from operator import itemgetter

data = [ [ "shrini",10,6],["jeeva",4,5],["ashok",1,8], ["suresh",10,4]  ]

print data

print sorted(data, key=itemgetter(1,2), reverse=True)

