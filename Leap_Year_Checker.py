#This checks if a year is a leap year

year_in_question = int(input("Enter a year to check: "))
div_4 = year_in_question % 4
div_100 = year_in_question % 100
div_400 = year_in_question % 400


def check_leap(year_in_question, div_4, div_100, div_400):
    if div_4 == 0:
        if div_100 != 0:
            return True
        if div_100 == 0 and div_400 == 0:
            return True
        else:
            return False

    if div_4 != 0:
        return False



check_leap(year_in_question, div_4, div_100, div_400)

print(check_leap(year_in_question, div_4, div_100, div_400))