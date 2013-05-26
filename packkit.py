
from kit import *
##import kivy
##from kivy.app import App
##from kivy.uix.label import Label
##from kivy.uix.button import Button


def main():


    make_new_kit( "Thailand" )
    all_kits = get_list_of_kits()
    my_kit = set_working_kit( all_kits[0] )
    add_item( 'wallet', Item( 'Wallet', 'rucksack', False, None, 70 ) )
    add_item( 'towel', Item( 'Towel','rucksack', False, None, 110 ) )
    pack_item( 'wallet' )
    pack_item( 'towel' )
    unpack_item( 'wallet' )
    pack_all()
    print str(check_weight())
    print "*******************************************************"
    make_new_kit( "India" )
    all_kits = get_list_of_kits()
    set_working_kit( 'India' )
    add_item( 'camera', Item( 'D90 Camera', 'handbag', True, '14.30', 700 ) )
    add_item( 'shirt', Item( 'Green Shirt', 'suitcase', True, '12.35', 100 ) )
    pack_item( 'camera' )
    print str(check_weight())
    print_list()
    pack_all()
    print "*******************************************************"
    set_working_kit( 'Thailand' )
    unpack_item( 'towel' )
    print "Total weight = "+str( check_weight() )+ "g"
    p, u = get_packed_unpacked()
    print p[0].name
    pass


##class MyApp(App):
##
##    def build(self):
##        return Button(text='Hello world')



if __name__ == '__main__':
    main()
    #MyApp().run()


