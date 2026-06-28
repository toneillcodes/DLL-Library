# Binary Specification: icmp.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\icmp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `efbb68d98859055aa9ff83240d65e732dfff60f55ef651972c4b171c95e6311f`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `IcmpCloseHandle` | `0x0` | - | Forwarded | Forwarded to: `iphlpapi.IcmpCloseHandle` |
| 2 | `IcmpCreateFile` | `0x0` | - | Forwarded | Forwarded to: `iphlpapi.IcmpCreateFile` |
| 3 | `IcmpParseReplies` | `0x0` | - | Forwarded | Forwarded to: `iphlpapi.IcmpParseReplies` |
| 4 | `IcmpSendEcho` | `0x0` | - | Forwarded | Forwarded to: `iphlpapi.IcmpSendEcho` |
| 5 | `IcmpSendEcho2` | `0x0` | - | Forwarded | Forwarded to: `iphlpapi.IcmpSendEcho2` |
| 6 | `do_echo_rep` | `0x0` | - | Forwarded | Forwarded to: `iphlpapi.do_echo_rep` |
| 7 | `do_echo_req` | `0x0` | - | Forwarded | Forwarded to: `iphlpapi.do_echo_req` |
| 8 | `register_icmp` | `0x0` | - | Forwarded | Forwarded to: `iphlpapi.register_icmp` |
