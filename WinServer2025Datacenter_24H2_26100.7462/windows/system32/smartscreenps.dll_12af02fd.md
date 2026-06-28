# Binary Specification: smartscreenps.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\smartscreenps.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `12af02fd5ebf32babf54631435cd9bca0fc4c812e1f88aa88411c54583962aae`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xBAE0` | 58 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0xBB20` | 255 | UnwindData |  |
| 3 | `DllGetClassObject` | `0xBC30` | 53 | UnwindData |  |
| 4 | `DllRegisterServer` | `0xBC90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0xBCC0` | 1,388 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
