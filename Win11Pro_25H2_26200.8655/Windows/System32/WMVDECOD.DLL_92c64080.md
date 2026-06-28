# Binary Specification: WMVDECOD.DLL

## Binary Metadata
* **Original Path:** `C:\Windows\System32\WMVDECOD.DLL`
* **Architecture:** x64
* **SHA256 Fingerprint:** `92c640804ce698a038c996e2aabb387b6f10b34e44291853cb9f4c663c1bd629`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `DllRegisterServer` | `0xBB880` | 616 | UnwindData |  |
| 6 | `DllUnregisterServer` | `0xBBAF0` | 80 | UnwindData |  |
| 1 | `GetVC1DecoderFunctionTable` | `0xC2CF0` | 366 | UnwindData |  |
| 2 | `CreateInstance` | `0xC3220` | 121 | UnwindData |  |
| 3 | `DllCanUnloadNow` | `0xC3300` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllGetClassObject` | `0xC3330` | 232 | UnwindData |  |
