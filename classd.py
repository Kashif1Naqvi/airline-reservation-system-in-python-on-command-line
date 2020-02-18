class Flight:
    """ A Flight with particular passenger in aircraft """
    def __init__(self,number,aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"code is invaild  '{number}' ")
        if not number[2:].isdigit():
            raise ValueError(f"code digit is invalid {number} ")
        if not (number[2:].isdigit()  and int(number[2:]) <= 9999 ) :
            raise ValueError(f"Ivaild route number")
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{ letter : None for letter in seats} for _ in rows ]
    def number(self):
        return self.number
    def airline(self):
        return self.number[:2]
    def aircraft_model(self):
        return self._aircraft.model()
    def allocate_seat(self,seat,passenger):
        """
            Allocate a seat to  a passenger
                Args:
                    seat: A seat designer such as '12C' or '21F'
                    passenger: the passenger name
                Raises:
                    ValueError: if seat is not AVAIABLE
        """
        row , letter = self._parse_seat(seat)
        if self._seating[row][letter] is not None:
            raise ValueError(f"seat {seat} Already occupied! ")
        self._seating[row][letter] = passenger
    def _parse_seat(self,seat):
        rows , seat_letters = self._aircraft.seating_plan()
        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f"invaild seat letter {letter} ")
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"invaild  seat row {row_text}  ")
        if row not in rows:
            raise ValueError(f"invaild row number {row}  ")
        return row,letter
    def relocate_passenger(self,from_seat,to_seat):
        """
            Relocate the passenger to a diffrent seats
            Args:
                from_seat : The existing seat designator for the passenger to be moved
                to_seat   : The new seat designer.
        """
        from_row,from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is  None:
            raise ValueError(f"No Passenger to relocate in seat {from_seat} ")
        to_row , to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f"Seat {to_seat} Alread occupied! ")
        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None
    def num_avaiable_seats(self):
        return sum(sum(1 for s in row.values() if s is None )
            for row in self._seating
            if row is not  None
        )
    def make_boarding_cards(self,card_printer):
        for passenger,seats in sorted(self._passenger_seats()):
            card_printer(passenger,seats,self._number,self.aircraft_model())
    def _passenger_seats(self):
        """an iterable series of passenger"""
        row_number,seat_letters = self._aircraft.seating_plan()
        for row in row_number:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield(passenger,f"{row}{letter}")

# f = Flight('A11S','any')
# print(f._number)
# senario is in plan total seats is base of ABCDEFGHIJK  IN EVERY ROW 6 SEATS AVAIABLE

"""
class Aircraft:
    def __init__(self,registration,model,num_rows,num_seats_per_row):
        self._registration      = registration
        self._model             = model
        self._num_rows          = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1,self._num_rows + 1),'ABCDEFGHIJK'[:self._num_seats_per_row])
"""
# now convert above Aircraft class to polymorphism way
# so by using inheritance

class Aircraft:
    def __init__(self,registration):
        self._registration = registration
    def registration(self):
        return self._registration
    # def num_seats(self):
    #     rows, row_seats = self.seating_plan()
    #     return len(rows) * len(row_seats)
class AirbusA319(Aircraft):
    """
    when use inheritance also code show more clean remove doublicate from classes
    def __init__(self,registration):
        self._registration = registration
    def registration(self):
        return self._registration
    """
    def model(self):
        return "Airbus A319"
    def seating_plan(self):
        return range(1,23),'ABCDEF'

class Boeing777(Aircraft): # it's inheritance
    """
    def __init__(self,registration):
        self._registration = registration

    def registration(self):
        return self._registration
    """
    def model(self):
        return "Boeing777"

    def seating_plan(self):
        # For simplicity's we ignore complex
        # seating arragment for first class
        return range(1,56) , 'ABCDEFGHIJK'





# a = Aircraft('dc12','S3544',num_rows=22,num_seats_per_row=6)
# print(f"Aircraft model is {a._model} and Registration no is {a._registration}")

"""


b = Flight('BA758',Aircraft('G-EUPT','Airbus A319',num_rows=22,num_seats_per_row=6))


"""
#
# print(b.aircraft_model())
# print(b._seating)
from pprint import pprint as pp
def make_flight():
    """
    f = Flight('BA758',Aircraft('G-EUPT','Airbus A319',num_rows=15,num_seats_per_row=6))
    f.allocate_seat("2A","Allama Mohsin naqvi")
    f.allocate_seat("2B","Ali Naqvi")
    f.allocate_seat("1A","Sir Syed Murtza")
    f.allocate_seat("1B","Kashif Naqvi")
    f.allocate_seat("1C","Hassnain Naqvi")
    f.allocate_seat("1E","Sulman Naqvi")
    f.allocate_seat("1F","haider Naqvi")
    f.allocate_seat("12A","Guido van Rossum")
    f.allocate_seat("12B","Kashif naqvi")
    f.allocate_seat("13C","Kashif naqvi") """

    f = Flight('BA758',AirbusA319('G-EUPT'))
    f.allocate_seat("2A","Allama Mohsin naqvi")
    f.allocate_seat("2B","Ali Naqvi")
    f.allocate_seat("1A","Sir Syed Murtza")
    f.allocate_seat("1B","Kashif Naqvi")
    f.allocate_seat("1C","Hassnain Naqvi")
    f.allocate_seat("1E","Sulman Naqvi")
    f.allocate_seat("1F","haider Naqvi")
    f.allocate_seat("12A","Guido van Rossum")
    f.allocate_seat("12B","Kashif naqvi")
    f.allocate_seat("13C","Kashif naqvi")

    g = Flight('AF72',Boeing777('F-GSPS'))

    g.allocate_seat("55K","Muzamil zaidi")
    g.allocate_seat("33G","Sadaif rizvi")
    g.allocate_seat("4B","Hizqeel zaidi ")
    g.allocate_seat("11B","Mubasir rizvi")
    g.allocate_seat("11C","Asad")

    return f,g
f,g = make_flight()

# data = AirbusA319('G-EUPT')
# print(f"data {data.num_seats()} ")


def console_card_printer(passenger,seat,flight_number,aircraft):
    output = f" | Name: {passenger} " \
             f" Flight  {flight_number}  " \
             f" seat {seat} " \
             f" Aircraft {aircraft} " \
             "|"
    banner = "+" + "-" * (len(output) -2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"
    lines  = [banner,border,output,border,banner]
    card   = "\n".join(lines)
    print(card)
    print()
print(f.relocate_passenger("2B","3A"))
print(f.relocate_passenger("1A","2D"))
print(g.relocate_passenger("11B","1C"))
# print(pp(f._seating))
print("avaiable seats for f:=>",f.num_avaiable_seats())
print(g.make_boarding_cards(console_card_printer)) # #see this line bellow output
"""
                                                +----------------------------------------------------------+
                                                |                                                          |
                                                 | Name: Asad  Flight  AF72   seat 11C  Aircraft Boeing777 |
                                                |                                                          |
                                                +----------------------------------------------------------+

                                                +-------------------------------------------------------------------+
                                                |                                                                   |
                                                 | Name: Hizqeel zaidi   Flight  AF72   seat 4B  Aircraft Boeing777 |
                                                |                                                                   |
                                                +-------------------------------------------------------------------+

                                                +------------------------------------------------------------------+
                                                |                                                                  |
                                                 | Name: Mubasir rizvi  Flight  AF72   seat 1C  Aircraft Boeing777 |
                                                |                                                                  |
                                                +------------------------------------------------------------------+

                                                +-------------------------------------------------------------------+
                                                |                                                                   |
                                                 | Name: Muzamil zaidi  Flight  AF72   seat 55K  Aircraft Boeing777 |
                                                |                                                                   |
                                                +-------------------------------------------------------------------+

                                                +------------------------------------------------------------------+
                                                |                                                                  |
                                                 | Name: Sadaif rizvi  Flight  AF72   seat 33G  Aircraft Boeing777 |
                                                |                                                                  |
                                                +------------------------------------------------------------------+
"""
print("avaiable seats for g :=>",g.num_avaiable_seats())
print(f.make_boarding_cards(console_card_printer)) #see this line bellow output
"""
                                                +-----------------------------------------------------------------+
                                                |                                                                 |
                                                 | Name: Ali Naqvi  Flight  BA758   seat 3A  Aircraft Airbus A319 |
                                                |                                                                 |
                                                +-----------------------------------------------------------------+

                                                +---------------------------------------------------------------------------+
                                                |                                                                           |
                                                 | Name: Allama Mohsin naqvi  Flight  BA758   seat 2A  Aircraft Airbus A319 |
                                                |                                                                           |
                                                +---------------------------------------------------------------------------+

                                                +-------------------------------------------------------------------------+
                                                |                                                                         |
                                                 | Name: Guido van Rossum  Flight  BA758   seat 12A  Aircraft Airbus A319 |
                                                |                                                                         |
                                                +-------------------------------------------------------------------------+

                                                +----------------------------------------------------------------------+
                                                |                                                                      |
                                                 | Name: Hassnain Naqvi  Flight  BA758   seat 1C  Aircraft Airbus A319 |
                                                |                                                                      |
                                                +----------------------------------------------------------------------+

                                                +--------------------------------------------------------------------+
                                                |                                                                    |
                                                 | Name: Kashif Naqvi  Flight  BA758   seat 1B  Aircraft Airbus A319 |
                                                |                                                                    |
                                                +--------------------------------------------------------------------+

                                                +---------------------------------------------------------------------+
                                                |                                                                     |
                                                 | Name: Kashif naqvi  Flight  BA758   seat 12B  Aircraft Airbus A319 |
                                                |                                                                     |
                                                +---------------------------------------------------------------------+

                                                +---------------------------------------------------------------------+
                                                |                                                                     |
                                                 | Name: Kashif naqvi  Flight  BA758   seat 13C  Aircraft Airbus A319 |
                                                |                                                                     |
                                                +---------------------------------------------------------------------+

                                                +-----------------------------------------------------------------------+
                                                |                                                                       |
                                                 | Name: Sir Syed Murtza  Flight  BA758   seat 2D  Aircraft Airbus A319 |
                                                |                                                                       |
                                                +-----------------------------------------------------------------------+

                                                +--------------------------------------------------------------------+
                                                |                                                                    |
                                                 | Name: Sulman Naqvi  Flight  BA758   seat 1E  Aircraft Airbus A319 |
                                                |                                                                    |
                                                +--------------------------------------------------------------------+

                                                +--------------------------------------------------------------------+
                                                |                                                                    |
                                                 | Name: haider Naqvi  Flight  BA758   seat 1F  Aircraft Airbus A319 |
                                                |                                                                    |
                                                +--------------------------------------------------------------------+
"""
