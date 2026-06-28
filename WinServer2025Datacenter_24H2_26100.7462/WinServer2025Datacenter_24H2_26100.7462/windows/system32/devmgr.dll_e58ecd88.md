# Binary Specification: devmgr.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\devmgr.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e58ecd88db876728d818bc21239f609e02ddcbbc32e2f376d676897d986bdd6b`
* **Total Exported Functions:** 27

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 15 | `DllCanUnloadNow` | `0x1FAD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `DllGetClassObject` | `0x1FAF0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `DllRegisterServer` | `0x1FBB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `DllUnregisterServer` | `0x1FBC0` | 108,592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `DeviceAction_RunDLLA` | `0x3A3F0` | 55 | UnwindData |  |
| 29 | `DeviceAction_RunDLLW` | `0x3A430` | 43 | UnwindData |  |
| 17 | `DeviceAdvancedPropertiesA` | `0x3A470` | 86 | UnwindData |  |
| 18 | `DeviceAdvancedPropertiesW` | `0x3A4D0` | 75 | UnwindData |  |
| 26 | `DeviceExecuteActionA` | `0x3A530` | 155 | UnwindData |  |
| 27 | `DeviceExecuteActionW` | `0x3A5E0` | 118 | UnwindData |  |
| 9 | `DeviceManager_ExecuteA` | `0x3A660` | 52 | UnwindData |  |
| 10 | `DeviceManager_ExecuteW` | `0x3A660` | 52 | UnwindData |  |
| 11 | `DeviceProblemTextA` | `0x3A6A0` | 234 | UnwindData |  |
| 12 | `DeviceProblemTextW` | `0x3A790` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `DeviceProblemWizardA` | `0x3A7B0` | 100 | UnwindData |  |
| 14 | `DeviceProblemWizardW` | `0x3A820` | 75 | UnwindData |  |
| 23 | `DeviceProblenWizard_RunDLLA` | `0x3A880` | 57 | UnwindData |  |
| 24 | `DeviceProblenWizard_RunDLLW` | `0x3A8C0` | 45 | UnwindData |  |
| 7 | `DevicePropertiesA` | `0x3A900` | 123 | UnwindData |  |
| 21 | `DevicePropertiesExA` | `0x3A990` | 127 | UnwindData |  |
| 22 | `DevicePropertiesExW` | `0x3AA20` | 86 | UnwindData |  |
| 8 | `DevicePropertiesW` | `0x3AA80` | 94 | UnwindData |  |
| 5 | `DeviceProperties_RunDLLA` | `0x3AAF0` | 57 | UnwindData |  |
| 6 | `DeviceProperties_RunDLLW` | `0x3AB30` | 45 | UnwindData |  |
| 19 | `DeviceCreateHardwarePage` | `0x3F0E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `DeviceCreateHardwarePageCustom` | `0x3F100` | 228 | UnwindData |  |
| 20 | `DeviceCreateHardwarePageEx` | `0x3F1F0` | 256 | UnwindData |  |
