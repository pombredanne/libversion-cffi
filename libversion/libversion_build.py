#!/usr/bin/env python
#
# Copyright (c) 2017 Dmitry Marakasov <amdmi3@amdmi3.ru>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from subprocess import check_output

from cffi import FFI


def pkgconfig(package):
    result = {}
    for token in check_output(['pkg-config', '--libs', '--cflags', package]).decode('utf-8').split():
        if token.startswith('-I'):
            result.setdefault('include_dirs', []).append(token[2:])
        elif token.startswith('-L'):
            result.setdefault('library_dirs', []).append(token[2:])
        elif token.startswith('-l'):
            result.setdefault('libraries', []).append(token[2:])
    return result


ffi = FFI()
ffi.set_source('libversion._libversion', """
    #include <libversion/compare.h>
""", **pkgconfig('libversion'))
ffi.cdef("""
    int version_compare_simple(const char* v1, const char* v2);
""")


if __name__ == '__main__':
    ffi.compile()
