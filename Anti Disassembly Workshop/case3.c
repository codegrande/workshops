#include <stdio.h>

void main() {
	printf("Hello, World!");
	
	asm(".intel_syntax noprefix\n"
	//"jz .later\n"
	".byte 0x74\n"
	".byte 0x03\n"
	//"jnz .later\n"
	".byte 0x75\n"
	".byte 0x01\n"

	//".later:\n"
	".byte 0xe9\n"
	);
	printf("Not seen");

}
