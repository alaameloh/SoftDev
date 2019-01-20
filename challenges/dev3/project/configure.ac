#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

# Prelude
AC_PREREQ([2.59])
AC_INIT([lame_project], [3.3.5], [houimel@eurecom.fr]) #because WOWTLK was the best
AC_CONFIG_SRCDIR([src/main/main.c])
AC_CONFIG_HEADERS([config.h])
AM_INIT_AUTOMAKE([foreign]) 

# Checks for programs.
AC_PROG_CC

# Checks for libraries
AC_PROG_RANLIB #warning from automake

AC_SEARCH_LIBS([mistery_value], [mistery magic voodoo ])
# Checks for header files
AC_COMPILE_IFELSE(
    [AC_LANG_PROGRAM([[#include <mistery.h>]], [[mistery_value(2);]])],
    [AC_MSG_RESULT([yes])],
    [AC_DEFINE([MISTERY_VALUE_ONEPARAM], [77], [the system is too lame to take two params])]
)
# Checks for typedefs, structures

# Check for compiler characteristics

# Checks for library functions

# Checks for system services

# Output files
AC_CONFIG_FILES([Makefile
                 src/Makefile
                 src/lib_foo/Makefile
                 src/main/Makefile])
AC_OUTPUT