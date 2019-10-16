from sys import argv
from mail import Mail as ml
from update import UpdateDBS as udbs
from insert import Insert as ins

def main():
    desciption="""
    Amazon Price Trace
    Note:
        python main.py url http://www.amazon.in/7gyyf6ft/0-ji/9yui-9
        python main.py update
        python main.py show
        python main.py  email
    """


    if len(argv)==1:
        print(desciption)
    elif argv[1]=='url':
        if len(argv)==2:
            print('Please provide link')
        else:
            #! Link checking process
            if argv[2][:21]=='https://www.amazon.in':
                i=ins(argv[2])
                i.controller()
            else:
                print('Your Link Is Invalid',argv[2][:20])
    elif argv[1]=='update':
        #! Update
        u=udbs()
        u.update()
    elif argv[1] == 'show':
        #! To show database 
        u=udbs()
        u.get_tables()
    elif argv[1]=='email':
        #! Email details check 
        m=ml()
        m.checkInfo()
    else:
        print('Invalid')
        print(desciption)

if __name__ == "__main__":
    main()