def function(string, str_to_search_for):
      count = 0
      for x in range(len(string) - len(str_to_search_for) + 1):
           if string[x:x+len(str_to_search_for)] == str_to_search_for:
                count += 1
      return count

def minion(s):
    result = ""
    s = s.upper()
    vowels = "AEIOU"
    points_k = 0
    points_s = 0
    substrings_k = []
    kevin = []
    for i in range(len(s)):
        ctr = i
        if s[i] in vowels:
            while ctr  < len(s) + 1:
                substrings_k.append(s[i:ctr])
                ctr += 1
    substrings_s = []
    for j in range(len(s)):
        ctr = 1
        if s[j] not in vowels:
            while ctr < len(s) + 1:
                substrings_s.append(s[j:ctr])
                ctr += 1
#            break
    for x in substrings_k:
        if x in s and x != "" and x not in kevin:
            kevin += [str(x)]
            points_k += function(s, x)
    kevin = sorted(kevin, key = len)
    stuart = []   
    for k in substrings_s:
        if k in s and k != "" and k not in stuart:
            stuart += [str(k)]
            points_s += function(s, k)
        stuart = sorted(stuart, key = len)
    if points_s == points_k:
        return "It was a draw!"
    elif points_k > points_s:
        result += "The winner was Kevin with a total of " + str(points_k) + " points:"
        for i in kevin:
            result += "\n" + "- " + str(i) + ": " + str(function(s, i))
    elif points_s > points_k:
        result += "The winner was Stuart with a total of " + str(points_s) + " points:"
        for i in stuart:
            result += "\n" + "- " + str(i) + ": " + str(function(s, i))
    return result
    
    
            
print(minion("ANANAS"))
    
