from guizero import App, Text, TextBox, PushButton, Slider, Picture

def say_my_name():
    welcome_msg.value = name_TB.value

def change_text_size(slider_value):
    welcome_msg.size = slider_value
    
app = App(title="Hello world")

welcome_msg = Text(app, text="Welcome to my app", size=28, font="Times New Roman", color="lightblue")
name_TB = TextBox(app)
update_text = PushButton(app, command=say_my_name, text="Display my name")
text_size = Slider(app, command=change_text_size, start=10, end=80)
my_cat = Picture(app, image="/usr/share/scratch/Media/Costumes/Transportation/train.gif")

app.display()

