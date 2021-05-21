import datetime

def inputs():
    try:
        print('\nWelcome To the NIS CHECKER\n'+'='*20)
        kelas = input('Input the class : ').lower().split()
        kelas_x = ''.join(kelas)

        # if kelas is number
        if kelas_x.isdigit() == True:
            print('OUTPUT'.center(20, '=')+'\nPlease input class correctly!')
            inputs()
     
        absen = int(input('='*20+'Input the attendee\'s number : '))
        print('OUTPUT'.center(20, '='))

        if kelas_x == 'xmipa1':
            data = []
            n = 202110001
            while n <= 202110035:
                data.append(n)
                n += 1
            print('Your nis is',data[absen-1])

        elif kelas_x == 'xmipa2':
            data = []
            n = 202110036
            while n <= 202110071:
                data.append(n)
                n += 1
            print('Your NIS is',data[absen-1])
            
        elif kelas_x == 'xmipa3':
            data = []
            n = 202110072
            while n <= 2021100107:
                data.append(n)
                n += 1
            print('Your NIS is',data[absen-1])
            
        elif kelas_x == 'xmipa4':
            data = []
            n = 202110108
            while n <= 202110143:
                data.append(n)
                n += 1
            print('Your NIS is',data[absen-1])
            
        elif kelas_x == 'xmipa5':
            data = []
            n = 202110144
            while n <= 202110179:
                data.append(n)
                n += 1
            print('Your NIS is',data[absen-1])
            
        elif kelas_x == 'xmipa6':
            data = []
            n = 202110180
            while n <= 202110215:
                data.append(n)
                n += 1
            print('Your NIS is',data[absen-1])
            
        elif kelas_x == 'xmipa7':
            data = []
            n = 202110216
            while n <= 202110251:
                data.append(n)
                n += 1
            print('Your NIS is',data[absen-1])

        elif kelas_x == 'xmipa8':
            data = []
            n = 202110252
            while n <= 202110287:
                data.append(n)
                n += 1
            print('Your NIS is',data[absen-1])

        elif kelas_x == 'xips1':
            data = []
            n = 202110288
            while n <= 202110323:
                data.append(n)
                n += 1
            print('Your NIS is',data[absen-1])

        elif kelas_x == 'xips2':
            data = []
            n = 202110324
            while n <= 202110359:
                data.append(n)
                n += 1
            print('Your NIS is',data[absen-1])

        elif kelas_x == 'xips3':
            data = []
            n = 202110360
            while n <= 202110395:
                data.append(n)
                n += 1
            print('Your NIS is',data[absen-1])

        elif kelas_x == 'xips4':
            data = []
            n = 202110396
            while n <= 202110431:
                data.append(n)
                n += 1
            print('Your NIS is',data[absen-1])

        else:
            print('There is no data! Please input again.')
            inputs()

    #Attendee's number isn't more than 36
    except IndexError:
        print("Attendee's number is not more than 36! Please input again.")
        inputs()

    except ValueError:
        print('\nPlease input the attendee\'s number with a number')
        inputs()
    finally:
        x = datetime.datetime.now().strftime('%I:%M %p, %d/%m/%Y')
        print('\nThank you for using this program\nYou access this website at',x)
        inputs()
        
inputs()
