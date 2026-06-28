# Binary Specification: tcpmib.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\tcpmib.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8a1e40438d788ed3a7daea36fef405ee51db22c6f84f98058e49d94dbbfa9ab7`
* **Total Exported Functions:** 35

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `??0CTcpMibABC@@QEAA@AEBV0@@Z` | `0x2340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `??0CTcpMibABC@@QEAA@XZ` | `0x2340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??1CTcpMibABC@@UEAA@XZ` | `0x2360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??4CTcpMibABC@@QEAAAEAV0@AEBV0@@Z` | `0x2380` | 2,880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `??0CTcpMib@@QEAA@AEBV0@@Z` | `0x2EC0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??4CTcpMib@@QEAAAEAV0@AEBV0@@Z` | `0x2F00` | 4,416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0CTcpMib@@QEAA@XZ` | `0x4040` | 56 | UnwindData |  |
| 5 | `??1CTcpMib@@UEAA@XZ` | `0x4080` | 52 | UnwindData |  |
| 11 | `?GetDeviceDescription@CTcpMib@@UEAAKPEBD0KPEAGK@Z` | `0x40C0` | 219 | UnwindData |  |
| 12 | `?GetDeviceId@CTcpMib@@UEAAJPEBGKPEAGKPEAK@Z` | `0x41B0` | 188 | UnwindData |  |
| 13 | `?GetDeviceIdFromIni@CTcpMib@@AEAAJPEBGKPEAGKPEAK@Z` | `0x4280` | 1,201 | UnwindData |  |
| 14 | `?GetDeviceIdFromMib@CTcpMib@@AEAAJPEBGKPEAGKPEAK@Z` | `0x4740` | 281 | UnwindData |  |
| 15 | `?GetNextRequestId@CTcpMib@@UEAAKPEAK@Z` | `0x4860` | 99 | UnwindData |  |
| 16 | `?GetPortList@CTcpMib@@UEAAJPEBGPEAEKPEAK@Z` | `0x48D0` | 145 | UnwindData |  |
| 17 | `?GetPortListFromIni@CTcpMib@@AEAAJPEBGPEAEKPEAK@Z` | `0x4970` | 1,089 | UnwindData |  |
| 18 | `?GetPortListFromMib@CTcpMib@@AEAAJPEBGPEAEKPEAK@Z` | `0x4DC0` | 652 | UnwindData |  |
| 19 | `?GetStatusFromVBL@CTcpMib@@CAKPEAXPEAUsmiVALUE@@11@Z` | `0x5060` | 897 | UnwindData |  |
| 20 | `?InitSnmp@CTcpMib@@UEAAKXZ` | `0x53F0` | 132 | UnwindData |  |
| 21 | `?IsValid@CTcpMib@@QEBAHXZ` | `0x5480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `?MapAsynchToPortStatus@CTcpMib@@CAHKPEAU_PORT_INFO_3W@@@Z` | `0x5490` | 241 | UnwindData |  |
| 23 | `?RFC1157ToString@CTcpMib@@UEAAHPEAUSnmpVarBind@@PEAGKPEAK@Z` | `0x5590` | 295 | UnwindData |  |
| 24 | `?RegisterDeviceStatusCallback@CTcpMib@@UEAAKP6AKHPEBD0KKK@ZPEAPEAX@Z` | `0x56C0` | 84 | UnwindData |  |
| 25 | `?RequestDeviceStatus@CTcpMib@@UEAAKPEAXKPEBG1K@Z` | `0x5720` | 1,102 | UnwindData |  |
| 26 | `?SnmpCallback@CTcpMib@@CAKPEAXPEAUHWND__@@I_K_J0@Z` | `0x5B80` | 982 | UnwindData |  |
| 27 | `?SnmpGet@CTcpMib@@QEAAKPEBD0PEAUSnmpVarBindList@@@Z` | `0x5F60` | 190 | UnwindData |  |
| 28 | `?SnmpGet@CTcpMib@@UEAAKPEBD00PEAUSnmpVarBindList@@@Z` | `0x6030` | 199 | UnwindData |  |
| 29 | `?SnmpGet@CTcpMib@@UEAAKPEBD0PEAUAsnObjectIdentifier@@PEAUSnmpVarBindList@@@Z` | `0x6100` | 213 | UnwindData |  |
| 30 | `?SnmpGetNext@CTcpMib@@QEAAKPEBD0PEAUSnmpVarBindList@@@Z` | `0x61E0` | 190 | UnwindData |  |
| 31 | `?SnmpGetNext@CTcpMib@@UEAAKPEBD0PEAUAsnObjectIdentifier@@PEAUSnmpVarBindList@@@Z` | `0x62B0` | 213 | UnwindData |  |
| 32 | `?SupportsPortMonMib@CTcpMib@@AEAAJPEBGPEAH@Z` | `0x6400` | 376 | UnwindData |  |
| 33 | `?SupportsPrinterMib@CTcpMib@@UEAAHPEBD0KPEAH@Z` | `0x6580` | 323 | UnwindData |  |
| 34 | `?UnInitSnmp@CTcpMib@@UEAAXXZ` | `0x66D0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `GetTcpMibPtr` | `0x6870` | 125 | UnwindData |  |
| 10 | `??_7CTcpMibABC@@6B@` | `0x9010` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `??_7CTcpMib@@6B@` | `0x9080` | 0 | Indeterminate |  |
