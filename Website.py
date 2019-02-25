# Not-a-sopository(Sign up)
#build log for sign up web page
#ver1.1 - Created test data for ticket variable
#ver1.2 added server functionality to python

from bottle import run, route, view, get, post, request
from itertools import count


class Ticket: #class is an object which holds information
    # _ signifies a private variable, not to be used outside of this class
    _ids = count(0)
    
    def __init__(self, name, email, date_of_birth, check_in):
        #not passing ID as we want it to create it
        self.id = next(self._ids)
        self.name = name
        self.email = email
        self.dob = date_of_birth
        self.check_in = check_in
    


#test data
tickets =[Ticket("Jakob Schulz", "jakobschulz@email.com","20.02.2003",False),
          Ticket("John Connner","Terminator@email.com","12.12.2012",False),
          Ticket("John Cena","Invisible@email.com","01.01.1991",False),
          Ticket("John Wick","HisDog@email.com","06.09.1969",False)]



#pages
#index page
@route("/")
@view("index")
def index():
    #need this function to attach the decorators above
    pass
     

@route('/check-in')
@view('check-in')
def check_in():
    data = dict (ticket_list = tickets)
    return data




run(host ='0.0.0.0', port = 8080, reloader = True, debug = True)
