#belajar inheritance
from source import Hero_Fighter,Hero_Marksman

zani = Hero_Marksman('Zani')
yone = Hero_Fighter("Yone")

zani.show_info()
yone.show_info()

zani.gainExp = 300
yone.gainExp = 300

zani.show_info()
yone.show_info()
