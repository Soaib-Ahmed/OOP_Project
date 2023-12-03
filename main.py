from menu import Pizza,Burger,Drinks,Menu
from Restaurant import Restaurant
from users import Chef,Customer,Server,Manager
from order import Order

def main():
    menu=Menu()
    pizza_1 = Pizza('ameer pizza',200,'large',['aam','lebo'])
    menu.add_menu_item('pizza',pizza_1)
    pizza_2 = Pizza('komola pizza',600,'small',['komola','tetol'])
    menu.add_menu_item('pizza',pizza_2)
    pizza_3 = Pizza('kotkoti pizza',800,'xxxl',['kotkoti','amm'])
    menu.add_menu_item('pizza',pizza_3)

    burger_1=Burger('Kola',220,'Goru',['kacha kola','morich'])
    menu.add_menu_item('burger',burger_1)
    burger_2=Burger('Goat',220,'goat',['boro chagol','ada'])
    menu.add_menu_item('burger',burger_2)

    drinks_1=Drinks('coke',50,True)
    menu.add_menu_item('drinks',drinks_1)
    drinks_2=Drinks('7up',50,True)
    menu.add_menu_item('drinks',drinks_2)

    menu.show_menu()

    restaurant =Restaurant('Seaum_baba Restuarant',2000,menu)

    manager=Manager('abir',3433,'abir@gmail.com','Adalot',30000,'jan 23 2020','cashiar')
    restaurant.add_employee('manager',manager)

    chef=Chef('Pial','0239434','pial@gmail.com','chortha',22222,'jan 23 0202','kataktai','bortha')
    restaurant.add_employee('chef',chef)

    server=Server('Mridul','23948320','mridul2gmaol.com','chadpur',3000,'Feb 23 2022','Washing')
    restaurant.add_employee('server',server)

    restaurant.show_employee()

    #customer
    customer_1=Customer('Seaum','92938','seaum2gmaol.com','Dolipara',23433)

    order_1 = Order(customer_1,[pizza_1,burger_1,drinks_1,pizza_3])
    customer_1.pay_for_order(order_1)
    restaurant.add_order(order_1)

    #paying order
    restaurant.receive_payment(order_1,5000,customer_1)

    print(restaurant.revenue,restaurant.balance)

    #pay rent
    restaurant.pay_expense(restaurant.rent,'rent')
    print(restaurant.revenue,restaurant.balance)

    restaurant.pay_salary(chef)
    print(restaurant.revenue,restaurant.balance)

if __name__ == '__main__':
    main()