# Binary Specification: Wpc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Wpc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `cca9118f47e0289f968616d5a869f5647ea95db8c90c5bffeb0965d22b82c83d`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x9280` | 590 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0xD0A0` | 842 | UnwindData |  |
| 3 | `DllGetClassObject` | `0xD670` | 645 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x1EFA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x1EFD0` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `WpcTimeRestrictionsCreateLocalOverride` | `0x1F160` | 150 | UnwindData |  |
