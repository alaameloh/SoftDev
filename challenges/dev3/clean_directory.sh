find . \( -name "*.o" -or -name "*.a" -or -name "Makefile" -or -name "Makefile.in" -o -name ".deps" \) -delete; rm -rf $(ls -1 | grep -vE "(Makefile.am|configure.ac|src)") src/main/mistery_foo
