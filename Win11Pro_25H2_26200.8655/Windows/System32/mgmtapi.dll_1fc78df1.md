# Binary Specification: mgmtapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\mgmtapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1fc78df1e12e6b01ce3ae4578e352577e0c5516c8366aa9cbfd0a035d0c0df98`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `SnmpMgrClose` | `0x2EC0` | 193 | UnwindData |  |
| 2 | `SnmpMgrCtl` | `0x2F90` | 133 | UnwindData |  |
| 3 | `SnmpMgrGetTrap` | `0x3020` | 51 | UnwindData |  |
| 4 | `SnmpMgrGetTrapEx` | `0x3060` | 403 | UnwindData |  |
| 5 | `SnmpMgrOidToStr` | `0x3200` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `SnmpMgrOpen` | `0x3220` | 293 | UnwindData |  |
| 7 | `SnmpMgrRequest` | `0x3350` | 361 | UnwindData |  |
| 8 | `SnmpMgrStrToOid` | `0x34C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `SnmpMgrTrapListen` | `0x34E0` | 99 | UnwindData |  |
