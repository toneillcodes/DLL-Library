# Binary Specification: netprofm.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\netprofm.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0f8aa20170cd8eb9c02d5374afe04e37d4a28c5dbf4dd832261d096c25e6a615`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `InitHelperDll` | `0xA3A0` | 213 | UnwindData |  |
| 3 | `DllGetClassObject` | `0xC5C0` | 784 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0xC8D0` | 41 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x1A3B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x1A3C0` | 167,100 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
