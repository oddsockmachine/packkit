
from kit import *
import kivy
from kivy.app import App
from kivy.uix.label import Label



def main():
    mylist = Kit()
    print mylist.items['camera']
    mylist.add_item( 'wallet', Item( 'Wallet', 'rucksack', False, '12.20', 70 ) )
    mylist.pack_all()
    mylist.unpack_all()
    mylist.pack_item( 'camera' )
    mylist.pack_item( 'shirt' )
    mylist.pack_item( 'wallet', 'pocket' )
    mylist.unpack_item( 'shirt' )

    print "\n"
    mylist.print_list( True )
    print "Total weight = "+str( mylist.check_weight() )+ "g"
    print mylist.backup()
    pass


class MyApp(App):

    def build(self):
        return Label(text='Hello world')



if __name__ == '__main__':
    main()
    MyApp().run()


