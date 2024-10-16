def areSentencesSimilar( sentence1: str, sentence2: str) -> bool:
        if len(sentence1) < len(sentence2) :
            sentence1, sentence2 = sentence2, sentence1
        if sentence1.startswith(sentence2) or sentence1.endswith(sentence2) :
            return True
        s = sentence1.split()
        s1 = sentence2.split()
        result = []
        truth = True
        start = []
        end = []
        for i in s : 
            if i not in s1 :
                result.append(i)
                truth = False
            else :
                if truth :
                    start.append(i)
                else :
                    end.append(i)
        result = " ".join(start) + " " + " ".join(result) + " " + " ".join(end)
        print(result)
        print(sentence1)
        return result == sentence1
print(areSentencesSimilar("My name is Haley","My Haley"))
print(areSentencesSimilar("of","A lot of words"))
print(areSentencesSimilar("Eating right now","Eating"))
print(areSentencesSimilar("UI wqhw Lf","ezzXqqEQcS"))