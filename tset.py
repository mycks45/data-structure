pin_code =int(input('Enter a pin'))

if pin_code > 100000 and pin_code < 999999:
    pinStr= str(pin_code)
    length = len(pinStr)
    i=0
    while i < (length-2):
        if pinStr[i] == pinStr[i+2]:
            res='False'
            break
        else:
            res='true'
        i += 1
    print(res)
else:
    print('enter the number between 100000 and 999999')