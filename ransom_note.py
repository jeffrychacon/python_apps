def ransom_note(magazine: str, note: str):
  #magazine=magazine.isalpha();
  magazine_words= []
  note_words = []
  mydic = {}
  for c in magazine:
    #print (c)
    if (c.isalpha()):
      magazine_words.append(c)
  magazine_words.sort()
  for t in note:
    #print (c)
    if (t.isalpha()):
      note_words.append(t)
  note_words.sort()
 
  mydic={}
  mydic2={}
  for d in magazine_words:
    if d not in mydic:
      mydic[d]=1
    mydic[d]+=1
   
  for p in note_words:
    if p not in mydic2:
      mydic2[p]=1
    mydic2[p]+=1
 
  for a in mydic2:
    if a not in mydic:
      print('not possible')
      return 'failed'
    else:
      if (mydic2[a]<=mydic[a]):
        continue
      else:
        print('not possible')
        return 'failed'
  print('yes')
  #print(magazine_words)

ransom_note("I want to go to new york with my mom","I am in New York")
ransom_note("I want to go to New York with my mom","I am in New York")
