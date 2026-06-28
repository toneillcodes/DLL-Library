# Binary Specification: msmpeg2vdec.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\msmpeg2vdec.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `68080b2ac9d55310796c7a9ba13924f739d66dab9ac8fcc2e330bf2d24ac0a54`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `DllGetClassObject` | `0x9AFF0` | 380 | UnwindData |  |
| 1 | `GetH264DecoderFunctionTable` | `0xBD740` | 242 | UnwindData |  |
| 2 | `?GetSurface@CVIDEOfilter@@QEAAJHPEAEJ@Z` | `0xBE750` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `?GetSurfaceSize@CVIDEOfilter@@QEAAJHPEAJ@Z` | `0xBE770` | 8,528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `?LoadSurface@CVIDEOfilter@@QEAAJHPEAEK@Z` | `0xC08C0` | 22,544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DllRegisterServer` | `0xC60D0` | 1,143 | UnwindData |  |
| 8 | `DllUnregisterServer` | `0xC6550` | 121 | UnwindData |  |
| 5 | `DllCanUnloadNow` | `0x199510` | 411,660 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
