from decrypting_case import *

s = Security()

t1 = s.form_task_1(5000)

print(t1[0])
print(t1[1])

def decrypt(string):
    out = ""
    for x in string:
        if x in "qwertyuiopasdfghjklzxcvbnm1234567890":
            out += x

    return out

dec = decrypt(t1[0])

print(dec)


def mix_elements(into):
    into = into
    out = ""
    odd = [into[i] for i in range(0, len(into)) if i % 2 == 0]
    even =[into[i] for i in range(0, len(into)) if i % 2 != 0]
    for x in range(0, max(len(even), len(odd))):
        try:
            out = out + even[x] + odd[x]
        except:
            try:
                out += odd[x]
            except:
                try:
                    out += even[x]
                except:
                    pass
    return out

print(mix_elements(dec))