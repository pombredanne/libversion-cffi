# libversion-cffi

A simple CFFI wrapper around [libversion](https://github.com/repology/libversion) version string comparison library.

## Synopsis

```
>>> from libversion import version_compare_simple
>>> version_compare_simple('0.9', '1.0')
-1
>>> version_compare_simple('1.1', '1.0')
1
>>> version_compare_simple('1', '1.0.0')
0
```

## Author

* [Dmitry Marakasov](https://github.com/AMDmi3) <amdmi3@amdmi3.ru>

## License

[MIT](COPYING)
