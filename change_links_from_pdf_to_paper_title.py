import re
#import os os.chdir('')

#index.html:
#<a href="(.{3,70})"><font color=black>(.{2,70})</font></a>
#<a class="two" href="\1">\2</a>
#
#<a style="text-decoration:none" href="(.{3,70})"><font color=black>(.{2,70})</font></a>
#<a class="two" href="\1">\2</a>
#
#(\d]</b>) (\w.+?) \[<a href="(\w.+?)">pdf</a>\]
#\1 <a class="one" href="\3">\2</a>

mode = 2
if mode==1:
	pattern = re.compile(r'<font color=black>(.+?)</font>', re.IGNORECASE)
	newstr = r'\1'
	# '?' makes it non-greedy, or better use [^<]+; see https://stackoverflow.com/a/2503441
elif mode==2:
	pattern = re.compile(r'\]</b> (.+?) (\[<a .*? href=".+?">)pdf(</a>])')
	newstr = r'\]</b> \2\1\3'
#Improving IoT data quality in mobile crowd sensing: A cross validation approach</b> [<a class="one" href="pub/IOTJ19_iot_data_quality_crowdsensing_cross_validation.pdf">pdf</a>]
#sometimes you may encounter UnicodeDecodeError, then you can use open(..., encoding='utf-8')
with open('C:\\Users\\tlbh9\\Documents\\GitHub\\tluocs.github.io\\pub_new.html', 'r') as f:
	with open('C:\\Users\\tlbh9\\Documents\\GitHub\\tluocs.github.io\\pub_new2.html', 'w') as wf:
		# skip until <BODY> just to speed up
		line = f.readline()
		while line.lower() != '<body>\n':
			wf.write(line)
			line = f.readline()
		wf.write(line)

		print('Header skipped. Now looking for the pattern and substituting...')

		# find and substitute link styles
		n_replaced = 0
		for line in f.readlines(): # f == f.readlines()
			#for match in pattern.finditer(line):
			match = pattern.search(line)
			if match is None:
				wf.write(line)
			else:
#				print(match.group(0))
				newline = pattern.sub(newstr, line)
#				print(newline)
				wf.write(newline)
				n_replaced += 1

print(f'Done. {n_replaced} lines replaced.')
