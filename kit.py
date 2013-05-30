
import datetime
import collections
import glob
import pickle

Item = collections.namedtuple( 'Item', 
    [ 'name', 'location', 'packed', 'when_added', 'weight' ] )


def verbosity( fn ):
    def output( *arg ):
        out = fn(*arg)
        if manager.verbose:
            print out
        return out
    return output


#crap decorator
def check_kit( fn ):
    def check( *arg ):
        if manager.current_kit != None:
            return fn( *arg )
        else:
            return "No working kit defined"
            return None
    return check


class manager:
    current_kit = None
    verbose = False
    def __init__( self ):
        current_kit = None
        verbose = False
        return


@verbosity
def make_new_kit( name ):
    manager.current_kit = Kit( name )
    return manager.current_kit

@check_kit 
@verbosity
def save_working_kit():
    f_name = "saved/"+str(manager.current_kit.name)+".p"
    return pickle.dump( manager.current_kit, open( f_name, "wb" ) )

@verbosity
def load_kit( kit_name ):
    f_name = "saved/"+str(kit_name)+".p"
    manager.current_kit = pickle.load( open( f_name, "rb" ) )
    return manager.current_kit

@verbosity
def get_saved_kits():
    files = glob.glob("saved\\*.p")
    names = []
    for f in files:
        n = f.split("\\")[-1]
        names.append( n[:-2] )
    return names

@verbosity
def useful_date( thedate ):
    ret = []
    date_and_time = ( str(thedate).split(" ") )
    ymd = date_and_time[0]
    hms = date_and_time[1].split(".")[0]
    md = ymd[5:]
    hm = hms[:-3]
    return md, hm

@check_kit
@verbosity
def add_item( key, item ):
    return manager.current_kit.add_item( key, item )

@check_kit
@verbosity
def remove_item( key ):
    return manager.current_kit.remove_item( key )

@check_kit
@verbosity
def pack_item( itemkey, location=None ):
    return manager.current_kit.pack_item( itemkey, location )

@check_kit
@verbosity
def unpack_item( itemkey ):
    return manager.current_kit.unpack_item( itemkey )

@check_kit
@verbosity
def move_item( itemkey, new_loc ):
    return manager.current_kit.move_item( itemkey, new_loc )

@check_kit
@verbosity
def get_packed_unpacked():
    return manager.current_kit.get_packed_unpacked()

@check_kit
@verbosity
def print_list( packed_first = True ):
    return manager.current_kit.print_list(packed_first)

@check_kit
@verbosity
def pack_all():
    return manager.current_kit.pack_all()

@check_kit
@verbosity
def unpack_all():
    return manager.current_kit.unpack_all()

@check_kit
@verbosity
def check_weight():
    return manager.current_kit.check_weight()

@check_kit
@verbosity
def check_full():
    return manager.current_kit.check_full()

@check_kit
@verbosity
def get_fullness():
    return manager.current_kit.get_fullness()


class Kit:
    def __init__( self, name ):

        # when was this kit list created
        self.created_date = str(datetime.datetime.now())
        self.name = name
        # when was the kit last fully packed
        self.last_full_date = 0
        self.items = {}
        self.verbose = True
        if self.verbose:
            print ( "Created a new kit list: " + name )
        return

    def reimport( self, pick ):
        #self.add_item( ) TODO
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
        oi = self.items[itemkey]
        newitem = Item( oi.name, location if location else oi.location, True, str(datetime.datetime.now()), oi.weight )
        self.items[itemkey] = newitem
        if self.verbose:
            print "Packed "+str( itemkey )
            print str(self.get_fullness()) +"% packed"
        self.check_full()
        return

    def unpack_item( self, itemkey ):
        #set an items packed state to false
        oi = self.items[itemkey]
        newitem = Item( oi.name, oi.location, False, oi.when_added, oi.weight )
        self.items[itemkey] = newitem
        if self.verbose:
            print "Unpacked "+str( itemkey )
            print str(self.get_fullness()) +"% packed"

    def move_item( self, itemkey, new_loc ):
        #update where this item is stored (does not affect packed state)
        oi = self.items[itemkey]
        newitem = Item( oi.name, new_loc, oi.packed, oi.when_added, oi.weight )
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
                #print "\t%s packed in your %s on %s.", str(it.name), str(it.location), str( useful_date(it.when_added))
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

