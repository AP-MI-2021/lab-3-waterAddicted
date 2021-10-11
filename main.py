import math

def citire_date():
    result_list = []
    lst = input('Introduceti lista: ')
    str_lst = lst.split()
    for string_element in str_lst:
        element = int(string_element)
        result_list.append(element)
    return result_list


def palindrm(nr):
    '''
    Functia verifica daca un numar este palindrom sau nu.
    :param nr: numar intreg
    :return: True daca numarul este palindrom sau False in caz contrar.
    '''
    nr = abs(nr)
    lungime_numar = int(math.log10(nr)) + 1
    st = 1
    dr = lungime_numar
    t = 10
    t = t ** lungime_numar
    t = t // 10
    k = 10
    while st < dr:
        if int(nr % k // (k // 10)) == int(nr // t % 10):
            st += 1
            dr -= 1
            t = t // 10
            k = k * 10
        else:
            break
    if st >= dr:
        return True
    return False

#problema 5
def get_longest_all_palindromes(lst: list[int]) -> list[int]:
    ''' 
    Functia returneaza cea mai lunga subsecventa de numere care sunt palindroame.
    :param lst:lista de elemente
    :return:cea mai lunga subsecventa de numere care sunt palindrom
    '''
    result_lst = []
    start = 0
    finish = 0
    termeni_ok = 0
    curent = 0
    gasit = False
    for i in lst:
        element = int(i)
        if palindrm(element):
            termeni_ok += 1
            gasit = True
        elif palindrm(element) == False or curent == len(lst)-1:
            if termeni_ok >= finish - start + 1 and gasit:
                start = curent - termeni_ok
                finish = curent
            termeni_ok = 0
            gasit = False

        curent += 1
    #cazul in care ultimul termen al listei a fost palindrom
    if palindrm(lst[len(lst)-1]) and termeni_ok > finish - start:
        start = curent - termeni_ok
        finish = curent
    if finish - start == 0 and gasit == True:
        result_lst.append(lst[start])
    else:
        for i in range(start, finish):
            result_lst.append(lst[i])
    return result_lst

def x_la_puterea_k(numar,k):
    '''
    Functia determina daca un numar este egal sau nu cu un numar oarecare la puterea k.
    Input: numar = numarul care este verificat,k = puterea data
    Output: True daca numarul este egal cu un numar oarecare la puterea k;False in caz contrar
    '''
    rez = 0
    while rez ** k < numar:
        rez += 1
    if rez ** k == numar:
        return True
    return False

#problema 15
def get_longest_powers_of_k(lst: list[int], k: int) -> list[int]:
    '''
    Functia returneaza cea mai lunga subsecventa de numere care au forma de x la puterea k.
    :param lst:lista de elemente
    :return:cea mai lunga subsecventa de numere pentru care exista un x care la puterea k este egal cu acestea.
    '''
    result_lst = []
    start = 0
    finish = 0
    termeni_ok = 0
    curent = 0
    gasit = False
    for i in lst:
        element = int(i)
        if x_la_puterea_k(element,k):
            termeni_ok += 1
            gasit = True
        elif x_la_puterea_k(element,k) == False or curent == len(lst)-1:
            if termeni_ok >= finish - start + 1 and gasit:
                start = curent - termeni_ok
                finish = curent
            termeni_ok = 0
            gasit = False

        curent += 1
    #cazul in care ultimul termen al listei a fost un numar care se poate scire ca x la puterea k
    if x_la_puterea_k(lst[len(lst)-1],k) and termeni_ok > finish - start:
        start = curent - termeni_ok
        finish = curent
    if finish - start == 0 and gasit == True:
        result_lst.append(lst[start])
    else:
        for i in range(start, finish):
            result_lst.append(lst[i])
    return result_lst
def test_get_longest_all_palindromes():
    '''
    Functia testeaza funtionalitatea functiei
    '''
    lst = [23, 1, 4, 11, 919, 43, 25, 9, 8]
    result_lst = get_longest_all_palindromes(lst,)
    assert (result_lst[0] == 1)
    assert (result_lst[1] == 4)
    assert (result_lst[2] == 11)
    assert (result_lst[3] == 919)
    lst = [1, 8, 22, 6, 43, 25, 9, 8]
    result_lst = get_longest_all_palindromes(lst)
    assert (result_lst[0] == 1)
    assert (result_lst[1] == 8)
    assert (result_lst[2] == 22)
    assert (result_lst[3] == 6)
    lst = [12, 22, 34, 37, 76, 85, 98, 13, 511]
    result_lst = get_longest_all_palindromes(lst)
    assert (result_lst[0] == 22)


def test_get_longest_powers_of_k():
    '''
    Functia testeaza funtionalitatea functiei get_longest_powers_of_k
    '''
    lst = [23, 1, 4, 16, 9, 43, 25, 9, 8]
    result_lst = get_longest_powers_of_k(lst,2)
    assert (result_lst[0] == 1)
    assert (result_lst[1] == 4)
    assert (result_lst[2] == 16)
    assert (result_lst[3] == 9)
    lst = [3, 1, 8, 27, 64, 43, 25, 9, 8]
    result_lst = get_longest_powers_of_k(lst,3)
    assert (result_lst[0] == 1)
    assert (result_lst[1] == 8)
    assert (result_lst[2] == 27)
    assert (result_lst[3] == 64)
    lst = [1, 2, 4, 7, 6, 5, 8, 13, 11]
    result_lst = get_longest_powers_of_k(lst,1)
    assert (result_lst[0] == 1)
    assert (result_lst[1] == 2)
    assert (result_lst[2] == 4)
    assert (result_lst[3] == 7)
    assert (result_lst[4] == 6)
    assert (result_lst[5] == 5)
    assert (result_lst[6] == 8)
    assert (result_lst[7] == 13)
    assert (result_lst[8] == 11)




def main():
    '''
    Meniul pentru utilizator.
    '''
    lista_goala = False
    lst = []
    while True:
        print('1.   Citire date.')
        print('2.   Determinare cea mai lungă subsecvență cu proprietatea ca numerele sunt palindromuri.')
        print('3.   Determinare cea mai lungă subsecvență cu proprietatea ca numerele sunt egale cu un numar oarecare la o putere data.')
        print('4    Ieșire.')
        optiune = input("Alege optiunea:")
        if optiune == '1':
            lst = citire_date()
            lista_goala = True
        elif optiune == '2':
            if lista_goala == False:
                print('Lista este goala.Selectati optiunea 1 pentru a introduce date.')
            else:
                print(get_longest_all_palindromes(lst))
                test_get_longest_all_palindromes()
        elif optiune == '3':
            if lista_goala == False:
                print('Lista este goala.Selectati optiunea 1 pentru a introduce date.')
            else:
                k = int(input('Intorudceti puterea:'))
                print(get_longest_powers_of_k(lst,k))
                test_get_longest_powers_of_k()
        elif optiune == '4':
            break
        else:
            print('Optiune invalida.')


main()
