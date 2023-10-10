N1, N2, N3, N4 = map(float, input().split())
Media = ((N1*2 + N2*3 + N3*4 + N4*1)/10)
print(f"Media: {Media:.1f}")
if Media >= 7.0:
    print("Aluno aprovado.")
elif 5.0 <= Media <= 6.9:
    print("Aluno em exame.")
    N5 = float(input())
    print (f"Nota do exame: {N5:.1f}")
    mf = (N5+Media)/2
    if mf >= 5.0:
        print("Aluno aprovado.")
        print(f"Media final: {mf:.1f}")
elif Media < 5.0:
    print("Aluno reprovado.")
    