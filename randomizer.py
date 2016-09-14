import random,sys

fourth = ['Ayman', 'Shaeq', 'Patrick', 'Yvonne', 'Wilson','Brian', 'Farhan', 'Janet', 'Harry', 'Kevin','Nicholas', 'Jason', 'Yikai', 'Emma', 'Kenneth','Nala', 'Karol', 'Elias', 'Ely', 'Reo', 'Dhriaj','Amy', 'Arvind', 'Nobel', 'Angela', 'Edward','Jonathan', 'Celine', 'Daniel', 'Lindsey', 'Ziyan', 'Elina']

eighth = ['Julian', 'Sebastian', 'Jordan', 'Alan', 'Yuki','Chloe', 'Noah', 'Edvic', 'Jia Qi', 'Shan', 'Rodda','Anya', 'Edmond', 'Asher', 'Kathy', 'Sharon', 'Vncent','Lawrence', 'Sachal', 'Gabriel', 'Jason', 'Daniel','Felix', 'Jacob', 'Bayle', 'Fortune', 'Gio','Kelly', 'William', 'Jordan', 'Haley', 'Henry']

nineth = ['James', 'Vanna', 'Zicheng', 'Quinn', 'Anthony C','Joel', 'Steph', 'Xinhui', 'Richard', 'Misha','Maddie', 'Winston', 'Shariar', 'Nancy', 'Jerry','Michael', 'Stiven', 'Will',  'Olivia', 'Constantine','Jessica', 'Kate', 'Shamaul', 'Max', 'Sarah', 'Anthony L','Brandon', 'Nicole', 'Brian', 'Issac', 'Seiji', 'Lorenz']

def randNum(var):
    if var == '4' :
        num = random.random() * len(fourth)
    elif var == '8' :
        num = random.randrange(0,len(eighth))
    elif var == '9' :
        num = random.randrange(0,len(nineth))
    else:
        num = 0
    return int(num)

def printName():
    classNum = sys.argv[1]
    pos = randNum(classNum)
    if pos == '0':
        print("Class entered does not exist")
    elif classNum == '4':
        print(fourth[pos])
    elif classNum == '8':
        print(eighth[pos])
    elif classNum == '9':
        print(nineth[pos])
    return

printName()

            
