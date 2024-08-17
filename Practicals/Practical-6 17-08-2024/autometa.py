alpha = {"a","b"}
def dfa (text) :
	final_state = {"q1"}
	current_state = q0(text);
	if current_state in final_state :
		return "Accepted"
	else :
		return "Rejected"

def q0 (text) :
	if text == "" :
		return "Rejected"
	elif text[0] not in alpha :
		return "Rejected"
	elif text[0] == "a" :
		return q1(text[1:] if len(text)>1 else "")
	elif text[0] == "b" :
		return q0(text[1:] if len(text)>1 else "")

def q1 (text) :
	if text == "" :
		return "q1"
	elif text[0] not in alpha :
		return "Rejected"
	elif text[0] == "a" :
		return q1(text[1:] if len(text)>1 else "")
	elif text[0] == "b" :
		return q0(text[1:] if len(text)>1 else "")


print(dfa("abba"))