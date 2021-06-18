import turtle as tu
import paint as p

str = tu.textinput("Welcome to my pic field", "Plese input a pic name")
if str == "star":
    import star as s
    s.star()
elif str == "funny":
    p.funny()