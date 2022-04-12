def remove_match_int():
	#dummy u
	start_range	= int(input('start range'))
	end_range = int(input("end range"))
	if start_range > end_range :
		print("bad request")
		return 0
	list_my = []
	with open("file", "r", encoding="utf8") as file_decoder:
		for line in file_decoder: # read rest of lines
			for line_split in line.split() :
				if not(int(line_split) >= start_range and int(line_split) <= end_range):
					list_my.append(int(line_split))
	print(list_my)
	return 1