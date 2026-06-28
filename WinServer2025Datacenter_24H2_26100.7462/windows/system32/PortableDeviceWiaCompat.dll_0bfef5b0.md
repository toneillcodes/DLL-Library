# Binary Specification: PortableDeviceWiaCompat.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\PortableDeviceWiaCompat.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0bfef5b09bae0543fe188a2089db36c720ae2376e511189370deb1bc8ef23989`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xA850` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0xA870` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0xA920` | 91 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0xA990` | 63,920 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
