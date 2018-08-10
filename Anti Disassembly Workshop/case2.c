#include <stdio.h>

void main() {
	printf("Hello, World!");
	
	asm(".intel_syntax noprefix\n"
	"xor eax, eax\n"
	//"jz .later\n"
	".byte 0x74\n"
	".byte 0x01\n"
	//".later:\n"
	".byte 0xe9\n"
	);

	printf("Not seen");

}


