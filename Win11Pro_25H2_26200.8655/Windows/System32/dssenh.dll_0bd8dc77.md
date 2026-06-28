# Binary Specification: dssenh.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\dssenh.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0bd8dc77a884d95d1abc911857729fef8b154154e1edb4a609b9d5d31067847d`
* **Total Exported Functions:** 27

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CPAcquireContext` | `0x1010` | 1,082 | UnwindData |  |
| 2 | `CPCreateHash` | `0x26B0` | 384 | UnwindData |  |
| 17 | `CPHashData` | `0x3120` | 164 | UnwindData |  |
| 25 | `CPVerifySignature` | `0x3860` | 396 | UnwindData |  |
| 13 | `CPGetHashParam` | `0x3AF0` | 327 | UnwindData |  |
| 20 | `CPReleaseContext` | `0x4630` | 59 | UnwindData |  |
| 5 | `CPDestroyHash` | `0x4A40` | 75 | UnwindData |  |
| 11 | `CPGenKey` | `0x5220` | 1,869 | UnwindData |  |
| 15 | `CPGetProvParam` | `0x5D70` | 1,699 | UnwindData |  |
| 19 | `CPImportKey` | `0x6960` | 3,094 | UnwindData |  |
| 22 | `CPSetKeyParam` | `0xA710` | 357 | UnwindData |  |
| 10 | `CPExportKey` | `0xA880` | 817 | UnwindData |  |
| 3 | `CPDecrypt` | `0x112F0` | 339 | UnwindData |  |
| 9 | `CPEncrypt` | `0x11450` | 370 | UnwindData |  |
| 7 | `CPDuplicateHash` | `0x115D0` | 247 | UnwindData |  |
| 18 | `CPHashSessionKey` | `0x116D0` | 439 | UnwindData |  |
| 21 | `CPSetHashParam` | `0x11890` | 109 | UnwindData |  |
| 4 | `CPDeriveKey` | `0x11910` | 518 | UnwindData |  |
| 6 | `CPDestroyKey` | `0x11B20` | 79 | UnwindData |  |
| 8 | `CPDuplicateKey` | `0x11B80` | 243 | UnwindData |  |
| 14 | `CPGetKeyParam` | `0x11C80` | 131 | UnwindData |  |
| 16 | `CPGetUserKey` | `0x11D10` | 405 | UnwindData |  |
| 24 | `CPSignHash` | `0x122C0` | 345 | UnwindData |  |
| 23 | `CPSetProvParam` | `0x12420` | 435 | UnwindData |  |
| 12 | `CPGenRandom` | `0x125E0` | 75 | UnwindData |  |
| 26 | `DllRegisterServer` | `0x12640` | 169 | UnwindData |  |
| 27 | `DllUnregisterServer` | `0x126F0` | 26,518 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
