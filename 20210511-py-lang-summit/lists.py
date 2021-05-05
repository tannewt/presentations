import builtins
import random

def print_comparison(original, include, cols=6):
    height = len(original) // cols

    leftover = len(original) % cols
    if leftover > 0:
        height += 1

    gathered = []
    for i in range(height):
        row = []
        for j in range(cols):
            index = height * j + i
            if index >= len(original):
                row.append("")
            else:
                row.append(original[index])
        gathered.append(row)

    max_width = [0] * cols
    for i in range(height):
        for j, current in enumerate(max_width):
            max_width[j] = max(current, len(gathered[i][j]))

    for i in range(height):
        for j, current in enumerate(max_width):
            entry = gathered[i][j]
            print(entry + " " * (current - len(entry) + 1), end="")
        print()
    print()

    for i in range(height):
        for j, current in enumerate(max_width):
            entry = gathered[i][j]
            if entry not in include:
                entry = ""
            print(entry + " " * (current - len(entry) + 1), end="")
        print()


cpython_builtins = sorted([x for x in dir(builtins) if not x[0].isupper()])
circuitpython_builtins = ['__build_class__', '__class__', '__import__', '__name__', '__repl_print__', 'abs', 'all', 'any', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'complex', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'filter', 'float', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'zip']

print_comparison(cpython_builtins, circuitpython_builtins, cols=6)

circuitpython_modules = """
__main__          bitmaptools       json              sdcardio
_bleio            bitops            math              sharpdisplay
_eve              board             microcontroller   storage
_pixelbuf         builtins          micropython       struct
adafruit_bus_device                 busio             msgpack           supervisor
analogio          collections       neopixel_write    synthio
array             countio           os                sys
array             digitalio         pulseio           terminalio
audiobusio        displayio         pwmio             time
audiocore         errno             random            touchio
audiomixer        fontio            re                ulab
audiomp3          framebufferio     rgbmatrix         usb_hid
audiopwmio        gamepad           rotaryio          usb_midi
binascii          gc                rp2pio            vectorio
bitbangio         io                rtc               watchdog"""
cpython_modules = """
__future__          _testinternalcapi   getopt              rlcompleter
_abc                _testmultiphase     getpass             runpy
_aix_support        _thread             gettext             sched
_ast                _threading_local    glob                secrets
_asyncio            _tkinter            graphlib            select
_bisect             _tracemalloc        grp                 selectors
_blake2             _uuid               gzip                setuptools
_bootlocale         _warnings           hashlib             shelve
_bootsubprocess     _weakref            heapq               shlex
_bz2                _weakrefset         hmac                shutil
_codecs             _xxsubinterpreters  html                signal
_codecs_cn          _xxtestfuzz         http                site
_codecs_hk          _zoneinfo           idlelib             sitecustomize
_codecs_iso2022     abc                 imaplib             smtpd
_codecs_jp          aifc                imghdr              smtplib
_codecs_kr          antigravity         imp                 sndhdr
_codecs_tw          argparse            importlib           socket
_collections        array               inspect             socketserver
_collections_abc    ast                 io                  sqlite3
_compat_pickle      asynchat            ipaddress           sre_compile
_compression        asyncio             itertools           sre_constants
_contextvars        asyncore            json                sre_parse
_crypt              atexit              keyword             ssl
_csv                audioop             lib2to3             stat
_ctypes             base64              linecache           statistics
_ctypes_test        bdb                 lists               string
_curses             binascii            locale              stringprep
_curses_panel       binhex              logging             struct
_datetime           bisect              lzma                subprocess
_dbm                builtins            mailbox             sunau
_decimal            bz2                 mailcap             symbol
_distutils_hack     cProfile            marshal             symtable
_elementtree        calendar            math                sys
_functools          cgi                 mimetypes           sysconfig
_gdbm               cgitb               mmap                syslog
_hashlib            chunk               modulefinder        tabnanny
_heapq              cmath               multiprocessing     tarfile
_imp                cmd                 netrc               telnetlib
_io                 code                nis                 tempfile
_json               codecs              nntplib             termios
_locale             codeop              ntpath              test
_lsprof             collections         nturl2path          textwrap
_lzma               colorsys            numbers             this
_markupbase         compileall          opcode              threading
_md5                concurrent          operator            time
_multibytecodec     configparser        optparse            timeit
_multiprocessing    contextlib          os                  tkinter
_opcode             contextvars         parser              token
_operator           copy                pathlib             tokenize
_osx_support        copyreg             pdb                 trace
_peg_parser         crypt               pickle              traceback
_pickle             csv                 pickletools         tracemalloc
_posixshmem         ctypes              pip                 tty
_posixsubprocess    curses              pipes               turtle
_py_abc             dataclasses         pkg_resources       turtledemo
_pydecimal          datetime            pkgutil             types
_pyio               dbm                 platform            typing
_queue              decimal             plistlib            unicodedata
_random             difflib             poplib              unittest
_scproxy            dis                 posix               urllib
_sha1               distutils           posixpath           uu
_sha256             doctest             pprint              uuid
_sha3               easy_install        profile             venv
_sha512             email               psMat               warnings
_signal             encodings           pstats              wave
_sitebuiltins       ensurepip           pty                 weakref
_socket             enum                pwd                 webbrowser
_sqlite3            errno               py_compile          wheel
_sre                faulthandler        pyaff               wsgiref
_ssl                fcntl               pyclbr              xdrlib
_stat               filecmp             pydoc               xml
_statistics         fileinput           pydoc_data          xmlrpc
_string             fnmatch             pyexpat             xxlimited
_strptime           fontforge           queue               xxsubtype
_struct             formatter           quopri              zipapp
_symtable           fractions           random              zipfile
_sysconfigdata__darwin_darwin ftplib              re                  zipimport
_testbuffer         functools           readline            zlib
_testcapi           gc                  reprlib             zoneinfo
_testimportmultiple genericpath         resource"""

circuitpython_modules = sorted(list(set(circuitpython_modules.split())))
cpython_modules = sorted(cpython_modules.split())
cpython_modules = [x for x in cpython_modules if x[0] != "_"]
print_comparison(cpython_modules, circuitpython_modules, cols=10)

cpython_random = dir(random)
cpython_random = [x for x in cpython_random if x[0] != "_" and not (x[-1].isupper() or x[-1].isnumeric())]
circuitpython_random = ['choice', 'getrandbits', 'randint', 'random', 'randrange', 'seed', 'uniform']
print_comparison(sorted(cpython_random), circuitpython_random, cols=4)
