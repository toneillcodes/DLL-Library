# Binary Specification: wuapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wuapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8936e2593dea3ed312267bfcf606c850a581d46561b160f0f18f0cc03f95542f`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x7FB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x7FD0` | 187 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x80A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x80C0` | 57,714 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
