corv, core, cors, flav, flae, flas = map(int, input().split())
corp = corv * 3 + core
flap = flav * 3 + flae
if corp>flap:
    print("C")
elif corp<flap:
    print("F")
elif corp==flap:
    if cors==flas:
        print("=")
    elif cors>flas:
        print("C")
    elif cors<flas:
        print("F")
