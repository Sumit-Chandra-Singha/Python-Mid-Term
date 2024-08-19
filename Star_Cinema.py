class Star_Cinema:
    hall_list = []
    def entry_hall(self,hall): 
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self.rows = rows
        self.cols = cols
        self.__hall_no = hall_no
        
    def entry_show(self, id, movie_name, time):
        show = (id,movie_name,time)
        self._show_list.append(show)
        for i in range(self.rows):
            for j in range(self.cols):
                self._seats[id,i,j]=0
        
    def view_show_list(self):
        print('----------------')
        for show in self._show_list:
            print(f"MOVIE NAME: {show[1]}({show[0]}) SHOW ID: {show[0]} TIME: {show[2]}")
        print('----------------')
    
    def view_available_seats(self, id):
        for s in self._show_list:
            if id == s[0]:
                print()
                for i in range(self.rows):
                    print(end='[ ')
                    for j in range(self.cols):
                        print(f'{self._seats[id,i,j]}',end=' ')
                    print(']')
                return
        print('\nNO SHOW AVAILABLE.')

    def book_seats(self, id, seat):
        for s in self._show_list:
            if id == s[0]:
                row,col = seat
                if 0<row<=self.rows and 0<col<=self.cols:
                    if self._seats[id,row-1,col-1]==0:
                        self._seats[id,row-1,col-1]=1
                        print(f"\nSEAT ({row},{col}) IS BOOKED FOR YOU.")
                    else:
                        print("\nSEAT IS ALREADY BOOKED.")
                else:
                    print("\nINVALID SEAT.")  
                return
        
        print("\nSHOW IS NOT AVAILABLE.")
    
StarCinema = Star_Cinema()
hall = Hall(5,10,1)
StarCinema.entry_hall(hall)
hall.entry_show(1,"Iron Man","14:07:24 12:00 PM")
hall.entry_show(2,"Iron Man 2","14:07:24 5:00 PM")
hall.entry_show(3,"Iron Man 3","14:07:24 9:00 PM")

while True:
    print('\n1. VIEW ALL SHOW TODAY.')
    print('2. VIEW AVAILABLE SEATS.')
    print('3. BOOK TICKET.')
    print('4. EXIT.')

    option = int(input('\nENTER OPTION: '))

    if option == 1:
        hall.view_show_list()
    elif option == 2:
        id = int(input("ENTER SHOW ID: "))
        hall.view_available_seats(id)
    elif option == 3:
        id = int(input('ENTER SHOW ID: '))
        row = int(input('ENTER ROW NO: '))
        col = int(input('ENTER COLUMN NO: '))
        hall.book_seats(id,(row,col))
    elif option == 4:
        break
    else:
        print("\nINVALID OTION !!!")
        
