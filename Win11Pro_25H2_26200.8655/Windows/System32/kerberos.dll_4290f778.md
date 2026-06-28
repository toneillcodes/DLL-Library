# Binary Specification: kerberos.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\kerberos.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4290f7784dc7cae7c0704e6be051bb03a98001ae8a9c8363f0e25d3a968a6f75`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `SpUserModeInitialize` | `0x60FE0` | 312 | UnwindData |  |
| 32 | `SpInstanceInit` | `0x66A00` | 376 | UnwindData |  |
| 5 | `DllMain` | `0x69ED0` | 40 | UnwindData |  |
| 3 | `SpLsaModeInitialize` | `0x812C0` | 592 | UnwindData |  |
| 2 | `KerbDomainChangeCallback` | `0x91BB0` | 255 | UnwindData |  |
| 7 | `KerbIsInitialized` | `0x9AF00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `KerbKdcCallBack` | `0x9AF10` | 676 | UnwindData |  |
| 10 | `Kerberos` | `0x9B1C0` | 1,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `SpInitialize` | `0x9B5E0` | 2,932 | UnwindData |  |
| 6 | `KerbCreateTokenFromTicketForKdc` | `0xA0D80` | 351 | UnwindData |  |
| 9 | `KerbMakeKdcCall` | `0xA3C80` | 222 | UnwindData |  |
