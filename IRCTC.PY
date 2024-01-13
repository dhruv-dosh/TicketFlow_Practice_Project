import time

class Irctc: 
    def __init__(self,name,seats,price,pnr):
        self.price = price
        self.name = name
        self.seats =seats
        self.pnr=pnr

    def traininfo(self):
        print(f'name of train is {self.name}')    
        print(f'price of ticket is {self.price}')    
        print(f'no of seats in train is {self.seats}')    
        
    def bookticket(self):
            print('Hey please fill up the form')
            name=input('Enter your name :')
            while " " in name:
                print('Enter your name without space')
                name=input('Enter your name :')

            age=int(input('Enter your Age :'))
            while age < 10 or age > 110:
                print('Invalid age')
                age=int(input('Enter correct Age :'))

            number=input('Enter your Number :')
            while len(number) > 10 or len(number)< 10:
                print('Incorrect number')
                number=input('Enter Number again:')
            
            if (self.seats>0):
                payment=input('Confirm payment :')
                while 'cnf'!= payment:
                    print('Enter cnf to confirm')
                    payment=input('Confirm payment :')

                bookingtime = time.asctime(time.localtime())
                print('your ticket has been booked successfully')

                print(f'your seat no. is {self.seats}')
                list_of_seats=[]
                list_of_seats.append(self.seats)
                print(list_of_seats)
                self.seats=self.seats - 1

                print(f'your pnr no. is {self.pnr}')
                self.pnr=self.pnr- 1
                
                if payment == 'cnf':
                    status = 'booked'

                info=f"{name},{age},{number},{frm},{to},{payment},{bookingtime},{self.seats},{self.pnr}"
                with open('infop/passanger1.txt','a') as w:
                    w.write(f"{status},{self.name},{info}  \n")
            
            else:
                print('This train is bookes please try in tatkal!')


if __name__=="__main__":        
        intersity = Irctc('intersity_express : 90161',100,400,90161122100)
        indore_daund = Irctc('indore_daund_express : 19062',100,500,19062122100)
        Rajdhani = Irctc('Ranjdhani_express : 22062',100,600,22062122100)

        print('*******WELCOME TO IRCTC********')
 
        it = ['bahraich','payagpur','ayodhya','jaunpur','varanasi']
        i_d = ['daund','pune','lonavla','surat','vadodra','indore']
        raj = ['sealdah','durgapur','asansol','kanpur','delhi']
    
        print('''OPTIONS ARE :
        [bahraich - payagpur - ayodhya - jaunpur - varanasi]
        [daund - pune - lonavla - surat - vadodra - indore]
        [sealdah - durgapur - asansol - kanpur - delhi]'''
        )
        frm =input('From :')
        to =input('To :')
        tn = 'xyz'
        if frm in it and to in it:
            while frm == to:
                print('Invalid destination') 
                to =input('Enter valid destination :')

            tn = 'intersity'

        elif frm in i_d and to in i_d:
            while frm == to:
                print('Invalid destination')
                to =input('Enter valid destination :') 

            tn = 'ind_daund'

        elif frm in raj and to in raj:
            while frm == to:
                print('Invalid destination')
                to =input('Enter valid destination :')

            tn = 'rajdhani'

        else:
            print('This station is not in range')

    
        number_of_ticket= int(input("Enter number of tickets you want :"))
    
        while number_of_ticket > 0:
            if ('intersity' is tn):
                print(f'Your train name is intersity express')
                intersity.bookticket()
                number_of_ticket=number_of_ticket-1
            elif('ind_daund' is tn):
                print(f'Your train name is indore_daund express')
                indore_daund.bookticket()
                number_of_ticket=number_of_ticket-1
            elif('rajdhani' is tn):
                print(f'Your train name is rajdhani express')
                Rajdhani.bookticket()
                number_of_ticket=number_of_ticket-1
            else:
                print('no train found')    
                break

        exit=input('Enter to exit :')
        if('ok'in exit):
            exit()






