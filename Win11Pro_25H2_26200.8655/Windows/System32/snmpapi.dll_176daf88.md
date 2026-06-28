# Binary Specification: snmpapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\snmpapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `176daf88daeddd94b012412595fd7bee3ace575d5ac6101bc331c130ccf4b47f`
* **Total Exported Functions:** 38

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 11 | `SnmpTfxQuery` | `0x1940` | 2,234 | UnwindData |  |
| 17 | `SnmpUtilMemAlloc` | `0x3E90` | 48 | UnwindData |  |
| 13 | `SnmpUtilAsnAnyCpy` | `0x3ED0` | 70 | UnwindData |  |
| 21 | `SnmpUtilOctetsCpy` | `0x3FC0` | 143 | UnwindData |  |
| 18 | `SnmpUtilMemFree` | `0x4060` | 52 | UnwindData |  |
| 27 | `SnmpUtilOidFree` | `0x40A0` | 10 | UnwindData |  |
| 19 | `SnmpUtilMemReAlloc` | `0x4100` | 113 | UnwindData |  |
| 38 | `SnmpUtilVarBindListFree` | `0x4180` | 87 | UnwindData |  |
| 14 | `SnmpUtilAsnAnyFree` | `0x4350` | 57 | UnwindData |  |
| 22 | `SnmpUtilOctetsFree` | `0x43C0` | 48 | UnwindData |  |
| 36 | `SnmpUtilVarBindFree` | `0x4400` | 10 | UnwindData |  |
| 10 | `SnmpTfxOpen` | `0x44B0` | 55 | UnwindData |  |
| 25 | `SnmpUtilOidCmp` | `0x4600` | 200 | UnwindData |  |
| 35 | `SnmpUtilVarBindCpy` | `0x46D0` | 135 | UnwindData |  |
| 26 | `SnmpUtilOidCpy` | `0x4760` | 63 | UnwindData |  |
| 28 | `SnmpUtilOidNCmp` | `0x4850` | 231 | UnwindData |  |
| 24 | `SnmpUtilOidAppend` | `0x4940` | 87 | UnwindData |  |
| 2 | `SnmpSvcAddrToSocket` | `0x4A70` | 145 | UnwindData |  |
| 1 | `SnmpSvcAddrIsIpx` | `0x4CB0` | 209 | UnwindData |  |
| 4 | `SnmpSvcGetUptime` | `0x4E50` | 194 | UnwindData |  |
| 7 | `SnmpSvcSetLogLevel` | `0x5B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `SnmpSvcSetLogType` | `0x5BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `SnmpUtilDbgPrint` | `0x5BB0` | 274 | UnwindData |  |
| 20 | `SnmpUtilOctetsCmp` | `0x5CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `SnmpUtilOctetsNCmp` | `0x5CF0` | 133 | UnwindData |  |
| 30 | `SnmpUtilPrintAsnAny` | `0x5D80` | 1,034 | UnwindData |  |
| 31 | `SnmpUtilPrintOid` | `0x6190` | 160 | UnwindData |  |
| 9 | `SnmpTfxClose` | `0x63D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `SnmpUtilIdsToA` | `0x63E0` | 282 | UnwindData |  |
| 29 | `SnmpUtilOidToA` | `0x6500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `SnmpSvcGetEnterpriseOID` | `0x6520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `SnmpUtilAnsiToUnicode` | `0x6530` | 272 | UnwindData |  |
| 32 | `SnmpUtilUTF8ToUnicode` | `0x6650` | 272 | UnwindData |  |
| 33 | `SnmpUtilUnicodeToAnsi` | `0x6770` | 282 | UnwindData |  |
| 34 | `SnmpUtilUnicodeToUTF8` | `0x6890` | 288 | UnwindData |  |
| 5 | `SnmpSvcGetUptimeFromTime` | `0x69C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `SnmpSvcInitUptime` | `0x6A00` | 124 | UnwindData |  |
| 37 | `SnmpUtilVarBindListCpy` | `0x6A90` | 228 | UnwindData |  |
