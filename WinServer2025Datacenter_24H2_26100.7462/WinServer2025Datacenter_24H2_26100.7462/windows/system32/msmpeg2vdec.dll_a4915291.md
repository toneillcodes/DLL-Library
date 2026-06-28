# Binary Specification: msmpeg2vdec.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\msmpeg2vdec.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a4915291dfa85f1cbe9ccd72d21e21a2c9acacfa359f4d4cd3e5f0dfd32d687f`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `DllGetClassObject` | `0x9B030` | 380 | UnwindData |  |
| 1 | `GetH264DecoderFunctionTable` | `0xBD670` | 242 | UnwindData |  |
| 2 | `?GetSurface@CVIDEOfilter@@QEAAJHPEAEJ@Z` | `0xBE620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `?GetSurfaceSize@CVIDEOfilter@@QEAAJHPEAJ@Z` | `0xBE640` | 8,528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `?LoadSurface@CVIDEOfilter@@QEAAJHPEAEK@Z` | `0xC0790` | 21,504 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DllRegisterServer` | `0xC5B90` | 1,143 | UnwindData |  |
| 8 | `DllUnregisterServer` | `0xC6010` | 121 | UnwindData |  |
| 5 | `DllCanUnloadNow` | `0x19A4C0` | 416,908 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
