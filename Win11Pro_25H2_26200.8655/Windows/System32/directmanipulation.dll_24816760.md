# Binary Specification: directmanipulation.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\directmanipulation.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `24816760a9d3322c496aeae5043bd38bc83ab62c2423cfc1fbdaac8489178e4e`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `DllGetClassObject` | `0x48F00` | 647 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0x49650` | 413 | UnwindData |  |
| 1 | `InitializeDManipHook` | `0x57340` | 50,464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetActivationFactory` | `0x63860` | 127 | UnwindData |  |
