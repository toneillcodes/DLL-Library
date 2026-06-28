# Binary Specification: basecsp.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\basecsp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `78db22f663dcd66923568aba76998070a05fc76e20180a3a40530ae9bd846189`
* **Total Exported Functions:** 28

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CPAcquireContext` | `0xFA10` | 19 | UnwindData |  |
| 2 | `CPAcquireContextW` | `0xFC10` | 19 | UnwindData |  |
| 3 | `CPCreateHash` | `0xFEF0` | 29 | UnwindData |  |
| 4 | `CPDecrypt` | `0x100B0` | 56 | UnwindData |  |
| 5 | `CPDeriveKey` | `0x10200` | 29 | UnwindData |  |
| 6 | `CPDestroyHash` | `0x103C0` | 74 | UnwindData |  |
| 7 | `CPDestroyKey` | `0x10410` | 74 | UnwindData |  |
| 8 | `CPDuplicateHash` | `0x10460` | 29 | UnwindData |  |
| 9 | `CPDuplicateKey` | `0x10600` | 29 | UnwindData |  |
| 10 | `CPEncrypt` | `0x107A0` | 67 | UnwindData |  |
| 11 | `CPExportKey` | `0x10910` | 56 | UnwindData |  |
| 12 | `CPGenKey` | `0x10A60` | 19 | UnwindData |  |
| 13 | `CPGenRandom` | `0x10C00` | 19 | UnwindData |  |
| 14 | `CPGetHashParam` | `0x10CD0` | 37 | UnwindData |  |
| 15 | `CPGetKeyParam` | `0x10DF0` | 37 | UnwindData |  |
| 16 | `CPGetProvParam` | `0x10F40` | 27 | UnwindData |  |
| 17 | `CPGetUserKey` | `0x11220` | 19 | UnwindData |  |
| 18 | `CPHashData` | `0x11390` | 27 | UnwindData |  |
| 19 | `CPHashSessionKey` | `0x11490` | 19 | UnwindData |  |
| 20 | `CPImportKey` | `0x11580` | 37 | UnwindData |  |
| 21 | `CPReleaseContext` | `0x11760` | 116 | UnwindData |  |
| 22 | `CPSetHashParam` | `0x117E0` | 27 | UnwindData |  |
| 23 | `CPSetKeyParam` | `0x118E0` | 27 | UnwindData |  |
| 24 | `CPSetProvParam` | `0x119E0` | 19 | UnwindData |  |
| 25 | `CPSignHash` | `0x11AD0` | 56 | UnwindData |  |
| 26 | `CPVerifySignature` | `0x11C10` | 43 | UnwindData |  |
| 27 | `DllRegisterServer` | `0x11FF0` | 434 | UnwindData |  |
| 28 | `DllUnregisterServer` | `0x121B0` | 73,500 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
