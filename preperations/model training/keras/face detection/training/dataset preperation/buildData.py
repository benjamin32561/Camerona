
def main():
	path = "test2017.txt"
	dst = "all.txt"
	f = open(path, 'r')
	lines = f.read().split('\n')
	f.close()
	data = {}
	for line in lines:
		line = line.split(' ')
		name = line[0]
		points = line[1:]
		try:
			if len(data[name]) < 20:
				data[name].append(points)
		except:
			data[name] = [points]
	lines = []
	for key in data:
		line = key
		for point in data[key]:
			line += ' ' + ','.join(point)
		lines.append(line)
	f = open(dst, 'w+')
	f.write('\n'.join(lines))
	f.close()


if __name__ == '__main__':
    main()