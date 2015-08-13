# -*- coding: utf-8 -*-

input = u"""A personal grudge prompted Catapan to attack the couple using a sword," he said."""


r = input.count(u"“")
l = input.count(u"”")
qr= input.count('"')


if r != l:
	for i in input:
		if i == u"”":
			input = u"“%s" % input 
			
		elif i == u"“":
			input = u"%s”" % input
else:
	for o in input:
		if qr%2!=0:
			if len(o) == 0:
				input = '%s"' % input
				qr= input.count('"')
			else:
				input = '"%s' % input
				qr= input.count('"')
			

			

print input