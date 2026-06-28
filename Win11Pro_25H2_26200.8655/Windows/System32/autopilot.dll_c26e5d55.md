# Binary Specification: autopilot.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\autopilot.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c26e5d55bf0679c3edaaf12a0569e2cbf89446f081f8758f046695de7953e4bb`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 8 | `DllRegisterServer` | `0x8970` | 17,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `DllUnregisterServer` | `0x8970` | 17,008 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `AutoPilotGetOobeSettingsOverride` | `0xCBE0` | 311 | UnwindData |  |
| 2 | `AutoPilotGetPolicyDwordByName` | `0xCD20` | 300 | UnwindData |  |
| 3 | `AutoPilotGetPolicyStringByName` | `0xCE60` | 163 | UnwindData |  |
| 4 | `AutoPilotIsLocalProfileAvailable` | `0xCF10` | 242 | UnwindData |  |
| 5 | `AutoPilotIsNetworkRequired` | `0xD010` | 689 | UnwindData |  |
| 6 | `DllCanUnloadNow` | `0xD2D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DllGetClassObject` | `0xD2F0` | 162 | UnwindData |  |
