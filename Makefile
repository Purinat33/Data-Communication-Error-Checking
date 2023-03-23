parity:
	gcc parity.c -o parity

crc:
	gcc crc.c -o crc

checksum:
	gcc checksum.c -o checksum

hamming:
	gcc hamming.c -o hamming

clean:
	find . -type f ! -path './.git/*' ! -name '*.gitignore' ! -name '*.*' ! -name 'Makefile' -delete
