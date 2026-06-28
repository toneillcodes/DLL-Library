# Binary Specification: Windows.Networking.BackgroundTransfer.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Windows.Networking.BackgroundTransfer.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f3f51303dde8acccc72aa06334cee7986dd4593ef28f48266346b16e61e29ad5`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `DllMain` | `0x49350` | 102 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x4A2C0` | 65 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x4A310` | 229 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0x4C5F0` | 83 | UnwindData |  |
| 5 | `DllRegisterServer` | `0xB4E70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `DllUnregisterServer` | `0xB4EA0` | 2,076 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
