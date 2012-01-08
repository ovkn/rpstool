A simple requests per second (rps) counter.

Intended for use in combination with POSIX tail (or similar) program.
Example: tail -f /var/log/some-frequently-written-access-log | rpstool
Of course, its usage is reasonable for highly loaded services only ;-)
