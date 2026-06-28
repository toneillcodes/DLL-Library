# Binary Specification: autopilot.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\autopilot.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `68e33f43ae445add845ff9b658b2e5d2ded5d37b04f896fbb8427490585e2460`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 8 | `DllRegisterServer` | `0x8940` | 16,832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `DllUnregisterServer` | `0x8940` | 16,832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `AutoPilotGetOobeSettingsOverride` | `0xCB00` | 311 | UnwindData |  |
| 2 | `AutoPilotGetPolicyDwordByName` | `0xCC40` | 300 | UnwindData |  |
| 3 | `AutoPilotGetPolicyStringByName` | `0xCD80` | 163 | UnwindData |  |
| 4 | `AutoPilotIsLocalProfileAvailable` | `0xCE30` | 242 | UnwindData |  |
| 5 | `AutoPilotIsNetworkRequired` | `0xCF30` | 689 | UnwindData |  |
| 6 | `DllCanUnloadNow` | `0xD1F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DllGetClassObject` | `0xD210` | 162 | UnwindData |  |
