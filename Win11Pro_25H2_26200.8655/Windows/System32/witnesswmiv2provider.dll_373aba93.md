# Binary Specification: witnesswmiv2provider.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\witnesswmiv2provider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `373aba935ec1aefdc382a8fb7db0707d6a9efa07968308e258e9e9bda756db8d`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `MI_Main` | `0x1A30` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x1A90` | 47 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x1AD0` | 119 | UnwindData |  |
| 3 | `DllMain` | `0x1B50` | 82 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x1BB0` | 72 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x1C00` | 65 | UnwindData |  |
| 6 | `GetProviderClassID` | `0x1E20` | 4,912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `WitnessWmiInitialize` | `0x3150` | 600 | UnwindData |  |
| 9 | `WitnessWmiTerminate` | `0x33B0` | 279 | UnwindData |  |
