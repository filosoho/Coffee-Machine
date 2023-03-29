# Coffee-Machine
This project simulates a coffee machine with an interactive command-line interface. It allows the user to select a drink, insert coins, and receive their drink, along with the change. The application prompts users to insert coins to pay for their drink and calculates the change. It also checks whether there are enough resources to make the selected drink and provides an error message if not.

# Prerequisites  
~~~
Python 3.x
~~~

# Usage
To run the program, simply run:
~~~
main.py
~~~  

Once running, the program will prompt the user to select from one of the following options:  

* To order a drink:  "espresso", "latte", or "cappuccino".  

Hidden options:  
* To get a report on the machine's resources, type "report".  
* To turn off the machine, type "off".  

They can then select a drink, insert coins, and receive their drink and change. The program will check if there are enough resources to make the drink, and if there is enough money inserted to cover the cost.  

The program also has a "report" feature which displays the current state of the resources and the profit. This feature can be accessed by typing "report" in the terminal.    
  
~~~
  

                         )))
                        (((
                      +-----+
                      |     |]
                      `-----'    
                    ___________
                    `---------'

    ╔═╗┌─┐┌─┐┌─┐┌─┐┌─┐  ╔╦╗┌─┐┌─┐┬ ┬┬┌┐┌┌─┐
    ║  │ │├┤ ├┤ ├┤ ├┤   ║║║├─┤│  ├─┤││││├┤ 
    ╚═╝└─┘└  └  └─┘└─┘  ╩ ╩┴ ┴└─┘┴ ┴┴┘└┘└─┘                                                                    

 What would you like? (espresso/latte/cappuccino): report
==============================================================
    Water: 1200ml
    Milk: 400ml
    Coffee: 100g
    Money: $0
==============================================================
 What would you like? (espresso/latte/cappuccino): espresso
==============================================================
Please insert coins. 💰
==============================================================
how many quarters?: 8
how many dimes?: 8
how many nickles?: 6
how many pennies?: 4
==============================================================
Here is $1.64 in change. 👛
==============================================================
           
                     c[_]
        
    Here is your espresso (っ˘ڡ˘ς)☕️. Enjoy! 😋
==============================================================
 What would you like? (espresso/latte/cappuccino): report
==============================================================
    Water: 1150ml
    Milk: 400ml
    Coffee: 82g
    Money: $1.5
==============================================================
 What would you like? (espresso/latte/cappuccino): latte
==============================================================
Please insert coins. 💰
==============================================================
how many quarters?: 10
how many dimes?: 10
how many nickles?: 2
how many pennies?: 2
==============================================================
Here is $1.12 in change. 👛
==============================================================
               
                    ((((
                     ))))
                  _ .---.
                 ( |`---'|
                  \|     |
                  : .___, :
                   `-----'
        
    Here is your latte (っ˘ڡ˘ς)☕️. Enjoy! 😋
==============================================================
 What would you like? (espresso/latte/cappuccino): cappuccino
==============================================================
Please insert coins. 💰
==============================================================
how many quarters?: 10
how many dimes?: 10
how many nickles?: 5
how many pennies?: 5
==============================================================
Here is $0.8 in change. 👛
==============================================================

                   _..,----,.._
                .-;'-.,____,.-';
               (( |            |
                `))            ;
                 ` \          /
                .-' `,.____.,' '-.
               (     '------'     )
                `-=..________..--'
        
    Here is your cappuccino (っ˘ڡ˘ς)☕️. Enjoy! 😋
==============================================================
 What would you like? (espresso/latte/cappuccino): report
==============================================================
    Water: 700ml
    Milk: 150ml
    Coffee: 34g
    Money: $7.0
==============================================================
 What would you like? (espresso/latte/cappuccino): latte
==============================================================
Please insert coins. 💰
==============================================================
how many quarters?: 8
how many dimes?: 8
how many nickles?: 8
how many pennies?: 8
==============================================================
Here is $0.78 in change. 👛
==============================================================
               
                    ((((
                     ))))
                  _ .---.
                 ( |`---'|
                  \|     |
                  : .___, :
                   `-----'
        
    Here is your latte (っ˘ڡ˘ς)☕️. Enjoy! 😋
==============================================================
 What would you like? (espresso/latte/cappuccino): report
==============================================================
    Water: 500ml
    Milk: 0ml
    Coffee: 10g
    Money: $9.5
==============================================================
 What would you like? (espresso/latte/cappuccino): latte
==============================================================
     Sorry there is not enough milk. 🥛
==============================================================
 What would you like? (espresso/latte/cappuccino): espresso
==============================================================
     Sorry there is not enough coffee. (っ-,-)つ☕
==============================================================
 What would you like? (espresso/latte/cappuccino): off  
 
 ~~~
   
 # Contributing
If you would like to contribute to this program, feel free to submit a pull request. Please include a detailed description of the changes made and the reasons for the changes.

# License
Feel free to use and modify the code as per your requirements.
