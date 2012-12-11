def head(baseurl, urlname, name, wiki):
	print """<h3>
<a href=\"""" + baseurl + urlname + """\">""" + name + """</a> (<a href="http://en.wikipedia.org/wiki/""" + wiki + """\">en.Wikipedia</a>)
</h3>

<p style="font:12px Courier, mono; ">"""

def line(prefix, baseurl, name):
	print prefix + """<a href=\"""" + baseurl + """?name=""" + name + """\">""" + name + """</a>"""

def footer():
	print """</p>"""

global baseurl
baseurl = "http://genomes1.fi.muni.cz/cgi-bin/gb2/gbrowse/"

def a():
	urlname = "dropsophila_melanogaster"
	name = "Drosophila Melanogaster"
	wiki = "Drosophila_melanogaster"
	head(baseurl, urlname, name, wiki)
	pref = ""
	for chr in ["2L", "2LHet", "2R", "2RHet", "3L", "3LHet", "3R", "3RHet", "4", "X", "XHet", "YHet", "dmel_mitochondrion_genome"]:	
		line(pref, baseurl+urlname+'/', chr)
		if pref == "":
			pref = " "
	footer()

def b():
	urlname = "escherichia_coli"
	name = "Escherichia Coli K-12"
	wiki = "Escherichia_coli"
	head(baseurl, urlname, name, wiki)
	pref = " "
	line(pref, baseurl+urlname+'/', " NC_000913")
	footer()

def c():
	urlname = "homo_sapiens"
	name = "Homo Sapiens hg19"
	wiki = "Human"
	head(baseurl, urlname, name, wiki)
	pref = " "
	for chr in xrange(1,23):	
		line(pref, baseurl+urlname+'/', "chr"+str(chr))
		if pref == "":
			pref = " "
	for chr in ["X", "Y"]:
		line(pref, baseurl+urlname+'/', "chr"+chr)
	footer()
	
def d():
	urlname = "mus_musculus"
	name = "Mus Musculus"
	wiki = "House_mouse"
	head(baseurl, urlname, name, wiki)
	pref = " "
	for chr in ["NT_039573", "NT_039675", "NT_082868"]:	
		line(pref, baseurl+urlname+'/', chr)
		if pref == "":
			pref = " "
	footer()
#<option value="mus_musculus">Mus Musculus NBCI GRCm38.p1</option>
a()
print
b()
print
c()
print
d()