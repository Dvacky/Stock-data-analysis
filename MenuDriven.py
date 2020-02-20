import func_set

while True :
    print('******STOCK ANALYSIS******')
    print('='*40)
    print('Choose your  option :\n')
    print('1. GENERATE COMPLETE REPORT(YEARWISE )')
    print('2. GENERATE REPORT FOR PARTICULAR CHOICE')
    print('3. GENERATE DATE-WISE REPORT')
    print('4. EXIT')
    choice = int(input('Enter your choice : '))
    if choice == 1:
        cmplt_report = func_set.complete_report()
        print('*'*40)
        print(cmplt_report)
        print('*' * 40)
    if choice == 2:
        show = func_set.show_options()
        print('*' * 40)
        print(show)
        print('*' * 40)
        display = func_set.show_data(show)
        print(display)
    if choice ==3:
        show_date = func_set.Date_wise()
    if choice==4:
        print('Thank You ..!!!')
        break





