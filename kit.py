
import datetime
import collections
import json

Item = collections.namedtuple( 'Item', [ 'name', 'location', 'packed', 'when_added', 'weight' ] )


class manager:
    list_of_all_kits = {}
    current_kit = None
    def __init__( self ):
        current_kit = None
        return


def make_new_kit( name ):
    manager.list_of_all_kits[ name ] = Kit( name )
    return manager.list_of_all_kits[ name ]
    return

def get_list_of_kits():
    return manager.list_of_all_kits.keys()

def set_working_kit( name ):
    manager.current_kit = manager.list_of_all_kits[name]
    return manager.current_kit

def useful_date( thedate ):
    ret = []
    date_and_time = ( str(thedate).split(" ") )
    ymd = date_and_time[0]
    hms = date_and_time[1].split(".")[0]

    md = ymd[5:]
    hm = hms[:-3]

    #ret.extend( ret.index(-1).split)
    return md, hm

def add_item( key, item ):
    if manager.current_kit != None:
        manager.current_kit.add_item( key, item )

def remove_item( key ):
    if manager.current_kit != None:
        manager.current_kit.remove_item( key )

def pack_item( itemkey, location=None ):
    if manager.current_kit != None:
        manager.current_kit.pack_item( itemkey, location )

def unpack_item( itemkey ):
    if manager.current_kit != None:
        manager.current_kit.unpack_item( itemkey )

def move_item( itemkey, new_loc ):
    if manager.current_kit != None:
        manager.current_kit.move_item( itemkey, new_loc )

def get_packed_unpacked():
    return manager.current_kit.get_packed_unpacked()

def print_list( packed_first = True ):
    if manager.current_kit != None:
        manager.current_kit.print_list(packed_first)

def pack_all():
    if manager.current_kit != None:
        manager.current_kit.pack_all()

def unpack_all():
    if manager.current_kit != None:
        manager.current_kit.unpack_all()

def check_weight():
    if manager.current_kit != None:
        return manager.current_kit.check_weight()

def check_full():
    if manager.current_kit != None:
        manager.current_kit.check_full()

def get_fullness():
    if manager.current_kit != None:
        manager.current_kit.get_fullness()

def backup():
    if manager.current_kit != None:
        manager.current_kit.backup()


class Kit:
    def __init__( self, name ):

        # when was this kit list created
        self.created_date = str(datetime.datetime.now())
        # when was the kit last fully packed
        self.last_full_date = 0
        self.items = {}
        self.verbose = True
        if self.verbose:
            print ( "Created a new kit list: " + name )
        return

    def add_item( self, key, item ):
        #add an item to this kit list
        self.items[key] = item
        self.pack_item( key )   #TODO messy!
        self.unpack_item( key )
        if self.verbose:
            print "added "+str(item.name)+" to kit list"
        return

    def remove_item( self, key ):
        #permanently remove an item from this kit list
        del self.items[key]
        return

    def pack_item( self, itemkey, location=None ):
        #set an items packed state to true
        olditem = self.items[itemkey]
        newitem = Item( olditem.name, location if location else olditem.location, True, str(datetime.datetime.now()), olditem.weight )
        self.items[itemkey] = newitem
        if self.verbose:
            print "Packed "+str( itemkey )
            print str(self.get_fullness()) +"% packed"
        self.check_full()
        return

    def unpack_item( self, itemkey ):
        #set an items packed state to false
        olditem = self.items[itemkey]
        newitem = Item( olditem.name, olditem.location, False, olditem.when_added, olditem.weight )
        self.items[itemkey] = newitem
        if self.verbose:
            print "Unpacked "+str( itemkey )
            print str(self.get_fullness()) +"% packed"

    def move_item( self, itemkey, new_loc ):
        #update where this item is stored (does not affect packed state)
        olditem = self.items[itemkey]
        newitem = Item( olditem.name, new_loc, olditem.packed, olditem.when_added, olditem.weight )
        self.items[itemkey] = newitem
        return

    def get_packed_unpacked( self ):
        packed_list = []
        unpacked_list = []
        for key, it in sorted(self.items.iteritems()):
            packed_list.append(it) if it.packed else unpacked_list.append(it)
        return packed_list, unpacked_list

    def print_list( self, packed_first=True ):
        #output the state and location of all items in this kit list (packed first)
        packed_list, unpacked_list = self.get_packed_unpacked()
        def print_item( it ):
            if it.packed:
                print "\t"+str(it.name)+" packed in your "+str(it.location)+" on "+str( useful_date(it.when_added))
            else:
                print "\t"+str(it.name)+" unpacked from your "+str(it.location)+" on "+str( useful_date(it.when_added))

        def print_list( the_list, packed ):
            if packed:
                print ("Already packed:")
            else:
                print ("Not packed yet:")
            for it in the_list:
                print_item( it )

        if packed_first:
            print_list(packed_list, True )
            print_list(unpacked_list, False )
        else:
            print_list(unpacked_list, False )
            print_list(packed_list, True )

    def pack_all( self ):
        #set all items in this kit list to packed state
        if self.verbose:
            print "Marking all items as packed - are you sure?"
        for key, it in self.items.iteritems():
            if it.packed != True:
                self.pack_item( key )
        return

    def unpack_all( self ):
        #set all items in this kit list to unpacked state
        if self.verbose:
            print "Unpacking everyting"
        for key, it in self.items.iteritems():
            if it.packed != False:
                self.unpack_item( key )
        return

    def check_weight( self ):
        sum_weight = 0
        packed_weight = 0
        for it in self.items.itervalues():
            sum_weight += it.weight
            if it.packed:
                packed_weight += it.weight
        return packed_weight, sum_weight

    def check_full( self ):
        #check whether all the items in this kit have been packed
        #then do something special about it
        all_packed = True
        for it in self.items.itervalues():
            if it.packed != True:
                all_packed = False
                break
        #TODO maybe there's a 'if any' syntax
        #TODO or just use get_fullness == 100
        if all_packed == False:
            return False
        else:
            print "All items packed, time to leave"
            self.last_full_date = str(datetime.datetime.now())
        return True

    def get_fullness( self ):
        size = len(self.items)
        packed = 0
        for it in self.items.itervalues():
            if it.packed:
                packed += 1
        ret = (packed*100)/size
        return ret

    def backup( self ):
        return json.dumps(self.items)

