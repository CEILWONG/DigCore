

#y=x+1;y=2x+2

def Dec(option):
    if option==1:
        def xx1(x):
            return x+1
        return xx1
    else:

        def xx2(x):
            return 2*x+2
        return xx2

def main():
    YX1=Dec(1)
    YX2=Dec(2)

    print('YX1=%d'%YX1(1))
    print('YX2=%d'%YX2(1))

main()