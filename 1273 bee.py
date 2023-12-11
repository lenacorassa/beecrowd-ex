while True:
        
    n=int(input())
    words=[]
    maxtam=0

    if n==0:
        break

    for i in range(n):
        palavra=input()
        words.insert(len(words),palavra)
        if len(palavra)>maxtam:
            maxtam=len(palavra)
    
    for palavra in words:
        space=maxtam-len(palavra)
        neword=""
        for _ in range (space):
            neword+=" "
        neword+=palavra
        print(neword)
    print()
