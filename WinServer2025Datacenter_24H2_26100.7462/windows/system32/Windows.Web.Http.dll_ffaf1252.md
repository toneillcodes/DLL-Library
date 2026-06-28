# Binary Specification: Windows.Web.Http.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Windows.Web.Http.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ffaf125246c6a1b4e9267a0962ec38a18bb0b4792535299438665061b28cdfff`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetActivationFactory` | `0x5BD50` | 822 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x623D0` | 108 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x63CD0` | 136 | UnwindData |  |
| 4 | `DllMain` | `0x7D470` | 112 | UnwindData |  |
| 5 | `DllRegisterServer` | `0xC0E70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllUnregisterServer` | `0xC0EA0` | 15,356 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
