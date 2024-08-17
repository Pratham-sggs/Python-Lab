def slice(object, slicing_parameters) :
	length = len(slicing_parameters)

	if length > 3 :
		return "Only 3 arguments required";
	
	start = 0;
	end = len(object);
	step = 1;
	result = "";
	
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
	if end > len(object) :
		end = len(object);

	if (start>= end) :
		type_of_obj = type(object)
		
		if type_of_obj == str :
			return "";
		else :
			return [];
	elif (start < end and start >= 0 and end > 0 and step > 0) :
		type_of_obj = type(object)
		truth = False
		if type_of_obj == str :
			truth = True;

		if truth :
			i = start;
			while i < end :
				result = result + object[i]
				i += step
			return result;
		else :
			i = start;
			result = []
			while i < end :
				result.append(object[i])
				i += step
			return result;
	if (end >= 0 and start >= 0 and step < 0) :
		type_of_obj = type(object)
		
		if type_of_obj == str :
			return "";
		else :
			return [];


print(slice("hjekhaflieu",[8,6,1]))
			