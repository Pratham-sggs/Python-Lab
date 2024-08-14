def change_case(string, style) :
	if(style == "c" or style == "C") :
		result_list = [];
		result = "";
		for i in range(0,len(string)) :
			for k in range(97,123) :
				l = chr(k)
				if(l==string[i]) :
					result_list.append(chr(k-32))
					break;
				else :
					if(chr(k-32) == string[i]) :
						result_list.append(string[i])
		for i in range(0,len(result_list)) :
			result =  result + result_list[i];
		return result;
	elif(style == "s" or style == "S") :
		result_list = [];
		result = "";
		for i in range(0,len(string)) :
			for k in range(65,91) :
				l = chr(k)
				if(l==string[i]) :
					result_list.append(chr(k+32))
					break;
				else :
					if(chr(k+32) == string[i]) :
						result_list.append(string[i])
		for i in range(0,len(result_list)) :
			result =  result + result_list[i];
		return result;
	elif(style == "r" or style == "R") :
		result_list = [];
		result = "";
		for i in range(0,len(string)) :
			for k in range(65,91) :
				if(chr(k)==string[i]) :
					result_list.append(chr(k+32))
				if(chr(k+32) == string[i]) :
						result_list.append(chr(k))
		for i in range(0,len(result_list)) :
			result =  result + result_list[i];
		return result;
	elif(style == "u" or style == "U") :
		result_list = [];
		result = "";
		for i in range (65,91) :
		if(i == )
		






print(change_case("SGgS","R"))