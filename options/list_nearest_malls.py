from options.num import OptionsNum
from utils import get_loc, parse_shoppingmall_data, distance

def text():
    return f'{OptionsNum.LIST_NEAREST_MALLS.value}. List nearest malls from location.'
    
    
def execute():
    loc = get_loc()
    
    if loc is None:
        print("Unable to get location.\n")
        return
    else:
        lat, long = loc
        
        shops = parse_shoppingmall_data()
        shops['Distance'] = shops.apply(lambda shop: distance(lat, long, float(shop['LATITUDE']), float(shop['LONGITUDE'])), axis=1)
        shops_sorted = shops.sort_values(by='Distance')
        
        s = f"{'Mall':<40} {'Distance (KM)'}"
        print(s)
        print("-"*len(s))
        for _, row in shops_sorted[['Mall', 'Distance']][1:11].iterrows():
            print(f"{row['Mall']:<40} {row['Distance']}")
       


