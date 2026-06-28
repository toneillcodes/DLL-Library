# Binary Specification: rsaenh.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\rsaenh.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5ef6ecba64fa6aae2748aa5e64929f3de5c4f9f289b964070fb47187c4b8bf42`
* **Total Exported Functions:** 27

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 22 | `CPSetKeyParam` | `0x1950` | 2,820 | UnwindData |  |
| 16 | `CPGetUserKey` | `0x28A0` | 824 | UnwindData |  |
| 11 | `CPGenKey` | `0x2BE0` | 1,906 | UnwindData |  |
| 4 | `CPDeriveKey` | `0x3360` | 2,596 | UnwindData |  |
| 24 | `CPSignHash` | `0x5C90` | 1,907 | UnwindData |  |
| 2 | `CPCreateHash` | `0x6EA0` | 2,900 | UnwindData |  |
| 9 | `CPEncrypt` | `0x7A00` | 173 | UnwindData |  |
| 21 | `CPSetHashParam` | `0x8740` | 3,008 | UnwindData |  |
| 7 | `CPDuplicateHash` | `0x9BE0` | 510 | UnwindData |  |
| 8 | `CPDuplicateKey` | `0xA190` | 715 | UnwindData |  |
| 5 | `CPDestroyHash` | `0xAC20` | 760 | UnwindData |  |
| 6 | `CPDestroyKey` | `0xAF20` | 819 | UnwindData |  |
| 25 | `CPVerifySignature` | `0xB2D0` | 1,214 | UnwindData |  |
| 17 | `CPHashData` | `0xB7A0` | 721 | UnwindData |  |
| 13 | `CPGetHashParam` | `0xBFB0` | 5,704 | UnwindData |  |
| 15 | `CPGetProvParam` | `0x12F50` | 4,327 | UnwindData |  |
| 23 | `CPSetProvParam` | `0x14520` | 1,243 | UnwindData |  |
| 14 | `CPGetKeyParam` | `0x15350` | 2,124 | UnwindData |  |
| 20 | `CPReleaseContext` | `0x15BB0` | 160 | UnwindData |  |
| 1 | `CPAcquireContext` | `0x15F90` | 185 | UnwindData |  |
| 12 | `CPGenRandom` | `0x17500` | 90 | UnwindData |  |
| 18 | `CPHashSessionKey` | `0x1AE00` | 1,129 | UnwindData |  |
| 3 | `CPDecrypt` | `0x1B6D0` | 80 | UnwindData |  |
| 10 | `CPExportKey` | `0x1C0B0` | 5,904 | UnwindData |  |
| 19 | `CPImportKey` | `0x1D7D0` | 7,368 | UnwindData |  |
| 26 | `DllRegisterServer` | `0x21EE0` | 167 | UnwindData |  |
| 27 | `DllUnregisterServer` | `0x21F90` | 20,190 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
