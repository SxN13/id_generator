import sys
from array import array

latin_alph = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' ]
russi_alph = [ 'а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я' ]
        
def weigth(st):
    we = 0
    for i in range(len(st)):
        for j in range(len(russi_alph)):
            if (st[i] == russi_alph[j]):
                we +=j+1;
    return we

def abriveature(f, s):
    kb = weigth(f) % len(latin_alph)
    kb1 = weigth(s) % len(latin_alph)
    st = latin_alph[kb - 1] + latin_alph[kb1 - 1]
    return st.upper();
    
def lite_path(f, s, t):
    lp = 0
    for i in range(len(russi_alph)):
        if (f[0] == russi_alph[i]):
            lp += i + 1
        if (s[0] == russi_alph[i]):
            lp += i + 1
        if (t[0] == russi_alph[i]):
            lp += i + 1
    return lp

def full_path(f, s, t):
    fp = weigth(f) + weigth(s) + weigth(t)
    return fp

def constructor_id(f, s, t):
    st = abriveature(f, s) + "-" + str(full_path(f, s, t)) + "-" + str(lite_path(f, s, t))
    return st

fn = sys.argv[1]
sn = sys.argv[2]
tn = sys.argv[3]

print("\nФамилия: \t" , fn)
print("Имя: \t\t" , sn)
print("Отчество: \t" , tn)

print("Вычисленный id: ",constructor_id(fn.lower(), sn.lower(), tn.lower()))

