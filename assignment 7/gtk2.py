import pygtk
pygtk.require('2.0')
import gtk
w = gtk.Window(gtk.WINDOW_TOPLEVEL)
w.show()
b = gtk.Button("Hello PPL")
w.add(b)
b.show()
def hello(widget):
	print "hello there!"
b.connect("clicked", hello)
gtk.main()
