# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
Player1 = "Ruud Gullit"
Player2 = "Marco van Basten"
goal_0 = 32
goal_1 = 54
scorers = Player1 + " " + str(goal_0) + ", " + Player2 + " " + str(goal_1)
#report1 = Player1 + " " + "scored in the " + str(goal_0) +"nd minute\n" + Player2 + " " + "scored in the " + str(goal_1) + "th minute" 
report = f'{Player1} scored in the {str(goal_0)}nd minute' + "\n" f'{Player2} scored in the {str(goal_1)}th minute' 
"""

Use f-strings -or- the +-operator to create a single string with information about who scored when in the format:

Dacht zodoende dat het ook mocht :)
"""

player = "Marco van Basten"
first_name_end=player.find(" ") # zolang een dubbele voornaam met een - is.. 
first_name = player[:first_name_end]
last_name = player[(first_name_end+1):] 
first_name_len=len(first_name)
last_name_len=len(last_name)
print (first_name, last_name)

name_short=first_name[0:1] + ". " + last_name

chant = (first_name+"! ")*(first_name_len-1)+first_name+"!"
chant_len=len(chant)
last_char=chant[chant_len-1]
good_chant=(last_char!=" ")

print (chant)