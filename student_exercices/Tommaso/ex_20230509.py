# def f1(my_list, my_object):
#     somme = 0
#     for i in my_list:
#         if i == my_object:
#             somme += 1
#     return somme
#
# print(f1([1, 1, 1, 2, 2, 2, 3], 2))
#
# print([1, 1, 1, 2, 2, 2, 3].count(2))
#
#
# def f2(*args,**kwargs):
#     print(args,kwargs)
#
# f2(1,1,1,2,3,x=1,y=3,z=0)

# def f3(*numbers):
#     somme = 0
#     for i in numbers:
#       somme += i
#     return somme
# print(f3(1,2,3,4))
# lettres = "abcd"
# for i in range(1, 21):
#     # 1-5 => 0 / 6-10 => 1 / 11-15 => 2 / 16-20 => 3
#     lettre = lettres[3 - (i - 1) // 5]
#     print(lettre, i)

# def grains(n):
#     if n == 1:
#         return 1
#
#     somme = 1
#     for i in range(n-1):
#         print(2**(i+1), somme)
#         somme += 2**(i+1)
#
#     return somme
#
# print(grains(64))

def trigo(minutes, heures):
    angle_minutes = minutes * 6
    angle_heures = (heures * 30) % 360
    angle_heures_precis = angle_heures + angle_minutes//12
    return abs(angle_minutes-angle_heures_precis),360-abs(angle_heures_precis-angle_minutes)

for h in range(0,24):
    for m in range(0,60,15):

        print(h,m,trigo(m,h))

