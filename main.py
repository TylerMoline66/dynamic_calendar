import cal
import num_check

the_month = input('input what month you want to check(please use the number): ')
the_year = input('input what year you want to check(after 1703): ')

num_check.do_a_thingy(the_year)
num_check.do_a_thingy(the_month)

the_year = num_check.do_a_thingy(the_year)
the_month = num_check.do_a_thingy(the_month)


cal.print_month_cal(the_month, the_year)