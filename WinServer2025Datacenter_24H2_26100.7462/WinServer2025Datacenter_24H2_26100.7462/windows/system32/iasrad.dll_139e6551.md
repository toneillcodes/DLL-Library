# Binary Specification: iasrad.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\iasrad.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `139e6551a562e0b52142f706763f962fe8b1cc96e5c9a070c37162e69ba90912`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `DllCanUnloadNow` | `0x85E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DllGetClassObject` | `0x8600` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `DllRegisterServer` | `0x8730` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `DllUnregisterServer` | `0x8750` | 33 | UnwindData |  |
| 1 | `?initialize@VSAFilter@@QEAAJXZ` | `0x12E70` | 928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `?radiusFromIAS@VSAFilter@@QEBAJPEAUIAttributesRaw@@H@Z` | `0x13210` | 455 | UnwindData |  |
| 3 | `?radiusToIAS@VSAFilter@@QEBAJPEAEKAEAVIASAttributeVector@IASTL@@@Z` | `0x134D0` | 536 | UnwindData |  |
| 4 | `?radiusToIAS@VSAFilter@@QEBAJPEAUIAttributesRaw@@@Z` | `0x136F0` | 207 | UnwindData |  |
| 5 | `?shutdown@VSAFilter@@QEAAJXZ` | `0x137D0` | 50 | UnwindData |  |
