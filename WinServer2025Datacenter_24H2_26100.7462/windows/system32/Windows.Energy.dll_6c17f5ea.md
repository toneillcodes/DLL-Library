# Binary Specification: Windows.Energy.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Windows.Energy.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6c17f5ea08b58f999a751e87a1ecc3a114af5de839790b5b1aa8c64e96ac1bd3`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xE2E0` | 38 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0xE310` | 165 | UnwindData |  |
| 3 | `DllGetClassObject` | `0xE3C0` | 111 | UnwindData |  |
| 4 | `DllRegisterServer` | `0xE500` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0xE530` | 135,315 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
