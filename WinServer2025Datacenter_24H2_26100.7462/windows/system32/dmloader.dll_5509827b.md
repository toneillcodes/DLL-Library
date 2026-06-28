# Binary Specification: dmloader.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dmloader.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5509827bda4bac495c5f36b45b45c55716b82bc5145b01ad53bf1c2fc7effc4b`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x84B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x84E0` | 232 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x8610` | 88 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x8670` | 64 | UnwindData |  |
