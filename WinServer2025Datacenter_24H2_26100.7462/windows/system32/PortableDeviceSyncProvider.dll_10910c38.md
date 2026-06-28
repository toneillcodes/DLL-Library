# Binary Specification: PortableDeviceSyncProvider.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\PortableDeviceSyncProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `10910c3852a872cded0fa4ca623f7e47347010b5db600ebd532ce730524f9518`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x5280` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x52B0` | 384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x5430` | 76 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x5490` | 120,880 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
