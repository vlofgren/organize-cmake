# organize\_cmake.py

A quick python script I hacked together in order to organize my CLion-created CMake-file that grew more unwieldy
with every file.

## Usage:

    ./organize_cmake.py a/foo.cpp a/foo.h b/foo.cpp bar.cpp baz.cpp

Example output:

	# a/foo.cpp a/foo.h b/foo.cpp bar.cpp baz.cpp
	set(A_HEADERS a/foo.h)
	set(A_SOURCES a/foo.cpp)

	set(B_HEADERS )
	set(B_SOURCES b/foo.cpp)

	set(BASE_HEADERS )
	set(BASE_SOURCES bar.cpp baz.cpp)

	set(SOURCE_FILES ${A_SOURCES} ${A_HEADERS} ${B_SOURCES} ${B_HEADERS} ${BASE_SOURCES} ${BASE_HEADERS})
	
