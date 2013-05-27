
from kit import *
##import kivy
##from kivy.app import App
##from kivy.uix.label import Label
##from kivy.uix.button import Button


def main():



    make_new_kit( "Iceland" )
    my_kit = set_working_kit( 'Iceland' )
    add_item( 'wallet', Item( 'Wallet', 'Rucksack', False, None, 70 ) )
    add_item( 'coat', Item( 'Wooly Coat','Suitcase', False, None, 420 ) )
    pack_item( 'wallet' )
    pack_item( 'coat' )
    unpack_item( 'wallet' )
    pack_all()
    print str(check_weight())
    save_working_kit()


    make_new_kit( "Thailand" )
    add_item( 'wallet', Item( 'Wallet', 'rucksack', False, None, 70 ) )
    add_item( 'towel', Item( 'Towel','rucksack', False, None, 110 ) )
    pack_item( 'wallet' )
    pack_item( 'towel' )
    unpack_item( 'wallet' )
    pack_all()
    print str(check_weight())
    save_working_kit()


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
    unpack_item( 'camera' )
    save_working_kit()




    print "*******************************************************"
    set_working_kit( 'Thailand' )
    #unpack_item( 'towel' )
    print "Total weight = "+str( check_weight() )+ "g"
    p, u = get_packed_unpacked()

    save_working_kit()
    print get_saved_kits()
    load_kit("Thailand")
    print "\n\n"
    squish()
    print "\n\n\n"
    unsquish( 'India' )
    print_list()


    print get_saved_kits()
    load_kit( 'Iceland' )
    print_list()
    print"\n\n"
    unpack_item( 'coat' )
    save_working_kit()
    print"\n\n"
    print_list()
    print"\n\n"


    pass


##class MyApp(App):
##
##    def build(self):
##        return Button(text='Hello world')



if __name__ == '__main__':
    main()
    #MyApp().run()


