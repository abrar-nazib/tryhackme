# Crackthehash

[Crackthehash Tryhackme](https://tryhackme.com/room/crackthehash)

## Hash1

**Hash:** `48bb6e862e54f2a795ffc4e541caed4d`

- `hashid $(cat hash1.txt)` raw-MD5
- `john hash1.txt --wordlist=../../wordlists/rockyou.txt --format=raw-MD5`

## Hash2

**Hash:** `CBFDAC6008F9CAB4083784CBD1874F76618D2A97`

- `hashid $(cat hash2.txt)` raw-SHA1
- `john hash2.txt --wordlist=../../wordlists/rockyou.txt`

## Hash3

**Hash:** `1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032`

- `hashid $(cat hash3.txt)`

## Hash6

**Hash:** `F09EDCB1FCEFC6DFB23DC3505A882655FF77375ED8AA2D1C13F640FCCC2D0C85`

- `hashid $(cat hash3.txt)`
- `hashcat -m 1400 hash6.txt ../../wordlists/rockyou.txt --force`

## Hash7

**Hash:** `1DFECA0C002AE40B8619ECF94819CC1B`

- NTLM
- `hashcat -m 1000 hash7.txt ../../wordlists/rockyou.txt --force`
