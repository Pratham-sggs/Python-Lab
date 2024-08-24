def slice(object, slicing_parameters) :
	length = len(slicing_parameters)

	if length > 3 :
		return "Only 3 arguments required....";
	
	start = 0;
	end = len(object);
	step = 1;
	result = "";
	type_of_obj = type(object)
	if type_of_obj == str :
		truth_value = False
	if length == 1 :
		start = slicing_parameters.pop()

	elif length == 2 :
		end = slicing_parameters.pop()
		start = slicing_parameters.pop()
	elif length == 3 :
		step = slicing_parameters.pop()
		end = slicing_parameters.pop()
		start = slicing_parameters.pop()
	if step == 0 :
		return "Error! Step can't be 0"
	
	if start < 0:
		start += len(object)

	if end < 0:
		end += len(object)

	if step < 0:
			if start >= len(object):
				start = len(object) - 1
			if end < 0:
				end = -1
	
	if step > 0:
		if start >= len(object):
			return "" if type_of_obj == str else []
		if end > len(object):
			end = len(object)
		i = start
		while i < end:
			result += object[i]
			i += step
	else:

		if start < 0:
			return "" if type_of_obj == str else []
		i = start
		while i > end:
			result += object[i]
			i += step

	if type_of_obj == str :
		return result 
	else :
		return list(result)


print(slice("Pratham",[0,100,1]))