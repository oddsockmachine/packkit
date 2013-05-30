
from kit import *
import unittest
##import kivy
##from kivy.app import App
##from kivy.uix.label import Label
##from kivy.uix.button import Button


def main():
    
    add_item( 'coat', Item( 'Wooly Coat','Suitcase', False, None, 420 ) )


    make_new_kit( "Iceland" )
    manager.verbose = False
    print manager.current_kit
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
    add_item( 'camera', Item( 'D90 Camera', 'handbag', True, '14.30', 700 ) )
    add_item( 'shirt', Item( 'Green Shirt', 'suitcase', True, '12.35', 100 ) )
    pack_item( 'camera' )
    print str(check_weight())
    print_list()
    pack_all()
    unpack_item( 'camera' )
    save_working_kit()




    print "*******************************************************"

    #print "Total weight = "+str( check_weight() )+ "g"
    #p, u = get_packed_unpacked()

    print get_saved_kits()
    load_kit("Thailand")
    unpack_item( 'towel' )
    print "\n\n"
    save_working_kit()
    print "\n\n\n"
    load_kit( 'India' )
    print_list()


    print get_saved_kits()
    load_kit( 'Iceland' )
    print_list()
    print"\n\n"
    unpack_item( 'wallet' )
    save_working_kit()
    print"\n\n"
    print_list()
    print"\n\n"

    manager.verbose = True
    sk = get_saved_kits()
    print load_kit( sk[1] ).name


    pass


##class MyApp(App):
##
##    def build(self):
##        return Button(text='Hello world')


class TestKit(unittest.TestCase):
    
    def test_no_kit_wrapper(self):
        manager.current_kit = None
        ret = add_item( 'coat', Item( 'Wooly Coat','Suitcase', False, None, 420 ) )
        self.assertEqual( ret,  "No working kit defined" )
        ret = remove_item( 'coat' )
        self.assertEqual( ret,  "No working kit defined" )

    def test_no_kit_wrapper(self):
        make_new_kit( "Test" )
        manager.verbose = False
        self.assertEqual( len(manager.current_kit.items), 0, "there should be 0 items in kit" )
        add_item( 'wallet', Item( 'Wallet', 'Rucksack', False, None, 70 ) )
        self.assertEqual( len(manager.current_kit.items), 1, "wrong number of items in kit" )

if __name__ == '__main__':
    main()
    unittest.main()
    
    #MyApp().run()
