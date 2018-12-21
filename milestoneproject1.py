import os
winner = -1


c=0

s='1 2 3 4 5 6 7 8 9  '



def printboard(n):
	global s, winner
	global c
	if n != 0:
		if c%2==0:
			symb='0'
		else:
			symb='X'
		
		i=s.find(n)
		if s[i+1]==' ':
			s=s[:i+1]+symb+s[i+2:]
		else:
			print()
			print()
			print('!!!!!Already taken!!!!!!')
			c-=1
	

	
	sv='   |   |   '
	sh='-----------'
	s3=' {} | {} | {} '.format(s[13],s[15],s[17])
	s2=' {} | {} | {} '.format(s[7],s[9],s[11])
	s1=' {} | {} | {} '.format(s[1],s[3],s[5])
	print(sv)
	print(s3)
	print(sv)
	print(sh)

	print(sv)
	print(s2)
	print(sv)
	print(sh)

	print(sv)
	print(s1)
	print(sv)

	if s[13] == s[15] == s[17] :
		if s[13] == 'X':
			winner = 2
		elif s[13] == '0':
			winner = 1
	if s[7] == s[9] == s[11] :
		if s[7] == 'X':
			winner = 2
		elif s[7] == '0':
			winner = 1
	if s[3] == s[5] == s[1] :
		if s[1] == 'X':
			winner = 2
		elif s[1] == '0':
			winner = 1
	if s[13] == s[9] == s[5] :
		if s[13] == 'X':
			winner = 2
		elif s[13] == '0':
			winner = 1
	if s[1] == s[9] == s[17] :
		if s[1] == 'X':
			winner = 2
		elif s[1] == '0':
			winner = 1
	if s[1] == s[13] == s[7] :
		if s[1] == 'X':
			winner = 2
		elif s[1] == '0':
			winner = 1
	if s[3] == s[9] == s[15] :
		if s[3] == 'X':
			winner = 2
		elif s[3] == '0':
			winner = 1
	if s[11] == s[5] == s[17] :
		if s[11] == 'X':
			winner = 2
		elif s[11] == '0':
			winner = 1
	ans=['y']
	if ' ' not in [s[1], s[3], s[5], s[7], s[9], s[11], s[13], s[15], s[17]]:
		ans = ['n']
	return ans


if __name__=='__main__':
	ans=['y']
	os.system('clear')
	printboard(0)
	
	while ans==['y']:
		n=input('Choose your next position (1-9) player {} :'.format((c%2)+1))
		os.system('clear')
		ans=printboard(n)
		if winner != -1:
			break
		c+=1
if winner != -1:
	print('WINNER IS PLAYER:'+str(winner))
else:
	print('DRAW!!!')