
cheesecake = {}

ingredients = [
"1 cup graham cracker crumbs.",
"1/4 cup unsalted butter, melted.",
"1 tablespoon sugar."
]

if len(ingredients) > 2:
    print("The first ingredient needed to make a cheesecake is a " + ingredients[0] )
    print("The second ingredient needed to make a cheesecake is a " + ingredients[1])
    print("The third ingredient needed is a " + ingredients[2])

fillings = [
"- 16 ounces cream cheese (room temperature)",
"- 2/3 cup sugar",
"- 1 cup sour cream",
"- 5 large eggs (room temperature)",
"- 1 tablespoon vanilla extract",
"- 1/2 cup heavy cream",
"fresh or marinated berries, or raspberry sauce."
]

if len(fillings) > 6:
    print("There are also fillings needed, such as: ")
    print (fillings[0])
    print (fillings[1])
    print (fillings[2])
    print (fillings[3])
    print (fillings[4])
    print (fillings[5])
    print ("We also have a serving suggestion, such as " + fillings[6])

instructions = [
"1. Position a rack in the middle of the oven and preheat to 350 degrees F.",
'''2. To make the crust: In a small bowl, mix the cracker crumbs with
the melted butter and the sugar together until evenly moistened.
Press the crumb mixture onto the bottom of a 9-inch springform pan.
Bake the crust until golden brown, about 10 to 12 minutes.
Cool the pan on a rack.''',
'''3. Lower the oven temperature to 325 degrees F.
In the bowl of a standing mixer fitted with the paddle attachment,
or with a hand-held mixer, cream the cream cheese on medium speed until smooth.
Gradually add the sugar and beat until light and fluffy.
(Stop mixing and scrape down the sides of the bowl and beaters as needed.)
Beat in the sour cream.
Add the eggs, one at a time, beating well after each addition.
Stir in the vanilla and cream.
Pour the batter into the prepared pan.''',
'''4. Bake until the top of the cheesecake is lightly browned,
but the center still jiggles slightly, about 45 minutes.
Cool the cake in the pan on a rack.
Cover with plastic wrap and refrigerate overnight before serving.''',
'''5. To remove the cake from the pan, run a knife or offset spatula
around the edges to release the edges from the pan.
Open the springform pan and remove the ring.''',
"6. Cut the cheesecake into wedges and serve with berries or a raspberry sauce if desired."
]

if len(instructions) > 5:
    print ("Instructions on making the cheesecake: ")
    print (instructions[0])
    print (instructions[1])
    print (instructions[2])
    print (instructions[3])
    print (instructions[4])
    print (instructions[5])
