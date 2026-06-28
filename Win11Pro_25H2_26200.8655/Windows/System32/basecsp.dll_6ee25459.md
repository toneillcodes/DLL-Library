# Binary Specification: basecsp.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\basecsp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6ee25459fe6c8ceab32cb3c9cd33145a1e5a36b47079fbe0cbe89c9e8493855b`
* **Total Exported Functions:** 28

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CPAcquireContext` | `0x19B80` | 19 | UnwindData |  |
| 2 | `CPAcquireContextW` | `0x19D80` | 19 | UnwindData |  |
| 3 | `CPCreateHash` | `0x1A060` | 29 | UnwindData |  |
| 4 | `CPDecrypt` | `0x1A220` | 56 | UnwindData |  |
| 5 | `CPDeriveKey` | `0x1A370` | 29 | UnwindData |  |
| 6 | `CPDestroyHash` | `0x1A530` | 74 | UnwindData |  |
| 7 | `CPDestroyKey` | `0x1A580` | 74 | UnwindData |  |
| 8 | `CPDuplicateHash` | `0x1A5D0` | 29 | UnwindData |  |
| 9 | `CPDuplicateKey` | `0x1A770` | 29 | UnwindData |  |
| 10 | `CPEncrypt` | `0x1A910` | 67 | UnwindData |  |
| 11 | `CPExportKey` | `0x1AA80` | 56 | UnwindData |  |
| 12 | `CPGenKey` | `0x1ABD0` | 19 | UnwindData |  |
| 13 | `CPGenRandom` | `0x1AD70` | 19 | UnwindData |  |
| 14 | `CPGetHashParam` | `0x1AE40` | 37 | UnwindData |  |
| 15 | `CPGetKeyParam` | `0x1AF60` | 37 | UnwindData |  |
| 16 | `CPGetProvParam` | `0x1B0B0` | 27 | UnwindData |  |
| 17 | `CPGetUserKey` | `0x1B390` | 19 | UnwindData |  |
| 18 | `CPHashData` | `0x1B500` | 27 | UnwindData |  |
| 19 | `CPHashSessionKey` | `0x1B600` | 19 | UnwindData |  |
| 20 | `CPImportKey` | `0x1B6F0` | 37 | UnwindData |  |
| 21 | `CPReleaseContext` | `0x1B8D0` | 116 | UnwindData |  |
| 22 | `CPSetHashParam` | `0x1B950` | 27 | UnwindData |  |
| 23 | `CPSetKeyParam` | `0x1BA50` | 27 | UnwindData |  |
| 24 | `CPSetProvParam` | `0x1BB50` | 19 | UnwindData |  |
| 25 | `CPSignHash` | `0x1BC40` | 56 | UnwindData |  |
| 26 | `CPVerifySignature` | `0x1BD80` | 43 | UnwindData |  |
| 27 | `DllRegisterServer` | `0x1C160` | 434 | UnwindData |  |
| 28 | `DllUnregisterServer` | `0x1C320` | 69,804 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
