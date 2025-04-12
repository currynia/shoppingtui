from options.num import OptionsNum
from utils import parse_shoppingmall_data


def text():
    return f'{OptionsNum.LIST_ALL_MALLS.value}. List all malls in Singapore.'

def execute():
    df = parse_shoppingmall_data()
  
    print("1.North\n2.South\n3.East\n4.West\n5.Central\n")
    inp = input("Enter number: ")
    try:
        inp = int(inp)
        print("\n")

        loc = None
        if inp == 1:
           loc = 'North'
        elif inp == 2:
            loc = 'South'
        
        elif inp == 3:
            loc = 'East'
       
        elif inp == 4:
            loc = 'West'

        elif inp == 5:
            loc = 'Central'
           
        else:
            print("Enter a valid number!\n")
            
        if loc is not None:
            s = f"{loc} Malls"
            print(s)
            print("-"*len(s))
            for _, row in df[df["Region"] == loc].iterrows():
                print(f"{row['Mall']}")

    except Exception as e:
         
         print("Enter a valid number!\n")
    return
