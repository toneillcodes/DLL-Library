# Binary Specification: kerberos.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\kerberos.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0e56c3679080f38a1db1745a3866ef7f27a0f0559132b4026a2c2851d1e118cc`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `SpUserModeInitialize` | `0x62C00` | 312 | UnwindData |  |
| 32 | `SpInstanceInit` | `0x68890` | 376 | UnwindData |  |
| 5 | `DllMain` | `0x6B750` | 40 | UnwindData |  |
| 3 | `SpLsaModeInitialize` | `0x81240` | 592 | UnwindData |  |
| 2 | `KerbDomainChangeCallback` | `0x916A0` | 255 | UnwindData |  |
| 7 | `KerbIsInitialized` | `0x9A3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `KerbKdcCallBack` | `0x9A3F0` | 676 | UnwindData |  |
| 10 | `Kerberos` | `0x9A6A0` | 976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `SpInitialize` | `0x9AA70` | 2,932 | UnwindData |  |
| 6 | `KerbCreateTokenFromTicketForKdc` | `0xA01D0` | 351 | UnwindData |  |
| 9 | `KerbMakeKdcCall` | `0xA4B10` | 222 | UnwindData |  |
