from guizero import App,Combo, Text, CheckBox, ButtonGroup, PushButton, info

def do_booking():
    info("Booking", "Thank you for booking")

app = App(title="My 2nd GUI App", width=300, height=200, layout="grid")

film_choice = Combo(app, options=["Star Wars", "Frozen", "Lion King"], grid=[1,0], align="left")
film_description = Text(app, text="Which film?", grid=[0,0], align="left")
vip_seat = CheckBox(app, text="VIP seat?", grid=[1,1], align="left")
row_choice = ButtonGroup(app, options=[ ["Front", "F"], ["Middle", "M"],["Back", "B"] ],
selected="M", horizontal=True, grid=[1,2], align="left")
book_seats = PushButton(app, command=do_booking, text="Book seat", grid=[1,3], align="left")

print( film_choice.value )
print( vip_seat.value )
print( row_choice.value )

app.display()


