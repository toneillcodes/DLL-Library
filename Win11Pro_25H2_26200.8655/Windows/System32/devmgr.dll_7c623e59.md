# Binary Specification: devmgr.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\devmgr.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7c623e59414c122c2eae2f30896ed774d1fa8688102c760fd047cac0fa2d4ed0`
* **Total Exported Functions:** 27

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 15 | `DllCanUnloadNow` | `0x194D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `DllGetClassObject` | `0x194F0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `DllRegisterServer` | `0x195B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `DllUnregisterServer` | `0x195C0` | 108,992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `DeviceAction_RunDLLA` | `0x33F80` | 55 | UnwindData |  |
| 29 | `DeviceAction_RunDLLW` | `0x33FC0` | 43 | UnwindData |  |
| 17 | `DeviceAdvancedPropertiesA` | `0x34000` | 86 | UnwindData |  |
| 18 | `DeviceAdvancedPropertiesW` | `0x34060` | 75 | UnwindData |  |
| 26 | `DeviceExecuteActionA` | `0x340C0` | 155 | UnwindData |  |
| 27 | `DeviceExecuteActionW` | `0x34170` | 118 | UnwindData |  |
| 9 | `DeviceManager_ExecuteA` | `0x341F0` | 52 | UnwindData |  |
| 10 | `DeviceManager_ExecuteW` | `0x341F0` | 52 | UnwindData |  |
| 11 | `DeviceProblemTextA` | `0x34230` | 234 | UnwindData |  |
| 12 | `DeviceProblemTextW` | `0x34320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `DeviceProblemWizardA` | `0x34340` | 100 | UnwindData |  |
| 14 | `DeviceProblemWizardW` | `0x343B0` | 75 | UnwindData |  |
| 23 | `DeviceProblenWizard_RunDLLA` | `0x34410` | 57 | UnwindData |  |
| 24 | `DeviceProblenWizard_RunDLLW` | `0x34450` | 45 | UnwindData |  |
| 7 | `DevicePropertiesA` | `0x34490` | 123 | UnwindData |  |
| 21 | `DevicePropertiesExA` | `0x34520` | 127 | UnwindData |  |
| 22 | `DevicePropertiesExW` | `0x345B0` | 86 | UnwindData |  |
| 8 | `DevicePropertiesW` | `0x34610` | 94 | UnwindData |  |
| 5 | `DeviceProperties_RunDLLA` | `0x34680` | 57 | UnwindData |  |
| 6 | `DeviceProperties_RunDLLW` | `0x346C0` | 45 | UnwindData |  |
| 19 | `DeviceCreateHardwarePage` | `0x38C70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `DeviceCreateHardwarePageCustom` | `0x38C90` | 228 | UnwindData |  |
| 20 | `DeviceCreateHardwarePageEx` | `0x38D80` | 256 | UnwindData |  |
