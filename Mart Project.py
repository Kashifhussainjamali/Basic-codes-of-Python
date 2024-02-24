class Mart:
 print("****SUPER MART****")
 print('''1: Grosery
2: Vegetable
3: Fruits
4: Electronic Machines
5: Drinks
6: Bill''')

 def grosery(self):
   self.price_list=""
   self.price_1=0
   print({"Grosery":{"1: Fog Body Spray":"RS 700",
                     "2: AXE Body Spray": "RS 800",
                     "3: Colgate": "RS 150",
                     "4: Exit":""}},)

   while True:
    self.select_grosery = input("Select Your Item ")
    if self.select_grosery=="1":
         print("Yes Fog Selected Any Thing Else")
         self.price_1=self.price_1+700
         self.price_list=(self.price_list+"Fog Body Spray      :RS 700""\n")
    elif self.select_grosery=="2":
        print("Yes AXE Selected Any Thing Else")
        self.price_1 = self.price_1 + 800
        self.price_list = (self.price_list+"AXE Body Spray      :RS 700""\n")
    elif self.select_grosery=="3":
        print("Yes Colgate Selected Any Thing Else")
        self.price_1 = self.price_1 + 150
        self.price_list = (self.price_list+"Colgate             :RS 150""\n")
    elif self.select_grosery=="4":
        break

 def vegetables(self):
     print({"Vegetables":{"1: Potato":"RS 80/kg",
                          "2: Tomato":"RS 120/kg",
                          "3: Ledy Fingure":"RS 150/kg",
                          "4: Exit":""}})
     while True:
         self.select_vegetable = input("Select Your Item ")
         if self.select_vegetable == "1":
             print("Yes Potato Selected Any Thing Else")
             self.price_1 = self.price_1 + 80
             self.price_list = (self.price_list + "Potato              :RS 80""\n")
         elif self.select_vegetable == "2":
             print("Yes Tomato Selected Any Thing Else")
             self.price_1 = self.price_1 + 120
             self.price_list = (self.price_list + "Tomato              :RS 120""\n")
         elif self.select_vegetable == "3":
             print("Yes Lady Fingure Selected Any Thing Else")
             self.price_1 = self.price_1 + 150
             self.price_list = (self.price_list + "Lady Fingure        :RS 150""\n")
         elif self.select_vegetable == "4":
             break


 def fruits(self):
     print({"Fruits":{"1: Apple":"RS 200/kg",
                      "2: Banana":"RS 200/12",
                      "3: Grapes":"RS 400/kg",
                      "4: Exit":""}})
     while True:
         self.select_fruits = input("Select Your Item ")
         if self.select_fruits == "1":
             print("Yes Apple Selected Any Thing Else")
             self.price_1 = self.price_1 + 200
             self.price_list = (self.price_list + "Apple               :RS 200""\n")
         elif self.select_fruits == "2":
             print("Yes Banana Selected Any Thing Else")
             self.price_1 = self.price_1 + 200
             self.price_list = (self.price_list + "Banana              :RS 200""\n")
         elif self.select_fruits == "3":
             print("Yes Grapes Selected Any Thing Else")
             self.price_1 = self.price_1 + 400
             self.price_list = (self.price_list + "Grapes              :RS 400""\n")
         elif self.select_fruits == "4":
             break

 def machines(self):
     print({"Machines":{"1: Washing Machine":"RS 60000",
                        "2: Iron":"RS 15000",
                        "3: Frizer":"RS 150000",
                        "4: Exit":""}})

     while True:
         self.select_machine = input("Select Your Item ")
         if self.select_machine == "1":
             print("Yes Washing Machine Selected Any Thing Else")
             self.price_1 = self.price_1 + 60000
             self.price_list = (self.price_list + "Washing Machine     :RS 60000""\n")
         elif self.select_machine == "2":
             print("Yes Iron Selected Any Thing Else")
             self.price_1 = self.price_1 + 15000
             self.price_list = (self.price_list + "Iron                :RS 15000""\n")
         elif self.select_machine == "3":
             print("Yes Frizer Selected Any Thing Else")
             self.price_1 = self.price_1 + 150000
             self.price_list = (self.price_list + "Frizer              :RS 150000""\n")
         elif self.select_machine == "4":
             break

 def drinks(self):
     print({"Drinks":{"1: Pepsi":"RS 180/1.5L",
                      "2: Coca Cola":"RS 180/1.5L",
                      "3: Fanta":"RS 170/1.5L",
                      "4: Exit":""}})
     while True:
         self.select_drink = input("Select Your Item ")
         if self.select_drink == "1":
             print("Yes Pepsi Selected Any Thing Else")
             self.price_1 = self.price_1 + 180
             self.price_list = (self.price_list + "Pepsi               :RS 180""\n")
         elif self.select_drink == "2":
             print("Yes Coca Cola Selected Any Thing Else")
             self.price_1 = self.price_1 + 180
             self.price_list = (self.price_list + "Coca Cola           :RS 180""\n")
         elif self.select_drink == "3":
             print("Yes Fanta Selected Any Thing Else")
             self.price_1 = self.price_1 + 170
             self.price_list = (self.price_list + "Fanta               :RS 170""\n")
         elif self.select_drink == "4":
             break

 def bill(self):
     print("****Your Bill****")
     print(self.price_list)
     print("GST 13%")
     print("Your Total Bill is :",self.price_1/100*113)


 def buyer(self):
     while True:
         order = input("Enter Your Option ")

         if order == "1":
             self.grosery()

         elif order == "2":
             self.vegetables()

         elif order == "3":
             self.fruits()

         elif order == "4":

             self.machines()

         elif order=="5":
             self.drinks()

         elif order=="6":
             self.bill()
             break
         else:
             print("Wrong Option")

obj=Mart()
obj.buyer()