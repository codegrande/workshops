#include <stdio.h>

void main() {
	printf("Hello, World!");
	
	asm(".intel_syntax noprefix\n"
	".byte 0xeb\n"
	".byte 0xff\n"
	".byte 0xc0\n"
	);

	printf("Not seen");

}
