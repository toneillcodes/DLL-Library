# Binary Specification: netprofm.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\netprofm.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b53bab97989a391cee5c11c6ead2c1e26800b778e9584e79e50e257d0901ca07`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `InitHelperDll` | `0xA3D0` | 213 | UnwindData |  |
| 3 | `DllGetClassObject` | `0xC640` | 784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0xC950` | 41 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x169B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x169C0` | 190,821 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
