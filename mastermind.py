import random
def computerin_secdiyi_texmini_rengler():
   lst1=[]
   for i in range(4):
       computerin_secimi=random.randint(0,5)
       lst1.append(computerin_secimi)
   return lst1
def istifadecinin_secimi():
    print('qirmizi ucun 0,mavi ucun 1,yasil ucun 2,qara ucun 3,sari ucun 4,ag ucun 5 secin')
    istifadeci_listi=[]
    for i in range(4):
        istifadecinin_secdiyi_reng=int(input('renge uygun ededi secin: '))
        istifadeci_listi.append(istifadecinin_secdiyi_reng)
    return istifadeci_listi
def yoxlama():
    lst1 = computerin_secdiyi_texmini_rengler()
    while True:
        texmin_sayi=0
        istifadeci_listi=istifadecinin_secimi()
        duzgun_yerde_reng = 0
        ferqli_yerde_duzgun_reng = 0
        for j in range(4):
            if istifadeci_listi[j]==(lst1[j]):
                duzgun_yerde_reng += 1
            elif istifadeci_listi[j] in lst1:
                ferqli_yerde_duzgun_reng += 1
        print('duzgun yerdeki renglerin sayi: ', duzgun_yerde_reng, 'duzgun reng lakin yanlis yerde: ', ferqli_yerde_duzgun_reng)
        texmin_sayi += 1
        if duzgun_yerde_reng==4:
             print('tebrikler! siz dogru tapdiniz')
             print('texmin sayisi ',texmin_sayi,'qederduir')
             break

yoxlama()