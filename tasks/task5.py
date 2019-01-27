from dateutil import parser

#date = input("Enter your date:")


def check_my_date(date):
   try:
       str(parser.parse(date))
       return True
   except ValueError:
       return False


#print(check_my_date(date))

