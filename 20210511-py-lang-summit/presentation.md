# CPython -> CircuitPython

---

# ~29 megabytes -> ~650 kilobytes

^ Our smallest CircuitPython builds are 192 kilobytes. Even when this small, CircuitPython feels like Python. Why is that?

---
# CPython builtins

```
__build_class__ breakpoint  enumerate id         next     setattr
__debug__       bytearray   eval      input      object   slice
__doc__         bytes       exec      int        oct      sorted
__import__      callable    exit      isinstance open     staticmethod
__loader__      chr         filter    issubclass ord      str
__name__        classmethod float     iter       pow      sum
__package__     compile     format    len        print    super
__spec__        complex     frozenset license    property tuple
abs             copyright   getattr   list       quit     type
all             credits     globals   locals     range    vars
any             delattr     hasattr   map        repr     zip
ascii           dict        hash      max        reversed
bin             dir         help      memoryview round
bool            divmod      hex       min        set
```

---
# CircuitPython builtins

```
__build_class__             enumerate id         next     setattr
                bytearray   eval      input      object   slice
                bytes       exec      int        oct      sorted
__import__      callable              isinstance open     staticmethod
                chr         filter    issubclass ord      str
__name__        classmethod float     iter       pow      sum
                                      len        print    super
                complex     frozenset            property tuple
abs                         getattr   list                type
all                         globals   locals     range
any             delattr     hasattr   map        repr     zip
                dict        hash      max        reversed
bin             dir         help      memoryview round
bool            divmod      hex       min        set
```

^ Thanks to MicroPython, CP has inherited a really strong syntax and language feature core. The best way to see this is through the tests that compare MicroPython behavior to CPython's.

---
# CPython Modules

```
abc         cmath        dis          gettext   lists           pathlib       pydoc_data    smtplib       telnetlib   uu
aifc        cmd          distutils    glob      locale          pdb           pyexpat       sndhdr        tempfile    uuid
antigravity code         doctest      graphlib  logging         pickle        queue         socket        termios     venv
argparse    codecs       easy_install grp       lzma            pickletools   quopri        socketserver  test        warnings
array       codeop       email        gzip      mailbox         pip           random        sqlite3       textwrap    wave
ast         collections  encodings    hashlib   mailcap         pipes         re            sre_compile   this        weakref
asynchat    colorsys     ensurepip    heapq     marshal         pkg_resources readline      sre_constants threading   webbrowser
asyncio     compileall   enum         hmac      math            pkgutil       reprlib       sre_parse     time        wheel
asyncore    concurrent   errno        html      mimetypes       platform      resource      ssl           timeit      wsgiref
atexit      configparser faulthandler http      mmap            plistlib      rlcompleter   stat          tkinter     xdrlib
audioop     contextlib   fcntl        idlelib   modulefinder    poplib        runpy         statistics    token       xml
base64      contextvars  filecmp      imaplib   multiprocessing posix         sched         string        tokenize    xmlrpc
bdb         copy         fileinput    imghdr    netrc           posixpath     secrets       stringprep    trace       xxlimited
binascii    copyreg      fnmatch      imp       nis             pprint        select        struct        traceback   xxsubtype
binhex      crypt        fontforge    importlib nntplib         profile       selectors     subprocess    tracemalloc zipapp
bisect      csv          formatter    inspect   ntpath          psMat         setuptools    sunau         tty         zipfile
builtins    ctypes       fractions    io        nturl2path      pstats        shelve        symbol        turtle      zipimport
bz2         curses       ftplib       ipaddress numbers         pty           shlex         symtable      turtledemo  zlib
cProfile    dataclasses  functools    itertools opcode          pwd           shutil        sys           types       zoneinfo
calendar    datetime     gc           json      operator        py_compile    signal        sysconfig     typing
cgi         dbm          genericpath  keyword   optparse        pyaff         site          syslog        unicodedata
cgitb       decimal      getopt       lib2to3   os              pyclbr        sitecustomize tabnanny      unittest
chunk       difflib      getpass      linecache parser          pydoc         smtpd         tarfile       urllib
```

^ Once you leave that core,

---
# CircuitPython Modules

```
.          
           
               
                     
array                                                                         random
            collections                                                       re

                                                math                                                      time        wheel     
                         errno




binascii                                                                                    struct


builtins                              io

                                                                                            sys
                         gc           json

                                                os
 
```

^ Once you leave that core,

---

# CPython `random`

```
Random       gauss          randint   triangular
SystemRandom getrandbits    random    uniform
betavariate  getstate       randrange vonmisesvariate
choice       lognormvariate sample    weibullvariate
choices      normalvariate  seed
expovariate  paretovariate  setstate
gammavariate randbytes      shuffle
```

^ Builtin modules are strict subsets of their CPython counterparts.

---

# CircuitPython `random`

```
                            randint
             getrandbits    random    uniform
                            randrange
choice
                            seed


```
---

# 1. The Python *feel* requires a small core.

---

# Smaller core means Python in more places.

---

# Things people have asked for:
* numpy
* f-strings
* pandas
* Jupyter
* pdb
* asyncio

---

# 2. Python is much bigger than just `python`

^ So, don't be scared of reworking the balance between the Python core and the vast array of libraries. Both pieces are already critical to what Python is for folks.
